import PyPDF2
import itertools

outputFile = open("output.txt","w")
pdfFileObj = open("test.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageNum=pdfReader.numPages
counter =0

while counter < pageNum:
    pageObj = pdfReader.getPage(counter)
    t = pageObj.extractText()
    for b in t:
        print(b)
    #outputFile.write(t)
    #print(t)
    print("==================================================================")
    counter+=1
    
outputFile.close()

'''
pdfFileObj = open("test.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#pdfReader.numPages
pageObj = pdfReader.getPage(counter)
t = pageObj.extractText()
print(t)
'''
