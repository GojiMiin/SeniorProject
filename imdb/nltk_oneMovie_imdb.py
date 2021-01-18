import nltk
import re
import pprint
import json
import requests
import pandas as pd
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
	return filtered_words  # " ".join(filtered_words)


# get id
main_url = "https://www.imdb.com/title/tt5013056/reviews?ref_=tt_ql_3"
html = request.urlopen(main_url).read().decode('utf8')
html[:400]

raw = BeautifulSoup(html, 'html.parser')
data = raw.findAll('div', {'id': 'main'})
review_only = data[0].findAll(
    'div', {'class': 'lister-item mode-detail imdb-user-review collapsable'})
ids = []
for div in review_only:
     ID = div.get('data-review-id')
     if ID is not None:
        ids.append(ID)
# print(ids)
# get review

reviewsCSV = []

for eachid in ids:

	url = "https://www.imdb.com/review/"+eachid+"/?ref_=tt_urv"
	html = request.urlopen(url).read().decode('utf8')
	html[:400]

	raw = BeautifulSoup(html, 'html.parser')

	# print(raw)

	data = raw.find('script', type='application/ld+json')
    jsonTemp = json.loads(data.contents[0])
    review = jsonTemp['reviewBody']
    # print(review)

	reviewsCSV.append(review)

	print("*************************************************************************************************************")
	print(eachid)
	# print(token)
	print(review)
	
data = {'Full Review': reviewsCSV}
toFile = pd.DataFrame(data)
toFile.to_csv("./oneMovieReview.csv", index=False)
