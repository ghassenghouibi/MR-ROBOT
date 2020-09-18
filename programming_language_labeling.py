import pandas as pd
import numpy as np
import csv


#usless, often we have pyresparser collector more precision
class ProgrammingLanguageLabel:

	def __init__(self,filename,data):
		self.filename=filename
		self.data=data


	def get_programming_language(self):
		df = pd.read_csv('./db/programming_language.csv', index_col='Name')
		return df

	def find_programming_language_in_data(self):
		pl=[]
		with open('./db/programming_language.csv', newline='') as csvfile:
			spamreader=csv.reader(csvfile, delimiter=' ',quotechar='|')
			for row in spamreader:
				pl.append(', '.join(row))
		res=[]
		for j in self.data:
			j.lower()
			j.capitalize()
			if j in pl:
				if j not in res:
					res.append(j)

		print(res)
		return res