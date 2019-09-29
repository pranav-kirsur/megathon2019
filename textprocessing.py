#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re


# In[3]:


def subs(text,find,replace):
#     find='r'+''""''+find
    output=re.sub(find,replace,text)
    return output


# In[8]:


def getTextDict():
    with open('kech102.txt', 'r', encoding='utf8') as f:
        data = f.read()
        paras = list(data.split('\n\n'))
        para_filter1 = []
        for i in paras:
            if i == '' or i == ' ':
                pass
            else:
                para_filter1.append(i)
        title = para_filter1[0]
        para_filter2 = []
        for i in para_filter1:
            if not i.startswith('\nFig.') and not i.startswith('Fig.'):
                para_filter2.append(i)
        para_filter3 = []
        for i in para_filter2:
            sentence = subs(i,'\(i+\)', "")
            sentence = subs(sentence, '^[1-9]. | \n[1-9].', "\n")
            sentence = subs(sentence, '\[Fig.*?\]', " " )
            sentence = subs(sentence, '\(Fig.*?\)', " ")
            sentence = subs(sentence, 'Fig. [1-9].[1-9]', " ")
            sentence = subs(sentence, 'equations* [1-9].[1-9]', " ")
            sentence = subs(sentence, 'equations* \([1-9].[1-9]\)', " ")
            sentence = subs(sentence, 'equation \([1-9].[1-9]+\)', " ")
            para_filter3.append(sentence)
    #     print(para_filter3)

        para_list = []

        for paragraphs in para_filter3: 
            final_para = {}
            final_para['title'] = subs(title, "\n", " ").strip()
            final_para['text'] = []
            prelist = paragraphs.split('. ')
            for i in prelist:
                lol=i.split('.\n')
                for j in lol :
                    j = subs(j, '\n', " ")
                    j = subs(j, '\t', " ")
                    j = subs(j, '\s{1,}', " ")
                    j = j.strip()
                    if len(j) == 0:
                        pass
                    else:
                        final_para['text'].append(j)
            para_list.append(final_para)

    return para_list


# In[ ]:




