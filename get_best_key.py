import nltk
from nltk.tokenize import word_tokenize

def get_best_key(keys,sentence):
    tokenized = word_tokenize(sentence)
    pos_tagged = nltk.pos_tag(tokenized)
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)    
    t=cp.parse(pos_tagged)
    n_leaves = len(t.leaves())
    leavepos = set(t.leaf_treeposition(n) for n in range(n_leaves))
    mapping = {}
    for pos in t.treepositions():
        if pos not in leavepos:
            mapping[t[pos].label()] = len(pos)
    pairslist = []
    for i in keys:
        pairslist.append((mapping.get(i,10000),i))
      #  print(pairslist)
    pairslist.sort()
    return pairslist[0][1]


print(get_best_key(["Ligaments", "matrix", "little", "contain"],"Ligaments contain very little matrix"))
