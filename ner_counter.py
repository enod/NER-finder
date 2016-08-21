# -*- coding: utf-8 -*-

import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from textblob import TextBlob


st = StanfordNERTagger(
    './stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
    './stanford-ner/stanford-ner.jar',
    encoding='utf-8')

counting = {}

def ner_finder(text):  # todo-me 3gram, bigram, unigram loop
    Blob = TextBlob(text)
    Blob = Blob.replace(',', '')
    for sentence in Blob.sentences:
        sentence = sentence.replace(',', '')
        # fill sentences that is dividable by 3.
        delta = len(sentence) % 3
        sentence = sentence + " ." * delta
        print sentence

        tokenized_sent = word_tokenize(unicode(sentence))
        classified = st.tag(tokenized_sent)

        get = counting.get


        for x, y, z in zip(*[iter(classified)] * 3):


            if x[1] == 'PERSON' and y[1] == 'PERSON' and z[1] == 'PERSON': #  trigram
                counting[x[0]+' '+y[0]+' '+z[0]] = get(x[0]+' '+y[0]+' '+z[0], 0) + 1

            elif x[1] == 'PERSON' and y[1] == 'PERSON' :  # bigram
                counting[x[0] + ' ' + y[0]] = get(x[0] + ' ' + y[0], 0) + 1

            elif y[1] == 'PERSON' and z[1] == 'PERSON' :  # bigram
                counting[y[0] + ' ' + z[0]] = get(y[0] + ' ' + z[0], 0) + 1

            elif x[1] == 'PERSON':
                counting[x[0]] = get(x[0], 0) + 1

            elif y[1] == 'PERSON':
                counting[y[0]] = get(y[0], 0) + 1

            elif z[1] == 'PERSON':
                counting[z[0]] = get(z[0], 0) + 1

    return 'Result is - ', counting

# text = u'''Donald Trump never asked the chief executive of Apple for leadership advice and Barack Obama still Michelle Obama.
#
# Still, Tim Cook could certainly teach the Republican presidential nominee about the art of the apology, telling the Washington Post in an interview published over the weekend that it is important for a leader to admit mistakes and move on.'''
# print ner_finder(text)