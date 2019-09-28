import nltk
import re
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# TODO error handling for 0 sentence length
def number_of_superlatives(sentence):
    tokenized = word_tokenize(sentence)
    pos_tagged = nltk.pos_tag(tokenized)
    num = 0
    for i in pos_tagged:
        if i[1] == 'JJS' or i[1] == 'RBS':
            num += 1
    return num / len(sentence)



def has_number(input):
    res = bool(re.search(r'\d', input)) 
    if res:
        return 1
    return 0
