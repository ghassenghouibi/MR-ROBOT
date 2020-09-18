# -*- coding: utf-8 -*-

"""
Created on Friday 14 August 2020 16:58:59

@author : Ghouibi Ghassen
"""
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.tokenize import word_tokenize
import numpy as np
import nltk


class TextProcessing:
	"""This class collect all Resume in these format DOCX,PDF,DOC for ResumeCollector"""
	def __init__(self):
		self.stopwords=stopwords.words('french')
		self.symbols="!\"#$%&()*+-./:;,'’<=>?@[\]^_`{|}~\n–»«"
		self.apostrophe="'"

	def list_to_lower(self,string_list):
		
		for i in range(len(string_list)):
			string_list[i]=string_list[i].lower()

		return string_list

	def removing_stop_words(self,data):
		text_tokens = word_tokenize(data)
		tokens_without_sw = [word for word in text_tokens if not word in self.stopwords]

		return tokens_without_sw


	def removing_punctuation(self,data):
		for x in data:
			if x in self.symbols:
				data = data.replace(x, " ")
		return word_tokenize(data)


	def text_cleaning_from_stop_words_and_punctuation(self,data):
		res=self.removing_stop_words(data)
		res=self.list_to_lower(res)
		return self.removing_punctuation(str(res))


	def transform_to_lower_case(self,data):
		#todo
		print(data)