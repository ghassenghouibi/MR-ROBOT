# importing required modules
import PyPDF2

pdfFileObject = open('./bank/CV-Imane ELIDRISSI-Consultante Cloud-Data.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
count = pdfReader.numPages
info=[]
for i in range(count):
    page = pdfReader.getPage(i)
    print(page.extractText())
    info.append(page.extractText())

print(info)