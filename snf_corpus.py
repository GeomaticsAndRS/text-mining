import unicodecsv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HTMLParser import HTMLParser

from pyvirtualdisplay import Display #run Firefox headless 

display = Display(visible=0, size=(800, 600))
display.start()

class MyHTMLParser(HTMLParser):
	is_abstract = False
	content = ''
	
	def get_content(self):
		return self.content

	def reset_content(self):
		self.content = ''
	
	def handle_data(self, data):
		self.content = self.content + " " + data.rstrip()

parser = MyHTMLParser()

with open("input/SNF_ambizione.csv", "r") as csvfile:
	reader = unicodecsv.reader(csvfile, delimiter=',', quotechar='"',skipinitialspace=True, encoding='utf-8')
	next(reader, None)
	for row in reader:
		
		author = unicode(row[1].split(" ")[0] + " " + row[0])

		print author

		browser = webdriver.Firefox()
		browser.get('http://p3.snf.ch/')

		elem = browser.find_element_by_name('ctl00$cphNavigationSearch$ucSearchNavigationPanel$txtCriteria')  # Find the search box
		elem.send_keys(author + Keys.RETURN)

		try:	
			elem = browser.find_element_by_partial_link_text("Ambizione")
			elem.click()
		except:
			try:
				elem = browser.find_element_by_partial_link_text("Fellowships for prospective")
				elem.click()
			except:
				browser.quit()
				continue
			
		elemts = browser.find_elements_by_class_name("click")
		for elem in elemts:
			try:
				elem.click()
			except:
				pass

		try:
			elem = browser.find_element_by_partial_link_text("Direct link to Lay Summary")
			elem.click()

			aw = browser.window_handles
			browser.switch_to_window(aw[1])
		except:
			browser.quit()
			continue
		
		outfile = open("Corpora/Ambizione/" + author.strip("") + ".txt", 'w+') 
		parser.feed(browser.page_source.encode("iso-8859-1", "replace"))
		outfile.write(parser.get_content())
		parser.reset_content()
		outfile.close()

		browser.quit()
