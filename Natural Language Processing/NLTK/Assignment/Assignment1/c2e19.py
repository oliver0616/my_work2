#Course: CSCI 4140
#Name: Huan-Yun Chen
#Date: 1/29/2018
#Tabs: 8
#The following program is program in Python 3 and Python IDLE

#==========================================================
import nltk
from nltk.corpus import brown
#import matplotlib
#matplotlib.use('TKagg')
from nltk import FreqDist, ConditionalFreqDist
#==========================================================
result =[]
fd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ["news","reviews","religion","government","romance"]
newsList = ["crime","society","victim","safety"] #set of words for news
reviewsList =["good","wrong","right","correct"] #set of words for review
religionList =["god","believe","religion","heaven"]    #set of words for religion
governmentList =["security","society","politics","nuclear"]  #set of words for government
romanceList =["love","live","forever","life"] #set of words for romance

commonList=["could","would","can","do","does","should"]   #set of words that is more often use in life
commonList2=["he","she","it","they","we","you","I"]  #pronoun

print("News:")
fd.tabulate(conditions=genres, samples=newsList)
print("===================================================================")
print("Reviews:")
fd.tabulate(conditions=genres, samples=reviewsList)
print("===================================================================")
print("Religion:")
fd.tabulate(conditions=genres, samples=religionList)
print("===================================================================")
print("Govenment:")
fd.tabulate(conditions=genres, samples=governmentList)
print("===================================================================")
print("Romance:")
fd.tabulate(conditions=genres, samples=romanceList)
print("===================================================================")
print("Common:")
fd.tabulate(conditions=genres, samples=commonList)
print("===================================================================")
print("Pronoun:")
fd.tabulate(conditions=genres, samples=commonList2)
