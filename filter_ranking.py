from numpy import *
import codecs
import datetime

target = "eth"
min_score = 0.33
min_year = 10

score = recfromcsv("output/" + target + '_ranking.csv', delimiter=',')

for i in range(size(score)):
	
	try:
		is_recent = datetime.datetime.strptime(score[i]['date'], "%Y-%m-%d") > datetime.datetime(2011, 1, 1)
	
	except:
		continue
	
	if score[i]['action'] != "":
		#~ if int(score[i]['action'][2:4]) > min_year and score[i]['score'] > min_score and is_recent and score[i]['action'][0:2] == "IS":
		if int(score[i]['action'][2:4]) > min_year and score[i]['score'] > min_score and is_recent:
			print score[i]
			
			matchtext = ""
			
			matchtext += score[i]['description'].strip('"') + "\nStart date: " + score[i]['date'] + "\nResponsible person: " + score[i]['pi'].strip('"') + "\n"
			
			f = open("Corpora/" + target + "/" + score[i]["filename"], 'r')
			matchtext += "".join(f.readlines()) + "\n\n"
			f.close()
			
			print matchtext
			
			matchtext += str(score[i]['action']) + "\n"
			
			f = open("Projects/COST/" + score[i]["action"] + ".txt", 'r')
			matchtext += "".join(f.readlines()) + "\n\n"
			f.close()
			
			try:
				outfile = codecs.open("Matches/"+ target +"/match_" + score[i]["filename"], "w", encoding='utf8')
				outfile.write(matchtext)
			except:
				pass
			#~ outfile.write(unicode(matchtext.decode("utf-8")))
			
			outfile.close()


