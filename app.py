# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import urllib2
from bs4 import BeautifulSoup
from ner_counter import ner_finder
# from ner_counter import ner_finder_ch

app = Flask(__name__)

@app.route('/', methods=['POST'])  # todo-me Implement chinese NER counter.
def poster():
    url = request.json['url']
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page,"html.parser")

    for script in soup(["script", "style"]):
        script.extract()  # rip it out

    text = soup.get_text()

    # # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    # return ner_finder(text)
    return jsonify(ner_finder(text))


@app.route('/', methods=['GET'])
def getter():
    return jsonify({"message": 'It works!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
