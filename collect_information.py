from os      import listdir
from os.path import isfile, join
from pptx    import Presentation
from tikapp  import TikaApp
from tika    import parser
import PyPDF2
import nltk
import re
import csv

class Collect:

	def __init__(self):
		self.collect_programming_language()
		self.collect_resume()
		self.language=[]
		self.resume=[]


	def collect_programming_language(self):
		language=[]
		with open('./db/programming_language.csv', newline='') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
			for row in spamreader:
				lan=', '.join(row)
				language.append(lan)

	def collect_resume_title(self):
		mypath='./db/bank'
		allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		return allfiles

	def collect_resume(self):
		mypath='./db/bank'
		allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		data=[]
		print(allfiles)
		exit(0)
		for i in range(0,len(allfiles)):
			file_data = parser.from_file('./db/bank/'+allfiles[i])
			text = file_data['content']
			print(text)
			data.append(text)


x=Collect()

x.collect_resume()