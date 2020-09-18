from collect_resume import ResumeCollector
from text_processing import TextProcessing
from candidats import Candidats
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from job_description import JobDescription
from scoring_refer_to_skills import Scoring
from scoring import ScoringCVreferToJobDescription
from model import Model
from interface import Interface
import docx2txt
import sys

RS=ResumeCollector()
TextClean=TextProcessing()
dataset=Candidats()
data=RS.starting_collection_from_pdf()


datalength=RS.files_length()
print("This test is using ",datalength," files")


job_description=docx2txt.process(sys.argv[1])
cleanjob_description=TextClean.text_cleaning_from_stop_words_and_punctuation(job_description)

job=JobDescription(sys.argv[1],cleanjob_description)

documentlabel=[]
alldata=[]
filesnames_label=[]
for i in range(0,datalength):
	dataclean=TextClean.text_cleaning_from_stop_words_and_punctuation(data[i]['text'])
	candidat=dataset.add_new_candidat(data[i]['filename'],
							data[i]['resume']['name'],
							data[i]['resume']['email'],
							data[i]['resume']['mobile_number'],
							data[i]['resume']['degree'],
							data[i]['resume']['experience'],
							data[i]['resume']['skills'],
							data[i]['resume']['designation'],
							data[i]['resume']['total_experience'],
							data[i]['resume']['company_names'],
							dataclean,
							data[i]['text'],
							[])
	alldata.append(dataclean)
	filesnames_label.append(data[i]['filename'])
	job_description=docx2txt.process(sys.argv[1])

	text=[str(data[i]['text']),job_description]
	cv =CountVectorizer()
	count_matrix=cv.fit_transform(text)	
	percentage=cosine_similarity(count_matrix)[0][1] * 100
	result=round(percentage,2)
	elem={
	'filename':data[i]['filename'],
	'score':result
	}
	print(elem)

	documentlabel.append(elem)
	

	
model=Model(alldata,cleanjob_description)
#vectors=model.model_word2vec()
#dataset.set_vectors(vectors)

doc,group=model.model_doc2vec()

print(doc)
exit(0)
names_found=list()



#find out list elements
for i in group:
	print(filesnames_label[1][int(i[2:])-1])
	names_found.append(filesnames_label[int(i[2:])-1])

for i in documentlabel:
	if i['filename'] in names_found:
		print(i)

exit(0)
job.job_description_set_vector(vectors)

scoring=ScoringCVreferToJobDescription(dataset.get_vector(),job.get_vector())

res_files_names=[]
res_pourcentage_matching=[]
for i in doc:
	res_files_names.append(documentlabel[int(i[2:])-1]['filename'])
	res_pourcentage_matching.append(documentlabel[int(i[2:])-1]['score'])



for k in documentlabel:
	print(k)


interface=Interface(res_files_names,res_pourcentage_matching,dataset.get_candidats_by_filename(res_files_names))

