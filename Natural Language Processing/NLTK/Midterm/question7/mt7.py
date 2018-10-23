#Name: Huan-Yun Chen
#Course: CSCI 4140
#Date: 3/18/2018
#Description: midterm exam question7
'''
Output:
Sentence for"that"
CS
The Fulton County Grand Jury said Friday an investigation of Atlanta's recent primary election produced `` no evidence '' that any irregularities took place . 

DT
`` Actually , the abuse of the process may have constituted a contempt of the Criminal court of Cook county , altho vindication of the authority of that court is not the function of this court '' , said Karns , who is a City judge in East St. Louis sitting in Cook County court . 

WPS
Regarding Atlanta's new multi-million-dollar airport , the jury recommended `` that when the new management takes charge Jan. 1 the airport be operated in a manner that will eliminate political influences '' . 

WPO
He was able to smell a bargain -- and a masterpiece -- a continent away , and the Museum of Modern Art's Alfred Barr said of him : `` I have never mentioned a new artist that Thompson didn't know about '' . 

QL
While the city council suggested that the Legislative Council might perform the review , Mr. Notte said that instead he will take up the matter with Atty. Gen. J. Joseph Nugent to get `` the benefit of his views '' . 

DT-NC
He has his own system of shorthand , devised by abbreviations : `` humility '' will be `` humly '' , `` with '' will be `` w '' , and `` that '' will be `` tt '' . 

WPS-NC
In of all the suggestions that were made , his was the silliest the possessive his represents his suggestion and is stressed . 

WPS-HL
Factors that inhibit learning and lead to maladjustment 

CS-NC
But when to represents to consciousness in that was the moment that I came to , and similarly in that was the moment I came to , there is much stronger stress on to . 

WPO-NC
Thus to has light stress both in that was the conclusion that I came to and in that was the conclusion I came to . 

NIL
Thus , as a development program is being launched , commitments and obligations must be entered into in a given year which may exceed by twofold or threefold the expenditures to be made in that year . 

CS-HL
According to the official interpretation of the Charter , a member cannot be penalized by not having the right to vote in the General Assembly for nonpayment of financial obligations to the `` special '' United Nations' budgets , and of course cannot be expelled from the Organization ( which you suggested in your editorial ) , due to the fact that there is no provision in the Charter for expulsion .

total spend time: 19.02849769592285
'''

import nltk
from nltk.corpus import brown
import time

#get first item as key in the tuple
def getFirstKey(item):
	return item[0]
#get third item as key in the tuple
def getThirdKey(item):
	return item[2]

#generate the output
def outputGen(n,result):
	print("Sentence for\""+n+"\"")
	for eachTag in result:
		finalSentence=""
		name,tag,tagCount,sentence=eachTag
		print(tag)
		for eachWord in sentence:
			word,tag = eachWord
			finalSentence+=word+" "
		print(finalSentence)
		print()

#Look for sentences
def lookForSentence(wordTuple):
	allSent=brown.tagged_sents()
	name,count,tag,listOfTag=wordTuple
	result=[]
	# storing sentences into result
	for sentence in allSent:
		cfd=nltk.ConditionalFreqDist(sentence)
		c=cfd.conditions()
		#if there is only one tag in this sentence
		if name in c and len(cfd[name])==1 and list(cfd[name])[0] in tag:
			tagCount=[c for n,c in listOfTag if n == list(cfd[name])[0]][0]
			result.append((name,list(cfd[name])[0],tagCount,sentence))
			tag.remove(list(cfd[name])[0])
		#if there are more than one tag in this sentence
		elif name in c and len(cfd[name])>1:
			for t in list(cfd[name]):
				if t in tag:
					tagCount=[c for n,c in listOfTag if n == t][0]
					result.append((name,t,tagCount,sentence))
					tag.remove(t)
		#break loop
		if len(tag) ==0:
			break
	return result
		
#main
start=time.time()
allWord=brown.tagged_words()
cfd=nltk.ConditionalFreqDist(allWord)
c=cfd.conditions()
maxCount =0
maxCountWord=""
wordList=[]
#find mostDiverse word
for word in c:
	if len(cfd[word]) > maxCount:
		maxCount=len(cfd[word])
		maxCountWord=word
		listOfTag=[(t,cfd[word][t])for t in cfd[word]]
		wordList.append((word,len(cfd[word]),listOfTag))
#filter out all the word in the list for highest count, to see if there is more than one highest count
maxList = [(word,count,list(cfd[word]),listOfTag) for word,count,listOfTag in wordList if count == maxCount]
maxList.sort(key=getFirstKey)
for wordT in maxList:
	name,count,tag,listOfTag=wordT
	result=lookForSentence(wordT)
	result.sort(key=getThirdKey)
	result.reverse()
	outputGen(name,result)
end=time.time()
print("total spend time: "+str(end-start))

