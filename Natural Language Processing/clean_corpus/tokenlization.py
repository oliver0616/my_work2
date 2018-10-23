import os
'''import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
'''
from string import printable
import string
import re

def main():
    path=os.getcwd()
    pathName=path+"\\inputFile\\"
    for inputFileName in os.listdir(pathName):
        file=open(pathName+inputFileName,'r')
        text=file.read()
        new_string = re.sub("[^{}]+".format(printable), "", text)
        new_string=new_string.replace('?','')
        #new_string=new_string.replace('\n','\\n')
        #new_string=new_string.replace('\t','')
        if "\t" in new_string:
            print("THERE IS A TAB")
        if new_string[:1] ==' ':
            new_string=new_string[1:]
        #print(new_string)
        
        outputFileName=path+"\\outputFile\\"+inputFileName
        outputFile=open(outputFileName,"w")
        outputFile.write(new_string)
        outputFile.close()
        

'''def main():
    path=os.getcwd()
    pathName=path+"\\inputFile\\"
    for inputFileName in os.listdir(pathName):
        file=open(pathName+inputFileName,'r')
        text =file.read()
        file.close()
        tokenlization(path,text,inputFileName)
        

    #split string by space lower all the cases(did not use nltk)
    
    words=text.split()
    
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]

    words=[word.lower() for word in stripped]
    print(words[:100])
    

    

def tokenlization(path,text,inputFileName):
    tokens = word_tokenize(text) 
    tokens = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words =[word for word in stripped if word.isalpha()]
    #stopWords
    #stop_words=set(stopwords.words('english'))
    #words = [w for w in words if not w in stop_words]
    final=' '.join(words)
    outputFileName=path+"\\outputFile\\"+inputFileName
    outputFile=open(outputFileName,"w")
    outputFile.write(final)
    outputFile.close()'''

    
main()
