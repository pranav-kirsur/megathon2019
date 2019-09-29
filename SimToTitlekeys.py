from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 


def SimToTitle(title,sentence):
    ps=PorterStemmer()
    titleArr = title.split()
    ansArr=[]
    for i in range(0,len(titleArr)):
        titleArr[i] = ps.stem(titleArr[i])
    sentenceArr=sentence.split()
    for i in range (0,len(sentenceArr)) :
        sentenceArr[i] = ps.stem(sentenceArr[i])
    common = set(titleArr).intersection(set(sentenceArr))
    keyAnsArr =[]
    for i in sentenceArr :
        if i in common :
            keyAnsArr.append(1)
        else :
            keyAnsArr.append(0)

#    print(keyAnsArr)
    return (keyAnsArr)

"""
k=SimToTitle("Jai murdered Ahish","Jai was busy sucking dicks")
print(k)
"""
