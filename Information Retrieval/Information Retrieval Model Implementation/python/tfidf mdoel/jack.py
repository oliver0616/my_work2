import nltk
from nltk.corpus import stopwords
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import numpy as np
import os
import time
from reuters_reader import rcv1
import ReutersParser

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
    #spaces are now replaces with _
    lowerNameTokens = [word.lower().replace(' ', '_') for word in nameTokens]    #i modified this to replace spaces in NE chnks with underscores
    #print(lowerNameTokens)
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
#
#                                                                                     Main
#
#=====================================================================================

pathToRcv1All = '/home/jovyan/work/Jack/rcv1-parsed/all-not-lower/'   #!!!!!!!!!!!! this is the input folder
pathToRcv1NEParsed = '/home/jovyan/work/Jack/rcv1-parsed/all-ne/' #!!!!!!!!!!!!! this is the output folder
print('starting')
print(pathToRcv1All)
i = 0
for doc in ReutersParser.rcv1Parser.parsedRcv1Reader(pathToRcv1All):
    filename = os.path.join(pathToRcv1NEParsed, doc['filename'])
    #print(filename)
    with open(filename, 'w+') as f:
        topics = ';'.join(doc['topics'])
        #print(topics)
        f.write(topics + '\n')
        countries = ';'.join(doc['countries'])
        f.write(countries + '\n')
        #print(countries)
        f.write(doc['byline'])
        #print(doc['byline'])


        #===============================================================================
        textNEL = indexingUni(doc['text'])
        textNE = ' '.join(textNEL)
        #===============================================================================


        #print(textNE)
        f.write(textNE)
        i += 1
        if(i % 100000 == 0):
            print('another 100,000 files processed.')