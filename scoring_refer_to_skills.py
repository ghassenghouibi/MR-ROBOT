from pyresparser import ResumeParser

class Scoring:
	def __init__(self,filename):
		self.job_description = ResumeParser(filename).get_extracted_data()
		self.skills=self.job_description['skills']

	def scoring_candidats_refer_to_skills(self,candidat):
		score=self.searching_skills(self.skills,candidat['skills'])
		return score
			

	def searching_skills(self,doc1,doc2):
		score=0
		for i in doc1:
			if i in doc2:
				score+=1

		return score