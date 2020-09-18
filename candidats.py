# -*- coding: utf-8 -*-

"""
Created on Friday 14 August 2020 16:58:59

@author : Ghouibi Ghassen
"""
from gensim import corpora
from gensim.utils import simple_preprocess
from gensim import corpora
from transform_text_to_vector import TransformText2Vector
from languages_labeling import LanguagesLabel
from scoring_refer_to_skills import Scoring
import nltk
import sys

class Candidats:
	"""This class contain the candidat informations """
	def __init__(self):
		self.candidats=[]

	def number_of_candidats(self):
		return len(self.candidats)

	def add_new_candidat(self,filename,name,email,mobile_number,degree,experience,skills,designation,total_experience,company_names,clean_text,text,vector):
		candidat={'filename':str(filename),
				  'name':name,
				  'email':email,
				  'mobile_number':mobile_number,
				  'degree':degree,
				  'experience':experience,
				  'skills':skills,
				  'designation':designation,
				  'total_experience':total_experience,
				  'company_names':company_names,
				  'clean_text':clean_text,
				  'languages': LanguagesLabel(filename,clean_text).find_languages_names_in_data(),
				  'text':text,
				  'vector':vector,
				  'score':0
				  }

		score=Scoring(sys.argv[1])
		candidat['score']=score.scoring_candidats_refer_to_skills(candidat)
		

		self.candidats.append(candidat)

		return candidat


	def send_vectors(self):
		vector=[]
		for i in self.candidats:
			vector.append(i['vector'])

		return vector

	def set_vectors(self,vector):
		for i in self.candidats:
			for j in i['clean_text']:
				i['vector'].append(vector[j])
	

	def get_vector(self):
		vector=[]
		for i in self.candidats:
			elem={
				'filename':i['filename'],
				'vector':i['vector']
			}
			vector.append(elem)
		return vector


	def get_candidats_by_filename(self,file_list):
		res=[]
		for j in file_list:
			for i in self.candidats:
				if i['filename']==j:
					res.append(i)
					pass

		return res				

	
	def remove_empty_element(self,x):
		while '' in x:
		    x.remove('')
		return x

	def remove_space(self,x):
		while '' in x:
		    x.remove('')
		return x

	def remove_new_lines(self,text):
		x=list(text.split('\n'))

		str_list = self.remove_empty_element(x)
		str_list = self.remove_space(str_list)
		
		return str_list

	def split_text_to_sentences(self,text):
		text.rstrip("\n")
		nltk.download('punkt')
		a_list = nltk.tokenize.sent_tokenize(text)
		return a_list

	def print_all_resume(self):
		for i in self.candidats:
			self.print_resume_detail(i)

	def print_resume_detail(self,candidat):
		print("---------------------")
		print("The filename :",candidat['filename'],"\n")
		print("Name -->",candidat['name'])
		print("Email -->",candidat['email'])
		print("Mobile -->",candidat['mobile_number'])
		print("Degree -->",candidat['degree'])
		print("Experience -->",candidat['experience'])
		print("Skills -->",candidat['skills'])
		print("Designation -->",candidat['designation'])
		print("Total Experiece -->",candidat['total_experience'])
		print("Company Names -->",candidat['company_names'])
		print("Languages -->",candidat['languages'])
		print("Scoring -->",candidat['score'])
		print("---------------------")

	def tokenize_text(self,text):
		tokens = [[token for token in sentence.split()] for sentence in text]
		gensim_dictionary = corpora.Dictionary(tokens)
		print("The Dictionnary has : "+str(len(gensim_dictionary))+ " tokens")
		for k,v in gensim_dictionary.token2id.items():
			print(f'{k:{15}} {v:{10}}')

	def print_bag_of_words(self,doc):
		tokenized_list = [simple_preprocess(doc) for doc in doc]
		mydict = corpora.Dictionary()
		mycorpus = [mydict.doc2bow(doc,allow_update=True) for doc in tokenized_list]
		word_counts= [[(mydict[id],count) for id, count in line] for line in mycorpus]
		print(word_counts)
		self.saving_bag_of_words(mydict,mycorpus)

	def saving_bag_of_words(self,mydict,corpus):
		mydict.save(' mydict.dict')
		corpora.MmCorpus.serialize('bow_corpus.mm',corpus)

	def load_bag_of_word(self,name):
		load_dict = corpora.Dictionary.load('mydict.dict')
		print(loaded_dict)
		corpus = corpora.MmCorpus('bow_corpus.mm')
		for line in corpus:
			print(line)

	def get_all_candidats(self):
		return self.candidats


	def show_all_files_names(self):
		for i in range(0,len(self.candidats)):
			print(self.candidats[i])

	def get_filename(self):
		return self.filename

	def get_resume(self):
		return self.resume


