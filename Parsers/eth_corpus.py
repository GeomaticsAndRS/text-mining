import os
import re
import csv
import string
from numpy import *

myfiles = os.listdir("../Raw/eth")
path = os.getcwd()

my_list = []

eth_csv = open("../output/eth_projects.csv", "w")
eth_writer = csv.writer(eth_csv)

for doc in sort(myfiles):
	if doc.endswith(".pdf"):
		os.system('pdftotext "../Raw/eth/' + doc + '" temp.txt')
		file = open("temp.txt", "r")
		filetext = file.read()
		file.close()
		
		if "Project status: Ongoing" in filetext:
			#print doc
			title = re.findall("Summary(.*?)1\)", filetext, re.DOTALL)[0].replace("\n", " ")
			#print title

			try:
				start = re.findall("4\)(.*?)5\)", filetext, re.DOTALL)[0]
				start = re.findall("..\...\.....", start, re.DOTALL)[0]
			except:
				start = ""
				pass
				
			summary = re.sub("\s+", " ", re.findall("11\) Short Summary:(.*?)12\)", filetext, re.DOTALL)[0]).strip()
			leader = re.sub("\s+", " ", re.findall("6\)(.*?)7\)", filetext, re.DOTALL)[0]).strip()
			leader = leader.replace("Project leader(s): - ", "")
			
			try:
				email = ''.join(re.findall("([_a-z0-9-]+)(\.[_a-z0-9-]+)*(@)([a-z0-9-]+)(\.[a-z0-9-]+)*(\.ch)", leader)[0])
			except:
				email = ""
			
			try:
				leader = leader.split(",")[1] + " " +  leader.split(",")[0]
			except:
				leader = ""
			
			if "no entry" not in summary:
				summary = re.sub("c ETH(.*?)page 1>", "", summary.replace("Short Summary: ", ""), re.DOTALL)
			else:
				summary = ""
			
			outfilename = doc.replace(".pdf", "") + ".txt"
			fileout = open("../Corpora/eth/" + outfilename, "w")
			fileout.writelines(title + "\n" + summary)
			
			print leader, start, title, outfilename
			
			eth_writer.writerow([leader, email, start, title, outfilename])
			
			fileout.close()		

eth_csv.close()
