#~ Machine download reports from the ETH database website

import urllib2
from numpy import *
import os

M = 1
N = 40000

for i in range(M, N):
	
	try:
		f = urllib2.urlopen("https://www.rdb.ethz.ch/projects/project_pdflatex.php?proj_id=" + str(i) + ".pdf")
		content = f.read()
	except urllib2.URLError:
		continue
	
	if not "You do not have enough rights on this project" in content:
		with open("../Raw/eth/project-" + str(i) + ".pdf", "wb") as code:
			print i
			code.write(content)
