#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 3/14/2018
#Tabs: 8

import nltk
from nltk.corpus import brown

entireBrown=brown.tagged_words(tagset="universal")
cfd=nltk.ConditionalFreqDist(entireBrown)
c=cfd.conditions()
onePOS=[]
for word in c:
	if len(cfd[word])==1:
		onePOS.append(word)
proportion=len(onePOS)/len(c)
moreThanOne=len(c)-len(onePOS)
ambiguousPercentage=moreThanOne/len(c)

print("The porposion is "+str(proportion))
print("The words that are ambiguous are "+str(moreThanOne))
print(ambiguousPercentage)
