# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 23:22:03 2025

@author: hcgau
"""
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')

stemmer=PorterStemmer()
lemmatizer=WordNetLemmatizer()

words=['running','flies','easily','fairly']

stemmed_words=[stemmer.stem(word) for word in words]

lemmatized_words=[lemmatizer.lemmatize(word, pos='v') for word in words]

print("stemmed Words:", stemmed_words)
print("Lemmatized Words:", lemmatized_words)