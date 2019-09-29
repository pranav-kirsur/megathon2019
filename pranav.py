import nltk

import re
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer


# TODO error handling for 0 sentence length
def number_of_superlatives(sentence):
    tokenized = word_tokenize(sentence)
    pos_tagged = nltk.pos_tag(tokenized)
    num = 0
    for i in pos_tagged:
        if i[1] == 'JJS' or i[1] == 'RBS':
            num += 1
    return num / len(sentence.split())


def has_number(input):
    res = bool(re.search(r'\d', input))
    if res:
        return 1
    return 0


def abbrevs_per_length(sentence):
    tokenized = word_tokenize(sentence)
    num = 0
    for i in tokenized:
        if re.match(r'^[A-Z\.]{2,}$',i):
            num+=1
    return num / len(sentence.split())

def nouns_per_length(sentence):
    tokenized = word_tokenize(sentence)
    pos_tagged = nltk.pos_tag(tokenized)
    num = 0
    for i in pos_tagged:
        if i[1] == 'NN' or i[1] == 'NNS' or i[1] == 'NNP' or i[1] == 'NNPS':
            num += 1
    return num / len(sentence.split())

def pronouns_per_length(sentence):
    tokenized = word_tokenize(sentence)
    pos_tagged = nltk.pos_tag(tokenized)
    num = 0
    for i in pos_tagged:
        if i[1] == 'PRP' or i[1] == 'PRP$':
            num += 1
    return num / len(sentence.split())


#Check special words

keywords = ["define"]
stemmed_keywords = []

stemmer = SnowballStemmer("english")

for i in keywords:
    stemmed_keywords.append(stemmer.stem(i))


def keyword_present(sentence):
    tokenized = word_tokenize(sentence)
    for token in tokenized:
        if stemmer.stem(token) in stemmed_keywords:
            return 1
    return 0




    

