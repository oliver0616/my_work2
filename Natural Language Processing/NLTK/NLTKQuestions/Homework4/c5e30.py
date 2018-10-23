#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 3/14/2018
#Tabs: 8

import nltk
from nltk.corpus import brown

#setting up words and sentences
newsWord=brown.words(categories="news")
newsWithTag=brown.tagged_sents(categories="news")

#figure out low frequncey words
counts=nltk.FreqDist(newsWord)
lowFrequency=[]
for w in newsWord:
	if counts[w] == 1:
		lowFrequency.append(w)

#changing low frequncey words to UNK
newList=[]
newSentences=[]
for sentence in newsWithTag:
	for word,tag in sentence:
		if word in lowFrequency:
			newList.append(("UNK",tag))
		else:
			newList.append((word,tag))
	newSentences.append(newList)
	newList=[]

#training and evaluate
size=int(len(newSentences)*0.9)
train_sent=newSentences[:size]
test_sent=newSentences[size:]

bigram_tagger=nltk.BigramTagger(train_sent)
print("Bigram:"+str(bigram_tagger.evaluate(test_sent)*100)+"%")
#12.897438453104754

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sent, backoff=t0)
t2 = nltk.BigramTagger(train_sent, backoff=t1)
print("DefaultTagger & Unigram:"+str(t2.evaluate(test_sent)*100)+"%")
#85.20881092395096

#Using defaultTagger and unigramTagger increase the evaluate

