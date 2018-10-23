import nltk
from nltk.corpus import stopwords
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import numpy as np
import os
import time
#=====================================================================================

def nameEntity(text):
    chunked = ne_chunk(pos_tag(text))
    name_entities_chunk = []
    regular_chunk = []
    for i in chunked:
        if type(i) == Tree:
            name_entities_chunk.append(" ".join([token for token, pos in i.leaves()]))
        else:
            name,pos = i
            regular_chunk.append(name)
    return (name_entities_chunk,regular_chunk)
#=====================================================================================

def indexingUni(inputString):
    #normalization
    #tokenize
    tokens = nltk.word_tokenize(inputString)
    #extract name entities and combine with rest of the tokens
    nameTokens, normalTokens = nameEntity(tokens)
    #lower case all the words
    lowerTokens = [word.lower() for word in normalTokens]
    lowerNameTokens = [word.lower() for word in nameTokens]
    #remove punctuation
    stripped = [word for word in lowerTokens if word.isalpha()]
    #remove stop words
    stop_words = set(stopwords.words('english'))
    words = [w for w in stripped if not w in stop_words]
    #combine name entities and tokens
    words = words + lowerNameTokens
    return words
    #stem words(ignore)
#=====================================================================================

def searchUni(uniWords):
    fd = nltk.FreqDist(uniWords)
    top = fd.most_common(20)
    return top
#=====================================================================================

def indexingBi(inputString):
    final =[]
    finalNameTokens=[]
    #normalization
    #sentences segmentation
    sentences = nltk.sent_tokenize(inputString)
    for sentence in sentences:
        #tokenize the sentence into tokens
        tokens = nltk.word_tokenize(sentence)
        #extract name entities and combine with rest of the tokens
        nameTokens, normalTokens = nameEntity(tokens)
        #lower case all words
        lowerTokens = [word.lower()for word in normalTokens]
        lowerNameTokens = [word.lower() for word in nameTokens]
        #remove punctuation
        stripped = [word for word in lowerTokens if word.isalpha()]
        #remove stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in stripped if not w in stop_words]
        #stem word ignore
        #create bigrams 
        bigram = nltk.bigrams(words)
        listBigram = list(bigram)
        tupleName = [(w,"") for w in lowerNameTokens]
        if len(listBigram) ==0:
            finalNameTokens=finalNameTokens+tupleName
            continue
        else:
            final.append(listBigram)
            finalNameTokens=finalNameTokens+tupleName
    final.append(finalNameTokens)
    return final
#=====================================================================================

def searchBi(searchSent):
    organize=[]
    for sentence in searchSent:
        for first, second in sentence:
            organize.append((first,second))
    fd = nltk.FreqDist(organize)
    top = fd.most_common(20)
    return top
#=====================================================================================

def getAllWords(inputPath,userInput):
    words = []
    #loop through files
    for f in os.listdir(inputPath):
        inputFileName = os.path.join(inputPath,f)
        inputFile=open(inputFileName,"r")
        inputString = inputFile.read()
        inputString = inputString.replace("\n"," ")
        #add all tokenize words
        if userInput == "3" or userInput == "5":
            words = words+ indexingUni(inputString)
        elif userInput == "4" or userInput == "6":
            bi = indexingBi(inputString)
            #deconsturct sentence structure
            for each in bi:
                words = words+ each
        print("File "+f+" word has extracted")

    result = set(words)
    return result
#=====================================================================================

def constructDict(allWords,indexeDict,docNum, inputPath, userInput):
    #initialize numpy array
    word_idf_dict = np.zeros(len(allWords))
    #loop through files and add one when word occur
    for f in os.listdir(inputPath):
        inputFileName = os.path.join(inputPath,f)
        inputFile=open(inputFileName,"r")
        inputString = inputFile.read()
        inputString = inputString.replace("\n"," ")
        words = []
        #find the word's index and add one
        if userInput == "3" or userInput == "5":
            words = set(indexingUni(inputString))
            indexes = [indexDict[word] for word in words]
            word_idf_dict[indexes] += 1.0
        elif userInput == "4" or userInput == "6":
            bi = indexingBi(inputString)
            for each in bi:
                words = words+ each
            indexes = [indexDict[word] for word in words]
            word_idf_dict[indexes] += 1.0
    #idf
    word_idf_dict = np.log(1+(docNum / (word_idf_dict).astype(float)))
    return word_idf_dict

#=====================================================================================

def tfidf(idfDict,indexDict, inputWords):
    result=[]
    #tf
    fd = nltk.FreqDist(inputWords)
    fdList = list(fd)
    
    #idf
    for each in fdList:
        idf = idfDict[indexDict[each]]
        tf = fd[each]
        tfidfVal = tf*idf
        result.append((each, tfidfVal))
    return result
#=====================================================================================

def freqDict(allWords,indexeDict, inputPath, userInput):
    #initialize numpy array
    collectionFreq = np.zeros(len(allWords))
    #loop through files and add one when word occur
    for f in os.listdir(inputPath):
        inputFileName = os.path.join(inputPath,f)
        inputFile=open(inputFileName,"r")
        inputString = inputFile.read()
        inputString = inputString.replace("\n"," ")
        words = []
        #find the word's index and add one
        if userInput == "5":
            all_words = indexingUni(inputString)
            freq_dist_words = nltk.FreqDist(all_words)
            words =set(all_words)
            indexes = [indexDict[word] for word in words]
            counts = [freq_dist_words[word] for word in words]
            collectionFreq[indexes] += counts
        elif userInput == "6":
            bi = indexingBi(inputString)
            for each in bi:
                all_words = words+ each
            freq_dist_words = nltk.FreqDist(all_words)
            words =set(all_words)
            indexes = [indexDict[word] for word in words]
            counts = [freq_dist_words[word] for word in words]
            collectionFreq[indexes] += counts
    return collectionFreq
#=====================================================================================

def cftfidf(tfidfDict,collectionFreqDict, indexDict, inputWords):
    alpha = 0.3
    uniqueWord = set(inputWords)
    result = []
    for each in uniqueWord:
        tfidfValue = tfidfDict[each]
        cfValue= collectionFreqDict[indexDict[each]]
        cftfidfValue= (alpha*tfidfValue) + 1 - (alpha*cfValue)
        result.append((each, cftfidfValue))
    return result
#=====================================================================================

def getKey(item):
    return item[1] 
#=====================================================================================
#choice operation
userInput=input("TF-Unigram: 1, TF-Bigram: 2, TF-IDF-Unigram: 3, TF-IDF-Bigram: 4, Collection Frequnecy Unigram: 5, Collection Frequnecy Bigram: 6")
cwd = os.getcwd()
#inputPath = os.path.join(cwd,"input")

# user input name here
inputPath = "C:\\Users\\olive\\Documents\\_School Works_\\_Research_\\2018 Summer\\Information Retrieval\\python\\Language Model\\New folder"
tfOutputPath = os.path.join(cwd,"output","tf")
tfidfOutputPath = os.path.join(cwd,"output","tfidf")
cftfidfOutputPath = os.path.join(cwd,"output","cf-tfidf")

if userInput == "3" or userInput == "4":
    #Get all the words, document counts, and word indexes
    x = time.time()
    allWords = getAllWords(inputPath, userInput)
    y = time.time()
    z = y - x
    print("Get All Words Time: "+str(z))
    docNum = len(os.listdir(inputPath))
    indexDict = {w: idx for idx, w in enumerate(allWords)}
    #construct idf dictionary
    a = time.time()
    idfDict = constructDict(allWords, indexDict, docNum, inputPath,userInput)
    b = time.time()
    c = b - a
    print("Done constructDict")
    print("ConstructDict Time: ",c)
elif userInput == "5" or userInput == "6":
    #Get all the words, document counts, and word indexes
    x = time.time()
    allWords = getAllWords(inputPath, userInput)
    y = time.time()
    z = y - x
    print("Get All Words Time: "+str(z))
    docNum = len(os.listdir(inputPath))
    indexDict = {w: idx for idx, w in enumerate(allWords)}
    #construct idf dictionary and collectionFreq dictionary
    a = time.time()
    idfDict = constructDict(allWords, indexDict, docNum, inputPath,userInput)
    b = time.time()
    c = b - a
    print("Done constructDict")
    print("ConstructDict Time: ",c)
    d = time.time()
    collectionFreqDict = freqDict(allWords, indexDict, inputPath,userInput)
    e = time.time()
    f = e - d
    print("Done collectionFreqDict")
    print("ConstructDict Time: ",f)

#calculations(tf,tf-idf)
for f in os.listdir(inputPath):
    inputFileName = os.path.join(inputPath,f)
    inputFile=open(inputFileName,"r")
    inputString = inputFile.read()
    inputString = inputString.replace("\n"," ")
    #TF
    if userInput=="1":
        #unigram
        uniWords = indexingUni(inputString)
        top = searchUni(uniWords)
        
    elif userInput == "2":
        #bigram
        biWords = indexingBi(inputString)
        top = searchBi(biWords)
    #TF-IDF
    elif userInput == "3":
        #unigram
        uniWords = indexingUni(inputString)
        tfidfList= tfidf(idfDict, indexDict, uniWords)
        tfidfList.sort(key=getKey, reverse= True)
    elif userInput == "4":
        #bigram
        words=[]
        biWords = indexingBi(inputString)
        for each in biWords:
            words = words+ each
        tfidfList= tfidf(idfDict, indexDict, words)
        tfidfList.sort(key=getKey, reverse= True)
    elif userInput == "5":
        #unigram
        uniWords = indexingUni(inputString)
        tfidfList= tfidf(idfDict, indexDict, uniWords)
        tfidfDict = dict((wo,i) for wo,i in tfidfList)
        cftfidfList= cftfidf(tfidfDict,collectionFreqDict, indexDict, uniWords)
        cftfidfList.sort(key=getKey, reverse= True)
    elif userInput == "6":
        #bigram
        words = []
        biWords = indexingBi(inputString)
        for each in biWords:
            words = words + each
        tfidfList= tfidf(idfDict, indexDict, words)
        tfidfDict = dict((wo,i) for wo,i in tfidfList)
        cftfidfList= cftfidf(tfidfDict,collectionFreqDict, indexDict, words)
        cftfidfList.sort(key=getKey, reverse= True)
    
    #Writeing output files
    #TF
    if userInput == "1" or userInput == "2":
        tfOutputFileName = os.path.join(tfOutputPath,f)
        tfOutputFile=open(tfOutputFileName,"w")
        tfOutputFile.write('%-30s %s\n' %("Word","Count"))
        tfOutputFile.write("-----------------------------------\n")
        for word, count in top:
            tfOutputFile.write('%-30s %s\n' %(word,count))
        tfOutputFile.close()
    #TF-IDF
    elif userInput == "3" or userInput == "4":
        tfidfOutputFileName = os.path.join(tfidfOutputPath,f)
        tfidfOutputFile = open(tfidfOutputFileName,"w")
        tfidfOutputFile.write('%-30s %s\n' %("Word","TF-IDF"))
        tfidfOutputFile.write("-----------------------------------\n")
        for word, count in tfidfList[:20]:
            tfidfOutputFile.write('%-30s %s\n' %(word,count))
        tfidfOutputFile.close()
    #CF TF-IDF
    elif userInput == "5" or userInput == "6":
        cftfidfOutputFileName = os.path.join(cftfidfOutputPath,f)
        cftfidfOutputFile = open(cftfidfOutputFileName,"w")
        cftfidfOutputFile.write('%-30s %s\n' %("Word","CF TF-IDF"))
        cftfidfOutputFile.write("-----------------------------------\n")
        for word, count in cftfidfList[:20]:
            cftfidfOutputFile.write('%-30s %s\n' %(word,count))
        cftfidfOutputFile.close()
    #tracer
    print("File " + f +" is done")

    
