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


def generate_candidate_keys(noun_phrases):
    possible_keys=[]
    for phrase in noun_phrases:
        tokenized = word_tokenize(phrase)
        pos_tagged = nltk.pos_tag(tokenized)
        most_worthy = ""
        for i in pos_tagged:
            if i[1] == 'NN' or i[1] == 'NNS' or i[1]=='NNP' or i[1]=='NNPS':
                most_worthy = i[0]
                break
        for i in pos_tagged:
            if i[1] == 'JJ' or i[1] == 'JJR' or i[1]=='JJS':
                most_worthy = i[0]
                break
        for i in pos_tagged:
            if i[1] == 'CD':
                most_worthy = i[0]
                break
        possible_keys.append(most_worthy)
    return possible_keys

print(generate_candidate_keys(generate_key_list("The strongest kind of chemical bonds are covalent bond and ionic bond")))
        
