from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import docx2txt
import pandas as pd
from pyresparser import ResumeParser
from tikapp  import TikaApp
from tika    import parser

class JobDescription:

	def __init__(self,filename,data):
		self.filename=filename
		self.data=data
		self.vector=[]

	def job_description_set_vector(self,vectorinmodel):
		for i in self.data:
			self.vector.append(vectorinmodel[i])


	def print_vector(self):
		for i,j in zip(self.data,self.vector):
			print(i,j)

	def get_vector(self):
		return self.vector