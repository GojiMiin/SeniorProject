import nltk, re, pprint
import json
import requests
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	return filtered_words#" ".join(filtered_words)

main_url = "https://www.rottentomatoes.com/m/the_invisible_man_2020/reviews?type=user"

""" <a class="audience-reviews__name" href="/user/id/978655616">
                                Lian R
	<p class="audience-reviews__review js-review-text clamp clamp-8 js-clamp">
                            </a> """

html = request.urlopen(main_url).read().decode('utf8')
html[:400]

raw = BeautifulSoup(html, 'html.parser')
data = raw.findAll('p',{'class':'audience-reviews__review js-review-text clamp clamp-8 js-clamp'})
#print(data)
for eachdata in data:
	print(eachdata.text)
	print("***************************************************")
