import pandas as pd
import numpy as np
import csv


#To improve collect of job labeling, found matching even if the job is splited
class JobLabel:

	def __init__(self,filename,data):
		self.filename=filename
		self.data=data

	def get_job_names(self):
		df = pd.read_csv('./db/work.csv', index_col='Name')
		return df

	def find_job_names_in_data(self):
		job=[]
		with open('./db/work.csv', newline='') as csvfile:
			spamreader=csv.reader(csvfile, delimiter=' ',quotechar='|')
			for row in spamreader:
				job.append(' '.join(row))

		res=[]
		for j in self.data:
			if j in job:
				res.append(j)

		print(res)
		return res