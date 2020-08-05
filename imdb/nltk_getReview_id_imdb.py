import nltk, re, pprint
import json
import requests
from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

#main_url = "https://www.imdb.com/title/tt8579674/reviews?ref_=tt_ql_3"

main_url = "https://www.imdb.com/title/tt8579674/reviews?ref_=tt_ql_3"
html = request.urlopen(main_url).read().decode('utf8')
html[:400]

raw = BeautifulSoup(html, 'html.parser')
print(raw)

data = raw.findAll('div',{'id':'main'})
#print(data)
review_only = data[0].findAll('div',{'class':['lister-item mode-detail imdb-user-review collapsable']})

#div_tags = soup.find_all('div')
ids = []
for div in review_only:
     ID = div.get('data-review-id')
     if ID is not None:
        ids.append(ID)

#print(review_only)
#print(ids)