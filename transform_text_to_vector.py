from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from nltk.tokenize import word_tokenize
from gensim.models import word2vec


class TransformText2Vector:

	def tfidfTransformer(self,data):
		vectorizer = TfidfVectorizer(norm = False, smooth_idf = False)
		sentence_vectors = vectorizer.fit_transform(data)

		return sentence_vectors.toarray()[0]