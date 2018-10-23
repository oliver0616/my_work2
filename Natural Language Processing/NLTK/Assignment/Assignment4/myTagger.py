#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 3/26/2018
#Tabs: 8

'''
Results by Sentences non-random data
Test Fold 	 Result
0 	 	 88.8
1 	 	 89.8
2 	 	 90.0
3 	 	 91.6
4 	 	 90.4
5 	 	 90.9
6 	 	 91.0
7 	 	 91.5
8 	 	 91.0
9 	 	 91.3
Results by Sentences random data
Test Fold 	 Result
0 	 	 92.4
1 	 	 92.5
2 	 	 92.3
3 	 	 92.3
4 	 	 92.4
5 	 	 92.3
6 	 	 92.2
7 	 	 92.4
8 	 	 92.2
9 	 	 92.3
Results by FileId non-random data
Test Fold 	 Result
0 	 	 88.6
1 	 	 90.1
2 	 	 89.7
3 	 	 91.2
4 	 	 91.4
5 	 	 90.4
6 	 	 91.0
7 	 	 90.9
8 	 	 91.1
9 	 	 91.2
Results by FileId random data
Test Fold 	 Result
0 	 	 91.4
1 	 	 91.1
2 	 	 91.1
3 	 	 90.9
4 	 	 90.7
5 	 	 90.6
6 	 	 90.6
7 	 	 90.5
8 	 	 91.0
9 	 	 90.8
total spend time: 976.1036176681519
'''

import nltk
from nltk.corpus import brown
import random
import time

#cut brown sentents into 10 equal size folds(For tageed sentences)
def produceFoldsSent(inputSent):
	s=0.1
	testSets=[]
	previous=0
	for count in range(0,10):
		now = int(len(inputSent)*s)
		testSet=inputSent[previous:now]
		setRange=(previous,now)
		testSets.append((testSet,setRange))
		previous=now
		s=round(s+0.1,2)
   
	return testSets
#===============================================================================
#get specific file's id and cut brown sentents into 10 equal size folds(For fileId)
def produceFoldsFile(inputFiles):
	s=0.1
	testSets=[]
	previous=0
	for count in range(0,10):
		now = int(len(inputFiles)*s)
		testSetLen=inputFiles[previous:now]
		testSet=brown.tagged_sents(fileids=testSetLen)
		trainSetLen=inputFiles[:previous]+inputFiles[now:]
		trainSet=brown.tagged_sents(fileids=trainSetLen)
		testSets.append((testSet,trainSet))
		previous=now
		s=round(s+0.1,2)
   
	return testSets
#===============================================================================
#find the train set and do the evaluate percentage(For tagged sentences)
def findPercentageSent(test,allB):
	result=[]
	counter=0
	for each in test:
		testSet,setRange = each
		start,end = setRange
		trainSet =allB[:start]+allB[end:]
		t0 = nltk.DefaultTagger('NN')
		t1 = nltk.UnigramTagger(trainSet, backoff=t0)
		t2 = nltk.BigramTagger(trainSet, backoff=t1)
		percentage=t2.evaluate(testSet)
		result.append((counter,percentage))
		counter+=1
		print(str(counter)+" fold has finished")		
	print("The program has completed current set of folds")
	return(result)
#===============================================================================
#evaluate the percentage(For fileid)
def findPercentageFile(test):
	result=[]
	counter=0
	for each in test:
		testSet,trainSet = each
		t0 = nltk.DefaultTagger('NN')
		t1 = nltk.UnigramTagger(trainSet, backoff=t0)
		t2 = nltk.BigramTagger(trainSet, backoff=t1)
		percentage=t2.evaluate(testSet)
		result.append((counter,percentage))
		counter+=1
		print(str(counter)+" fold has finished")		
	print("The program has completed current set of folds")
	return(result)
#===============================================================================
#print output table
def printTable(inputData,title):
	print(title)
	print("Test Fold","\t","Result")
	for each in inputData:
		number, percentage=each
		percentage=percentage*100
		percentage=round(percentage,1)
		print(number,"\t","\t",percentage)
#===============================================================================
#main
start=time.time()
brownSents = brown.tagged_sents()
randomBrownSents = random.sample(list(brownSents),len(brownSents))
brownFiles = brown.fileids()
randomBrownFiles = random.sample(list(brownFiles),len(brownFiles))

regTestSets=produceFoldsSent(brownSents)    #regular sets without randomize
randomTestSets=produceFoldsSent(randomBrownSents)   #set with randomize brown sentences
regFileFolds=produceFoldsFile(brownFiles)    #regular sets without randomize
randomFileFolds=produceFoldsFile(randomBrownFiles)   #set with randomize files

regPercentage=findPercentageSent(regTestSets, brownSents)
randomPercentage=findPercentageSent(randomTestSets, randomBrownSents)
regFilePercentage=findPercentageFile(regFileFolds)
randomFilePercentage=findPercentageFile(randomFileFolds)

printTable(regPercentage,"Results by Sentences non-random data")
printTable(randomPercentage,"Results by Sentences random data")
printTable(regFilePercentage,"Results by FileId non-random data")
printTable(randomFilePercentage,"Results by FileId random data")
end=time.time()
print("total spend time: "+str(end-start))



