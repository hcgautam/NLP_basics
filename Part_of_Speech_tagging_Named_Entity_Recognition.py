# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 23:40:22 2025

@author: hcgau
"""

import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('averaged_perceptron_tagger')

sentence="NLP helps machines understand human language."
tokens=word_tokenize(sentence)
pos_tags=nltk.pos_tag(tokens)

print("POS tags:", pos_tags)

import spacy

nlp=spacy.load('en_core_web_sm')

text="Elon musk founded Spacex and Tesla."

doc=nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)