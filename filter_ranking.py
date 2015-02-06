from numpy import *
import codecs
import datetime

target = "zhaw"
min_score = 0.33
min_year = 10

score = recfromcsv("output/" + target + '_ranking.csv', delimiter=',')

for i in range(size(score)):
	
	try:
		is_recent = datetime.datetime.strptime(score[i][4], "%Y-%m-%d") > datetime.datetime(2011, 1, 1)
	except:
		continue
		
	if int(score[i][2].strip('"')[2:4]) > min_year and score[i][5] > min_score and is_recent:
		#~ print score[i]
		
		matchtext = ""
		
		matchtext += score[i][1].strip('"') + "\nStart date: " + score[i][4] + "\nResponsible person: " + score[i][3].strip('"') + "\n"
		
		f = open("Corpora/" + target + "/" + score[i][6].strip('"') + ".txt", 'r')
		matchtext += f.readlines()[0] + "\n\n"
		f.close()
		
		matchtext += score[i][2].strip('"') + "\n"
		
		f = open("Projects/COST/" + score[i][2].strip('"') + ".txt", 'r')
		matchtext += f.readlines()[0] + "\n\n"
		f.close()

		outfile = codecs.open("Matches/"+ target +"/match_" + str(i) + ".txt", "w", encoding='utf8')
		outfile.write(unicode(matchtext.decode("utf-8")))
		outfile.close()
