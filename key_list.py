import nltk
from nltk.tokenize import word_tokenize


def generate_key_list(sentence):
    tokenized = word_tokenize(sentence)
    pos_tagged = nltk.pos_tag(tokenized)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    noun_phrases_list = [' '.join(leaf[0] for leaf in tree.leaves())
                         for tree in cp.parse(pos_tagged).subtrees()
                         if tree.label() == 'NP']

    return noun_phrases_list

