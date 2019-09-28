def SimToTitle(title,sentences):
    titleArr = title.split()
    for sentence in sentences :
        sentenceArr=sentence.split()
        common = set(titleArr).intersection(set(sentenceArr))
#        print(common)
        return (len(common)/len)


SimToTitle("Jai Murdered Ahish",["Jai was busy sucking dicks","Ahish started making jokes","Pranav laughed at the Murdered Ahish"])
