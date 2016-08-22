# NER-finder

Finds all person names of a given webpage and counts it. Based on stanford NER analyzer. 

:Input: url
:Output: text(dict)

#### Supported language

Currently supports only english

#### Requirements

pip install -r requirements.txt

- nltk
- textblob
- stanford analyzer

#### Testing 

curl -H "Content-Type: application/json" -X POST -d '{"url":"http://www.huffingtonpost.com/entry/donald-trump-tim-cook_us_57b1f302e4b0718404121724?ir=Politics?utm_content=socialchampVkbWaYGitW&utm_medium=social&utm_source=plus.google.com&utm_campaign=socialchamp.io"}' localhost:5000

