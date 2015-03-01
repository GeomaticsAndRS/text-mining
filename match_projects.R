library("tm")

target <- "eth"

files <- dir(paste0("Corpora_en/", target))

name <- vector()
project <- vector()
score <- vector()
	
for(f in files) {
	
	candidate <- paste(scan(paste(c("Corpora", target, f),collapse="/"), what = "character", fileEncoding = "iso-8859-1"), collapse = " ")
	candidate <- Corpus(VectorSource(candidate), readerControl = list(reader=readPlain))
	
	cost <-Corpus(DirSource("Projects/COSTrecent"), readerControl = list(reader=readPlain, language="eng"))
	
	cost_cand <- c(cost, candidate)

	## Convert to Plain Text Documents
	cost_cand <- tm_map(cost_cand, PlainTextDocument)

	## Remove common words
	cost_cand <- tm_map(cost_cand, removeWords, c("COST", "Lay summary", "Lead"))

	## Convert to Lower Case
	cost_cand <- tm_map(cost_cand, content_transformer(tolower))

	## Remove other common words
	cost_cand <- tm_map(cost_cand, removeWords, c("main objective", "action", "develop", "apply", "collaboration", "coordination", "networks", "network", "european", "europe", "research", "researchers", "researching", "science", "scientific", "will", "promote", "scientist", "scientists", "understand", "knowledge", "across", "workshops", "approach", "understanding", "keywords"))

	## Remove Stopwords
	cost_cand <- tm_map(cost_cand, removeWords, stopwords("english"))

	## Remove Punctuations
	cost_cand <- tm_map(cost_cand, removePunctuation)

	## Stemming
	cost_cand <- tm_map(cost_cand, stemDocument)

	## Remove Numbers
	cost_cand <- tm_map(cost_cand, removeNumbers)

	cost_cand <- tm_map(cost_cand, stripWhitespace)

	dtm <- DocumentTermMatrix(cost_cand)

	dtm_tfxidf <- weightTfIdf(dtm)

	m <- as.matrix(dtm_tfxidf)
	rownames(m) <- 1:nrow(m)

	### don't forget to normalize the vectors so Euclidean makes sense
	norm_eucl <- function(m) m/apply(m, MARGIN=1, FUN=function(x) sum(x^2)^.5)
	m_norm <- norm_eucl(m)

	names <- list.files("Projects/COSTrecent")

	query <-  as.numeric(as.matrix(t(m_norm[nrow(m_norm),])))
	M <- as.matrix(t(m_norm[1:nrow(m_norm)-1,]))
	
	prod <- query %*% M
	
	
	new_name <- gsub(".txt", "", f, perl = FALSE)
	new_project <- gsub(".txt", "", names[which.max(prod)], perl = FALSE)
	new_score <- max(prod)
	 
	if (sum(is.na(c(new_name, new_project, new_score)))==0){
		name <- c(name, new_name)
		project <- c(project, new_project)
		score <- c(score, new_score)
		print(c(gsub(".txt", "", f, perl = FALSE), gsub(".txt", "", names[which.max(prod)], perl = FALSE), max(prod)))
	}
}

ranking <- data.frame(Name = name, Project = project, Score = score)
ranking <- ranking[rev(order(ranking$Score)),]

write.csv(ranking, paste(c("output/", target, "_score.csv"), collapse=""), fileEncoding = "utf-8")
