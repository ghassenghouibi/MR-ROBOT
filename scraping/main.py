from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re


class Scraping:

	def __init__(self,filename):
		self.filename=filename
		self.driver = webdriver.Chrome("/usr/bin/chromedriver")
		self.names=[]
		self.url="https://fr.wikipedia.org/wiki/Liste_de_langages_de_programmation"
		self.driver.get(self.url)
		self.content = self.driver.page_source
		self.soup = BeautifulSoup(self.content,features="lxml")
		self.find()
		self.export()


	def cleanhtml(self,raw_html):
	  cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
	  cleantext = re.sub(cleanr, '', raw_html)
	  return cleantext



	def find(self):
		for a in self.soup.findAll('div',href=False, attrs={'class':'colonnes'}):
			self.name=a.find('ul')
			self.names.append(self.cleanhtml(str(self.name)))

	def export(self):
		df = pd.DataFrame({'Name':self.names})
		df.to_csv('../db/'+self.filename, index=False, encoding='utf-8')


Scraping("prog-lg.csv")