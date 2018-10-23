#Name: Huan-Yun Chen
#Course: CSCI 4140
#Date: 2/27/2018
#Description: midterm exam question1

import nltk

#Question 1:
universalTag=nltk.corpus.brown.tagged_words(tagset="universal")
unsimplifiedTag=nltk.corpus.brown.tagged_words()
ADVSet=[]
resultSet=[]
noDuplicate =[]
totalNum=0

#Store ADV Set
ADVSet =[word for word,tag in universalTag if tag == "ADV"]
ADVSet = set(ADVSet)
#Find ADV in unsimplified Sets
resultSet =[tag for word,tag in unsimplifiedTag if word in ADVSet]
noDuplicate = set(resultSet)

print("There are "+str(len(noDuplicate))+" different tags that map to ADV")

#Question 2
fd = nltk.FreqDist(resultSet)
#Find the highest count in the Frequency Distribution
mostCom = fd.most_common()
name,occursMost =mostCom[0]
#Add the total counts for all the words
for char,num in mostCom:
	totalNum+=num
#Find the Percentage
percentage = occursMost/totalNum
percentage = percentage *100
print("The "+name+" tag occurs "+format(percentage,'.1f')+"% of the time")



