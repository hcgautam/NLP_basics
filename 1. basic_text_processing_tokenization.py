# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 23:19:51 2025

@author: hcgau
"""

import nltk
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

from nltk.tokenize import word_tokenize

text="NLP is an exciting field in Artificial intellligence"

tokens=word_tokenize(text)

stop_words=set(stopwords.words('english'))
filtered_tokens=[word for word in tokens if word.lower() not in stop_words]

print("Original Text:", text)
print("Tokens:", tokens)
print("Filtered tokens:", filtered_tokens)

from nltk.tokenize import sent_tokenize
text="NLP is fun. I enjoy learning it!"
sentences=sent_tokenize(text)

print("Sentences:", sentences)

