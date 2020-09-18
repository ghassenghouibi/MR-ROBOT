import pandas as pd
import numpy as np
import csv
from nltk.tokenize import word_tokenize


class LanguagesLabel:

	def __init__(self,filename,data):
		self.filename=filename
		self.data=data

	def get_languages_names(self):
		df = pd.read_csv('./db/langues.csv', index_col='Name')
		return df

	def find_languages_names_in_data(self):
		languages=[]
		with open('./db/langues.csv', newline='') as csvfile:
			spamreader=csv.reader(csvfile, delimiter=' ',quotechar='|')
			for row in spamreader:
				languages.append(' '.join(row))

		res=[]
		for j in self.data:
			if j in languages:
				res.append(j)

		return res