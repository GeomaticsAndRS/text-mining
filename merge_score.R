target = 'eth' 

projects <- read.csv(paste(c("output/", target, "_projects.csv"), collapse = ""))
score <- read.csv(paste(c("output/", target, "_score.csv"), collapse = ""))
projects$Project <- gsub(".txt", "", projects$File)

result <- merge(score, projects, by = "Project")
result$Date <- as.Date(as.vector(result$Date), "%d.%m.%Y")

write.csv(result, paste(c("output/", target, "_ranking.csv"), collapse = ""))
