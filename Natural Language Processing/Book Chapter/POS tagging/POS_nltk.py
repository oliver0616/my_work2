#Reference: NLTK online Textbook chapter 5 Categorizing and Tagging Words(https://www.nltk.org/book/ch05.html)
#All Tags in NLTK for english(https://stackoverflow.com/questions/1833252/java-stanford-nlp-part-of-speech-labels?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
#====================================================================================

import nltk
from nltk import word_tokenize
from nltk.corpus import brown

#=====================================================================================
#Basic Tagging Technique
#Using str2tuple() to tage: tag one by one, given term and tag together
tag_token = nltk.tag.str2tuple('test/NN')
print(type(tag_token))
print(tag_token)
#output:('test', 'NN')

#default tagger
default_tagger = nltk.DefaultTagger('NN')
example_text = "Default Tagger tagged everything as you given"
text_token = word_tokenize(example_text)
result= default_tagger.tag(text_token)
print(result)
#output: [('This', 'NN'), ('is', 'NN'), ('test', 'NN'), ('String', 'NN')]
#used to tagged unseen tokens

#=======================================================================================
#Automatic Tagging
brown_tag_sent=brown.tagged_sents(categories='adventure')
brown_sent=brown.sents(categories='adventure')

#POS-tagger is a build in tagger in nltk package, using prebuild tagger to tag
tokens = word_tokenize("Computing is the new mathematics and new stethoscope of the 21st century")
tagTokens=nltk.pos_tag(tokens)
print(tagTokens)
#output: [('Computing', 'NN'), ('is', 'VBZ'), ('the', 'DT'), ('new', 'JJ'), ('mathematics', 'NNS'), 
#         ('and', 'CC'), ('new', 'JJ'), ('stethoscope', 'NN'), ('of', 'IN'), ('the', 'DT'), ('21st', 'JJ'), 
#         ('century', 'NN')]
#output produce tuple that contain the word and the pos tag

#evaluate tagger with the prebuild tagger
eva=default_tagger.evaluate(brown_tag_sent)
print(eva)
#output: 0.11610567909780509

#Regular Expression Tagger
#reference 4.2
patterns = [
    (r'.*ing$', 'VBG'),               # gerunds
    (r'.*ed$', 'VBD'),                # simple past
    (r'.*es$', 'VBZ'),                # 3rd singular present
    (r'.*ould$', 'MD'),               # modals
    (r'.*\'s$', 'NN$'),               # possessive nouns
    (r'.*s$', 'NNS'),                 # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')                     # nouns (default)
]
regexp_tagger = nltk.RegexpTagger(patterns)
brown_reg_tagged=regexp_tagger.tag(brown_sent[3])
print(regexp_tagger.evaluate(brown_tag_sent))
#output: 0.19011565861959562

#Lookup Tagger
#tag words with most common use POS
#reference 4.3
fd = nltk.FreqDist(brown.words(categories='adventure'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='adventure'))
most_freq_words = fd.most_common(100)
likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
print(baseline_tagger.evaluate(brown_tag_sent))
#output: 0.5220357070750772

#====================================================================================
#Machine Learning Part Of Speech Tagging
#n-gram Tagging(bigram)
brownTagSent = brown.tagged_sents(categories ='news')
brownSent = brown.sents(categories ='news')
size = int(len(brownTagSent)*0.9)
train = brownTagSent[:size]
test = brownTagSent[size:]
bigram = nltk.BigramTagger(train)
bigram.tag(brownSent[2007])
print(bigram.evaluate(test))
#output: 0.10206319146815508
#n-gram tagger produce poorly to unseen data

#creating n-gram tagger (template nltk.ngrams)
n = 6
sixgrams = nltk.ngrams(train,n)
#need to write evaluate function
#reference: https://stackoverflow.com/questions/17531684/n-grams-in-python-four-five-six-grams?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

#combine n-gram Tagging (using backoff)
tagger0 = nltk.DefaultTagger('NN')
tagger1 = nltk.UnigramTagger(train, backoff=tagger0)
tagger2 = nltk.BigramTagger(train, backoff=tagger1)
print(tagger2.evaluate(test))
#output: 0.8452108043456593
#the reslut improve dramatically after combine the n-gram taggers

#Given Features feed into decision tree for model to train
#https://www.nltk.org/book/ch06.html (1.4 part of speech tagging)

suffix_fdist = nltk.FreqDist()
for word in brown.words():
    word = word.lower()
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1

common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
    return features
tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n),g) for (n,g) in tagged_words]
size = int(len(featuresets)*0.1)
train_set,test_set=featuresets[size:],featuresets[:size]
classifier = nltk.DecisionTreeClassifier.train(train_set)
print(nltk.classify.accuracy(classifier,test_set))
#output:0.6270512182993535
classifier.classify(pos_features('cat'))



