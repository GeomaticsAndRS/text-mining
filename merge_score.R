target = 'zhaw' 

projects <- read.csv(paste(c("output/", target, "_projects.csv"), collapse = ""))
score <- read.csv(paste(c("output/", target, "_score.csv"), collapse = ""))
projects$id <- as.vector(sapply(x = projects$Path, FUN = gsub, paste(c("Corpora/", target, "/(.+?)_(.+?).txt"),collapse=""), "\\2"))
score$id <- as.vector(sapply(x = score$Name, FUN = gsub, "projekt-detail_(.+?)", "\\1"))
result <- merge(score, projects, by = "id")
result2 <- data.frame(Title = result$Title, Action = result$Project, Name = result$PI, Start.Date = result$Start.Date, Score = result$Score, File = result$Name)
result2$Title <- as.vector(sapply(x = result2$Title, FUN = gsub, ",", ""))
result2$Name[grep(",", result2$Name)] <- ""
result2$Name[grep(":", result2$Name)] <- ""
result2$Start.Date <- as.Date(as.vector(result2$Start.Date), "%d.%m.%Y")
write.csv(result2, paste(c("output/", target, "_ranking.csv"), collapse = ""))
