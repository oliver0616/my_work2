#imports
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree

#==============================================================================================
#ignore this block :)
''' 
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    #prev = None
    continuous_chunk = []
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
        elif current_chunk:
            named_entity = " ".join(current_chunk)
            if named_entity not in continuous_chunk:
                continuous_chunk.append(named_entity)
                current_chunk = []
            else:
                continue
    return continuous_chunk

 
def get_continuous_chunks(text):
    chunked = ne_chunk(pos_tag(word_tokenize(text)))
    current_chunk = []
    for i in chunked:
        if type(i) == Tree:
            current_chunk.append(" ".join([token for token, pos in i.leaves()]))
    return current_chunk'''
#================================================================================================
#Name Entity function is the same as the one I used in my program
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
#================================================================================================
def nameEntSpaceReplace(inputText):
    #tokenize the inputText
    tokens = word_tokenize(inputText)
    #Get the name entities
    nameTokens, otherTokens = nameEntity(tokens)
    #Loop through each Name Entities
    for eachName in nameTokens:
        #if they are in the sentence replace the orignial word in the sentence with the same word space replace with underline
        if eachName in inputText:
            outputText = inputText.replace(eachName,eachName.replace(" ","_"))
    return outputText
#================================================================================================
#main, start here
#Test sentences
my_sent = "WASHINGTON -- In the wake of a string of abuses by New York police officers in the 1990s, Loretta E. Lynch, the top federal prosecutor in Brooklyn, spoke forcefully about the pain of a broken trust that African-Americans felt and said the responsibility for repairing generations of miscommunication and mistrust fell to law enforcement."
my_sent2= "The cat went to the National Bank and deposit the money"

#Tracer
print(nameEntSpaceReplace(my_sent2))

