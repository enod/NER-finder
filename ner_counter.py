# -*- coding: utf-8 -*-

import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from textblob import TextBlob

from itertools import groupby
from operator import itemgetter
from collections import Counter

st = StanfordNERTagger(
    './stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
    './stanford-ner/stanford-ner.jar',
    encoding='utf-8')

Names = []


def ner_finder(text):
    Blob = TextBlob(text)
    for sentence in Blob.sentences:
        counting = {}
        tokenized_sent = word_tokenize(unicode(sentence))
        classified = st.tag(tokenized_sent)

        for idx, val in enumerate(classified):
            if val[1] == 'PERSON':
                counting[idx] = val

        keys = sorted(counting.keys())

        for k, g in groupby(enumerate(keys), lambda d: d[0] - d[1]):
            ids = map(itemgetter(1), g)  # [0, 1, 2], [14, 15], etc.
            person = ' '.join(counting[i][0] for i in ids)  # Donald John Trump, Barack Obama, etc
            Names.append(person)
        print Names
    return Counter(Names)


# text = u'''Donald John Trump never asked Donald John Trump the chief executive of Apple for leadership advice and Barack Obama, Michelle Obama.
# Still, Tim Cook and Donald John Trump could certainly teach the Republican presidential nominee about the art of the apology, telling the Washington Post in an interview published over the weekend that it is important for a leader to admit mistakes and move on.'''
#
# print ner_finder(text)
