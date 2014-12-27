library("textcat")
library("translateR")

files <- dir("output/Ambizione")

for(f in files) {
	
	candidate_orig <- paste(scan(paste0("output/Ambizione/", f), what = "character", fileEncoding = "iso-8859-1"), collapse = " ")
	
	language <- textcat(candidate_orig)
	
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
		candidate_eng <- translate(content.vec = c(candidate_orig), microsoft.client.id ="xxx", microsoft.client.secret = "f1yRrF3oIQ3AWiyIQQJWiNI1MfVu8bgIHwiby9yW5Ak=", source.lang = lang, target.lang = 'en')
	} else {
		candidate_eng <- candidate_orig
	}
	
	write(candidate_eng, paste0("output/Ambizione_en/", f))
}
