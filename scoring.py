import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from math import*

class ScoringCVreferToJobDescription:

	def __init__(self,cvs,jobdescription):
		self.cvs=cvs
		self.jobdescription=jobdescription


	def print_job_description(self):
		"""
		for i in range(0,5):
			print(self.jobdescription[i],len(self.jobdescription[i]))
		"""
		while len(self.jobdescription)!= len(self.cvs[0]['vector']):
			if len(self.jobdescription)>len(self.cvs[0]['vector']):
				self.cvs[0]['vector'].append([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
			elif len(self.jobdescription)<len(self.cvs[0]['vector']):
				self.jobdescription.append([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

		


		
	def print_cvs(self):
		for i in cvs:
			print(i)

	def euclidean_distance(self,x,y):
  		return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))

	def print_scoring_elem(self):
		print("Socring ",len(self.cvs)," CV")

	def square_rooted(self,x):
		res=0.0
		for i in x:
			res+=i*i
		print(sqrt(res))
	 
	def cosine_similarity(self,x,y):
 		numerator = sum(a*b for a,b in zip(x,y))
	 	denominator = self.square_rooted(x)*self.square_rooted(y)
 		return round(numerator/(denominator),3)