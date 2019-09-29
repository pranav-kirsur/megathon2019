from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 


def SimToTitle(title,sentences):
    ps=PorterStemmer()
    titleArr = title.split()
    ansArr=[]
    for i in range(0,len(titleArr)):
        titleArr[i] = ps.stem(titleArr[i])
#    print(titleArr)
    for sentence in sentences :
        if len(sentence) == 0:
            ansArr.append(0)
            pass
        else:
            sentenceArr=sentence.split()
            for i in range (0,len(sentenceArr)) :
                sentenceArr[i] = ps.stem(sentenceArr[i])
            common = set(titleArr).intersection(set(sentenceArr))
            ansArr.append(len(common)/len(sentenceArr))
    return (ansArr)

"""
k=SimToTitle("Jai murdered Ahish",["Jai was busy sucking dicks","Ahish started making jokes","Pranav laughed at the murdered Ahish"])
print(k)
"""
