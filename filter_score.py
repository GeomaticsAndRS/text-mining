from numpy import *
from shutil import *

target = "zhaw"
min_score = 0.26
min_year = 10

score = recfromcsv(target + '_score.csv', delimiter=',')

for i in range(size(score)):
    if int(score[i][2][2:4]) > min_year and score[i][3] > min_score:
		
		print "\n" + score[i][1]
		
		f = open("Corpora/" + target + "/" + score[i][1] + ".txt", 'r')
		print f.readlines()[0]
		f.close()
		
		print score[i][2]
		
		f = open("Projects/COST/" + score[i][2] + ".txt", 'r')
		print f.readlines()[0] + "\n"
		f.close()

		print "********************************************************************"
