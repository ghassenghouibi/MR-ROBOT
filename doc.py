from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from gensim.models import word2vec


data= ["I love machine learning it awesome",
	   "I love coding in python" ,
	   "I love building chatbots",
	   "They chat amagingly well",
	   "Moha la squale !!!!"]



tagged_data= [TaggedDocument(words=word_tokenize(_d.lower()),tags=[str(i)]) for i,_d in enumerate(data)]

max_epochs = 100
vec_size = 20
alpha = 0.025

model = word2vec.Word2Vec(tagged_data, size=300, window=20,
                          min_count=2, workers=1, iter=100)

print(model.corpus_count)
model = Doc2Vec(size=vec_size,alpha=alpha,min_alpha=0.00025,min_count=1,dm=1)

model.build_vocab(tagged_data)

print(model.wv.vocab)
exit(0)

for epoch in range(max_epochs):
	model.train(tagged_data,total_examples=model.corpus_count,epochs=model.iter)
	model.alpha -=0.0002
	model.min_alpha=model.alpha





model.save("d2v.model")
print("model saved !")