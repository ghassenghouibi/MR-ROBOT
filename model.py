from gensim.models import word2vec
import gensim 
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from nltk import word_tokenize
from sklearn.manifold import MDS
import numpy as np
import matplotlib.pyplot as plt

class Model:

	def __init__(self,candidats,job_description):
		self.candidats=candidats
		self.job_description=job_description
		self.corpus=[]
		self.model=''


	def get_all_cleaned_text(self):
		#edit the first tag
		self.corpus.append(self.job_description)
		for i in self.candidats:
			self.corpus.append(i)

		self.corpus = [
		    TaggedDocument(words, ['cv{}'.format(idx)])
		    for idx, words in enumerate(self.corpus)
		]
		

		return self.corpus

	def model_word2vec(self):
		
		word_emb=list()
		flat_list = [item for sublist in self.candidats for item in sublist]
		word_emb.append(self.job_description)
		word_emb.append(flat_list)

		model = word2vec.Word2Vec(word_emb,size=10,min_count=1)
		#print(model.most_similar(positive=['python']))

		return model


	def get_dict_model(self):
		w2c = dict()
		for item in self.model.wv.vocab:
		    w2c[item]=self.model.wv.vocab[item].count
		
		cv2vec=[]
		for i in w2c:
			cv2vec.append(self.model[i])

		return cv2vec

	def model_doc2vec(self):
		#verify model and smilarity cannot be the same instead that similarity is calculated with cos similarity
		converter=list()

		job=''
		for k in self.job_description:
			job+=k+' '

		converter.append(job)

		for i in self.candidats:
			text=""
			for j in i:
				text+=j+' '
			converter.append(text)


		tagged_data =[TaggedDocument(words=word_tokenize(_d.lower()),
									tags=['cv'+str(i)]) for i,_d in enumerate(converter)]


		alpha=0.025
		max_epochs=50
		vec_size=50
		model = Doc2Vec(vec_size=vec_size,alpha=alpha,min_alpha=0.00025,min_count=1,dm=1)
		model.build_vocab(tagged_data)
		#model = Doc2Vec(self.get_all_cleaned_text(), vector_size=100, window=2, min_count=1, workers=4)
		for epoch in range(max_epochs):
			model.train(tagged_data,total_examples=model.corpus_count,epochs=model.iter)
			model.alpha -= 0.0002
			model.min_alpha=model.alpha


		print(model.docvecs.most_similar('cv0'))

		v1 = model.docvecs[0]
		"""		
		for i in range(0,20):
			v= model.docvecs[i]
			dist=np.linalg.norm(v1 - v)
			print(i,dist)
		"""
		data = []
		for i in range(len(model.docvecs)):
		    data.append(model.docvecs[i])

		#data.append(model.infer_vector(resume))
		group=[]
		for i in range(0,10):
			group.append(model.docvecs.most_similar('cv0')[i])
			print(model.docvecs.most_similar('cv0')[i])

		mds = MDS(n_components=2, random_state=1)
		pos = mds.fit_transform(data)
		#print pos
		xs,ys = pos[:,0], pos[:,1]
		for x, y in zip(xs, ys):
		    plt.scatter(x, y)
		#    plt.text(x, y, name)
		xs2,ys2 = xs[-1], ys[-1]
		plt.scatter(xs2, ys2, c='Red', marker='+')
		words = ['cv0','cv1','cv2','cv3','cv4','cv5','cv6','cv7','cv8','cv9','cv10','cv11','cv12','cv13','cv14','cv15','cv16']
		
		for i, word in enumerate(words):
			plt.annotate(word,xy=(pos[i,0],pos[i,1]))
		
		#plt.text(xs2,ys2,'resume')
		plt.show()



		return model,group
