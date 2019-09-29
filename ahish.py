#!/usr/bin/env python
# coding: utf-8

# In[37]:


# import tensorflow
import numpy
import nltk 
# nltk.download()
import string
from sklearn.feature_extraction.text import TfidfVectorizer

import warnings
warnings.filterwarnings("ignore")

nltk.download('punkt')


# In[38]:


def stem_tokens(tokens):
    
    stemmer = nltk.stem.porter.PorterStemmer() #loads the stemmer
    return [stemmer.stem(item) for item in tokens]


# In[39]:


def normalize(text):
    
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation) #generates dict of punctuations to remove
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


# In[40]:


def cosine_sim(text1, text2):
    vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]


# In[41]:


# In[47]:


def getCosSims(listofstrings):
    # listofstrings = text.split('.')
    cosineSimilarities = [0 for i in range(len(listofstrings))]

    for i in range(len(listofstrings)):

        currSentence = listofstrings[i]
        for j in range(len(listofstrings)):

            if i == j:
                continue

            cosineSimilarities[i] += cosine_sim(currSentence, listofstrings[j])

        if len(listofstrings):
            cosineSimilarities[i] /= (len(listofstrings))
            
    return cosineSimilarities
        
        


# In[ ]:




