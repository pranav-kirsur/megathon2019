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



paragraph="""A group of cells that are similar in structure and/or work together to achieve a particular function forms a tissue.
6.1	Are Plants and Animals Made of Same Types of Tissues?
Let us compare their structure and functions. Do plants and animals have the same structure? Do they both perform similar functions?
There are noticeable differences between the two. Plants are stationary or fixed – they don’t move. Since they have to be upright, they have a large quantity of supportive tissue. The supportive tissue generally has dead cells.
Animals on the other hand move around in search of food, mates and shelter. They consume more energy as compared to plants. Most of the tissues they contain are living.
Another difference between animals and plants is in the pattern of growth. The growth in plants is limited to certain regions, while this is not so in animals. There are some tissues in plants that divide throughout their life. These tissues are localised in certain regions. Based on the dividing capacity of the tissues, various plant tissues can be classified as growing or meristematic tissue and permanent tissue. Cell growth in animals is more uniform. So, there is no such demarcation of dividing and non-dividing regions in animals.
The structural organisation of organs and organ systems is far more specialised and localised in complex animals than even in very complex plants. This fundamental difference reflects the different modes of life pursued by these two major groups of organisms, particularly in their different feeding methods. Also, they are differently adapted for a sedentary existence on one hand (plants) and active locomotion on the other (animals), contributing to this difference in organ system design.
It is with reference to these complex animal and plant bodies that we will now talk about the concept of tissues in some detail.
"""


def getSimtoSum(paragraph):
    l=_create_frequency_table(paragraph)
    i=sent_tokenize(paragraph)
    print(type(i))
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

<<<<<<< HEAD


    return finallist


print(getSimtoSum(['Hi how are', '\n', '', 'you'], 'Hi how are \n you' ))
=======
    return (finallist)

print(getSimtoSum(paragraph))
>>>>>>> bhavyajeet
