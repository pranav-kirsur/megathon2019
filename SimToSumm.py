import nltk
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize 



def _create_frequency_table(text_string) -> dict:

    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text_string)
    ps = PorterStemmer()

    freqTable = dict()
    for word in words:
        word = ps.stem(word)
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    return freqTable







def _score_sentences(sentences, freqTable) -> dict:
    sentenceValue = dict()

    for sentence in sentences:
        word_count_in_sentence = (len(word_tokenize(sentence)))
        for wordValue in freqTable:
            if wordValue in sentence.lower():
                if sentence[0:len(sentence)] in sentenceValue:
                    sentenceValue[sentence[0:len(sentence)]] += freqTable[wordValue]
                else:
                    sentenceValue[sentence[0:len(sentence)]] = freqTable[wordValue]

        sentenceValue[sentence[0:len(sentence)]] = sentenceValue[sentence[0:len(sentence)]] // word_count_in_sentence

    return sentenceValue




def _find_average_score(sentenceValue) -> int:
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))

    return average




def SimToTitle(title,sentences):
    ps=PorterStemmer()
    titleArr = title.split()
    ansArr=[]
    for i in range(0,len(titleArr)):
        titleArr[i] = ps.stem(titleArr[i])
#    print(titleArr)
    for sentence in sentences :
        sentenceArr=sentence.split()
        for i in range (0,len(sentenceArr)) :
            sentenceArr[i] = ps.stem(sentenceArr[i])
        common = set(titleArr).intersection(set(sentenceArr))
        ansArr.append(len(common)/len(sentenceArr))
    return (ansArr)



def _find_average_score(sentenceValue) -> int:
    sumValues = 0
    for entry in sentenceValue:
        sumValues += sentenceValue[entry]

    # Average value of a sentence from original text
    average = int(sumValues / len(sentenceValue))

    return average


def _generate_summary(sentences, sentenceValue, threshold):
    sentence_count = 0
    summary = ''

    for sentence in sentences:
        if sentence[0:len(sentence)] in sentenceValue and sentenceValue[sentence[0:len(sentence)]] > (threshold):
            summary += " " + sentence
            sentence_count += 1

    return summary



def getSimtoSum(i, paragraph):
    l=_create_frequency_table(paragraph)
    # i = sent_tokenize(paragraph)
    scoredict = _score_sentences(i,l)
    threshold = _find_average_score(scoredict)
    summary = _generate_summary(i, scoredict, 1.5 * threshold)
    #print(scoredict.values()/len(scoredict.keys().split()))
    valsl=scoredict.values()
    keysl=scoredict.keys()
    finallist=[]
    keysarr=[]
    scorearr=[]
    for i in scoredict:
        keysarr.append(i)
    for i in scoredict:
        scorearr.append(scoredict[i])
    #print (keysarr)
    #print (scorearr)

    for i in range (0,len(keysarr)):
    #    print (keysarr[i])
        lent=len(keysarr[i].split())
    #    print (lent)
        finallist.append(scorearr[i]/lent)



    return finallist


print(getSimtoSum(['Hi how are', '\n', '', 'you'], 'Hi how are \n you' ))