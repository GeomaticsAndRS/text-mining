from HTMLParser import HTMLParser
import os
import glob
from numpy import *
import re
import csv

class MyHTMLParser(HTMLParser):
	is_over = False
	assume_ok = False
	next_leader = False
	content = ''
	leader = ''
	start = ''
	
	def reset_content(self):
		self.content = ''
		self.leader = ''
		self.start = ''
		self.is_over = False	
		self.assume_ok = False	
		self.next_leader = False	
	
	def get_content(self):
		return self.content

	def get_title(self):
		return self.content
		
	def get_leader(self):
		return self.leader

	def get_start(self):
		return self.start
	
	def handle_data(self, data):
		if (data != "\n" and data != "" and data != ","): 
			if "var pkBaseURL" in data:
				self.is_over = True
			elif "Projektbeginn" in data:
				self.start = data
				self.assume_ok = True
			elif "Projektleiter/in" in data or "Project leader" in data:
				self.next_leader = True
			elif self.assume_ok == True and self.is_over == False:
				if not ("http" in data) and not ("rende Informationen:" in data) and not ("ProjektpartnerInnen:" in data) and not ("Start date " in data):
					self.content = self.content + " " + data.rstrip()
			elif self.next_leader == True and self.assume_ok == False:
				self.leader = self.leader + data
				self.next_leader = False

zhaw_csv = open("zhaw_projects.csv", "w")
zhaw_writer = csv.writer(zhaw_csv)

for proj in sort(glob.glob("Raw/zhaw/projekt-detail*")):
	
	parser = MyHTMLParser()
	
	projfile = open(proj, "r")
	content = projfile.read().decode("utf-8")
	projfile.close()
	
	parser.feed(content)
	
	try:
		title = re.findall("Projekte ZHAW: (.+)</title", content.encode('ascii', 'ignore'))[0].strip()
		start = parser.get_start()[-10:]
	except:
		parser.reset_content()
		continue
	
	print title
	
	leader = unicode(parser.get_leader()).encode("utf-8")
	outfilename = proj.replace("Raw", "Corpora").replace(".php", "").replace(".html", ".txt")
	
	zhaw_writer.writerow([leader, start, title, outfilename])
	
	outfile = open(outfilename, 'w+') 
	contenttext = parser.get_content().strip()
	
	outfile.write(contenttext.encode("utf-8"))
	outfile.close()
	
	parser.reset_content()
	
zhaw_csv.close()
