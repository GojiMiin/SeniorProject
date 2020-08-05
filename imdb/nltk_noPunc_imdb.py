import nltk, re, pprint
import json
import requests
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

url = "https://www.imdb.com/review/rw5318396/?ref_=tt_urv"
html = request.urlopen(url).read().decode('utf8')
html[:400]

raw = BeautifulSoup(html, 'html.parser')
data = json.loads(raw.find('script', type='application/ld+json').text)
review = data['reviewBody'].type

def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	return filtered_words#" ".join(filtered_words)

#token = preprocess(review)
print(review)

#print(json.load(script['reviewBody']))


#tokens = word_tokenize(raw)
#token = tokens[110:390]
