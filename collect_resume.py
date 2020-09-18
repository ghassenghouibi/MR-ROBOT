# -*- coding: utf-8 -*-

"""
Created on Friday 14 August 2020 16:58:59

@author : Ghouibi Ghassen
"""

import docx2txt
import PyPDF2 as p2
from tikapp  import TikaApp
from tika    import parser
import PyPDF2
import textract
import sys
import os
from os      import listdir
from os.path import isfile, join
from candidats import Candidats
from pyresparser import ResumeParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 



class ResumeCollector:
	"""This class collect all Resume in these format DOCX,PDF,DOC for ResumeCollector"""
	def __init__(self):
		self.pdfpath='./db/bank/test'

	def files_length(self):
		return len([x for x in listdir(self.pdfpath) if isfile(join(self.pdfpath, x))])

	def starting_collection_from_pdf(self):
		allfiles = [x for x in listdir(self.pdfpath) if isfile(join(self.pdfpath, x))]
		data=[]
		for i in range(0,len(allfiles)):
			os.environ['TIKA_SERVER_JAR'] = 'https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.19/tika-server-1.19.jar'
			file_data = parser.from_file(self.pdfpath+"/"+allfiles[i])
			text = file_data['content']
			resume = ResumeParser(self.pdfpath+"/"+allfiles[i]).get_extracted_data()
			info={'filename':allfiles[i],'resume':resume,'text':text}
			data.append(info)

		return data	