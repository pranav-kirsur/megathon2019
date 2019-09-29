def discourse_connector(sentence):
    connectors = ['because of', 'despite the fact that', 'in spite of', 'however', 'nevertheless', 'despite', 'in addition to', 'although', 'since', 'therefore', 'due to', 'as a result of', 'and', 'but', 'consequently', 'in addition', 'additionally', 'furthermore', 'moreover', 'along with', 'as well as', 'because']

    count = 0
    for connector in connectors:
        if connector in sentence:
            count+=1
            sentence = sentence.replace(connector + " ", "")
            # print(sentence)
    return count/len(sentence.split())
