import docx2txt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import textract
import sys
from os      import listdir
from os.path import isfile, join


mypath='./db/bank/test2'
allfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
data=[]


files_names=[]
classement=[]

for i in range(0,len(allfiles)):
	resume=docx2txt.process(mypath+"/"+allfiles[i])
	job_description=docx2txt.process(sys.argv[1])
	text=[resume,job_description]
	cv =CountVectorizer()
	count_matrix=cv.fit_transform(text)
	percentage=cosine_similarity(count_matrix)[0][1] * 100
	result=round(percentage,2)
	print("This CV ",allfiles[i],"is Matching : ",result,"%")
	classement.append(result)
	files_names.append(allfiles[i])


while len(files_names)>10:
	value=classement.index(min(classement))
	classement.remove(classement[value])
	files_names.remove(files_names[value])

print("\n\n TOP 10 CV \n\n")

for i in range(0,10):
	print(files_names[i],"match with ",classement[i],"%")