#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 3/14/2018
#Tabs: 8

import nltk
from nltk.corpus import brown

#find the percentage of the pass in word
def percentage(word,fdTotalWords,cfdTags):
	wordTotalCount=fdTotalWords[word]
	mostCommonWordTags=[count for tag,count in cfdTags[word].most_common(5)]
	mostCommonWordTagCount=mostCommonWordTags[0]
	resultPercentage= int(mostCommonWordTagCount/wordTotalCount*100)
	return resultPercentage

fdTotalWords = nltk.FreqDist(brown.words(categories='news'))
cfdTags = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
newsWords=brown.words(categories='news')
percentageList=[]
for word in newsWords:
	wordPercentage=percentage(word,fdTotalWords,cfdTags)
	percentageList.append(wordPercentage)
print("Highest Percentage is "+str(max(percentageList))+"%")


