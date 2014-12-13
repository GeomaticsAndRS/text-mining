from HTMLParser import HTMLParser
import urllib
import urllib2
from numpy import *
import os
import re

class MyHTMLParser(HTMLParser):
	is_abstract = False
	
	def handle_data(self, data):
		if "Descriptions are provided by the Actions directly" in data:
			self.is_abstract= True
			print "\n"
		elif (self.is_abstract & ("Description" == data)):
			self.is_abstract = False
		elif self.is_abstract == True:
			print data.rstrip(),

domain = array(["BMBS", "CMST", "ESSEM", "FA", "FPS", "ISCH", "ICT", "MPNS", "TUD", "TD"])
dm = array(["BM", "CM", "ES", "FA", "FP", "IS", "IC", "MP", "TU", "TD"])

parser = MyHTMLParser()

for i in range(size(domain)):
	for yy in range(6, 15):
		for an in range(1, 11):
			action = dm[i] + str(yy).zfill(2) + str(an).zfill(2)
			
			exists = int(urllib.urlopen("http://www.cost.eu/domains_actions/" + domain[i] + "/Actions/" + action).code) < 400
			
			if exists:
				action_page = urllib2.urlopen("http://www.cost.eu/domains_actions/" + domain[i] + "/Actions/" + action)
				content = action_page.read()
				action_page.close()
				
				parser.feed(content)
