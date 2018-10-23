import nltk
#import codecs
from nltk.tokenize import PunktSentenceTokenizer,sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer

#normalization
def simpleFilter(sentence):
    filtered_sent = []
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)
    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(w))
    return filtered_sent

#use wup_similarity to calculate the score of how close the meaning of two words is
def simlilarityCheck(word1, word2):
    word1 = word1 + ".n.01"
    word2 = word2 + ".n.01"
    try:
        w1 = wordnet.synset(word1)
        w2 = wordnet.synset(word2)
        return w1.wup_similarity(w2)
    except:
        return 0

#Store syn of the word into a list
def synonymsCreator(word):
	synonyms = []
	for syn in wordnet.synsets(word):
		for i in syn.lemmas():
			synonyms.append(i.name())
	return synonyms

# Remove Stop Words . Word Stemming . Return new tokenised list.
def filteredSentence(sentence):
    filtered_sent = []
    lemmatizer = WordNetLemmatizer()   #lemmatizes the words
    ps = PorterStemmer()    #stemmer stems the root of the word.
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(sentence)
    for w in words:
        if w not in stop_words:
            filtered_sent.append(lemmatizer.lemmatize(ps.stem(w)))
            for i in synonymsCreator(w):
                filtered_sent.append(i)

    return filtered_sent

#Main
cricfile = open("cricketbat.txt", 'r')
sent2 = cricfile.read().lower()
vampirefile = open("vampirebat.txt", 'r')
sent1 = vampirefile.read().lower()
sent3 = "start"
# FOR TEST , replace the above variables with below sent1 and sent 2
# sent1 = "the commercial banks are used for finance. all the financial matters are managed by financial banks and they have lots of money, user accounts like salary account and savings account, current account. money can also be withdrawn from this bank."
# sent2 = "the river bank has water in it and it has fishes trees . lots of water is stored in the banks. boats float in it and animals come and drink water from it."
# sent3 = "from which bank should i withdraw money"
while(sent3 != "end"):
    sent3 = input("Enter Query: ").lower()
    #Calculate word rank
    filtered_sent1 = []
    filtered_sent2 = []
    filtered_sent3 = []
    counter1 = 0
    counter2 = 0
    sent31_similarity = 0
    sent32_similarity = 0
    filtered_sent1 = simpleFilter(sent1)
    filtered_sent2 = simpleFilter(sent2)
    filtered_sent3 = simpleFilter(sent3)
    for i in filtered_sent3:
        for j in filtered_sent1:
            counter1 = counter1 + 1
            sent31_similarity = sent31_similarity + simlilarityCheck(i,j)
        for j in filtered_sent2:
            counter2 = counter2 + 1
            sent32_similarity = sent32_similarity + simlilarityCheck(i,j)

    #Calculate word appearences
    filtered_sent1 = []
    filtered_sent2 = []
    filtered_sent3 = []
    filtered_sent1 = filteredSentence(sent1)
    filtered_sent2 = filteredSentence(sent2)
    filtered_sent3 = filteredSentence(sent3)
    sent1_count = 0
    sent2_count = 0
    for i in filtered_sent3:
        for j in filtered_sent1:
            if(i==j):
                sent1_count = sent1_count + 1
        for j in filtered_sent2:
            if(i==j):
                sent2_count = sent2_count + 1
    if((sent1_count + sent31_similarity)>(sent2_count+sent32_similarity)):
        print("Mammal Bat")
    else:
        print("Cricket Bat")
		#-----------------------------------------------
		#Sentence1: the river bank has water in it and it has fishes trees . lots of water is stored in the banks. boats float in it and animals come and drink water from it.
		#sentence2: the commercial banks are used for finance. all the financial matters are managed by financial banks and they have lots of money, user accounts like salary account and savings account, current account. money can also be withdrawn from this bank.
		#query: from which bank should i withdraw money.

		#sen1: any of various nocturnal flying mammals of the order Chiroptera, having membranous wings that extend from the forelimbs to the hind limbs or tail and anatomical adaptations for echolocation, by which they navigate and hunt prey.
		#sen 2: a cricket wooden bat is used for playing criket. it is rectangular in shape and has handle and is made of wood or plastic and is used by cricket players.
    print("\nTERMINATED")

