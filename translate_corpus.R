library("textcat")
library("translateR")

target <- "zhaw"

files <- dir(paste0("Corpora/", target))

for(f in files) {
	
	candidate_orig <- paste(scan(paste(c("Corpora", target, f),collapse="/"), what = "character", fileEncoding = "iso-8859-1"), collapse = " ")
	
	language <- textcat(candidate_orig)
	
	if (! is.na(language)){
		if (language == "english"){
			lang = "en"
		} else if (language == "french") {
			lang = "fr"
		} else if (language == "german") {
			lang = "de"
		} else if (language == "italian") {
			lang = "it"
		}
	
		if (lang != "en"){
			candidate_eng <- translate(content.vec = c(candidate_orig), microsoft.client.id ="cardiff_text", microsoft.client.secret = "f1yRrF3oIQ3AWiyIQQJWiNI1MfVu8bgIHwiby9yW5Ak=", source.lang = lang, target.lang = 'en')
			write(candidate_eng, paste(c("Corpora_en", target, f), collapse = "/"))
		} else {
			candidate_eng <- candidate_orig
			write(candidate_eng, paste(c("Corpora_en", target, f), collapse = "/"))
		}
	}
	
}
