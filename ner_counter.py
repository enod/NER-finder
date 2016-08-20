# -*- coding: utf-8 -*-

from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from textblob import TextBlob


st = StanfordNERTagger(
    './stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
    './stanford-ner/stanford-ner.jar',
    encoding='utf-8')

counting = {}

def ner_finder(text):  # todo-me 3gram, bigram, unigram loop - make it faster
    Blob = TextBlob(text)
    for sentence in Blob.sentences:
        tokenized_sent = word_tokenize(unicode(sentence))
        classified = st.tag(tokenized_sent)
        for x, y, z in zip(classified, classified[1:], classified[2:]):
            if x[1] == 'PERSON' and y[1] == 'PERSON' and z[1] == 'PERSON': #  trigram
                # counting.append(x[0]+' '+y[0]+' '+z[0])

                if counting.get(x[0]+' '+y[0]+' '+z[0]):
                    counting[x[0] + ' ' + y[0] + ' ' + z[0]] += 1
                else:
                    counting[x[0] + ' ' + y[0] + ' ' + z[0]] = 1

            elif x[1] == 'PERSON' and y[1] == 'PERSON':  # bigram
                # counting.append(x[0] + ' ' + y[0])
                if counting.get(x[0] + ' ' + y[0]):
                    counting[x[0] + ' ' + y[0]] += 1
                else:
                    counting[x[0] + ' ' + y[0]] = 1

            elif x[1] == 'PERSON':
                # counting.append(x[0])
                if counting.get(x[0]):
                    counting[x[0]] += 1
                else:
                    counting[x[0]] = 1

    return counting
