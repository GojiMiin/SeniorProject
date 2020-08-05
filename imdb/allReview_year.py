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

#open file to save data
file = open("imdb_token.txt","w")

#get all movie in the year
all_url = "https://www.imdb.com/list/ls022596827/" #2019
openn = request.urlopen(all_url).read().decode('utf8')
openn[:400]

getPost = BeautifulSoup(openn, 'html.parser')
year = getPost.findAll('div',{'class':'lister-item-image ribbonize'})
#print(len(year))

allMovie = []
for i in range(len(year)):
    #print(i)
    perMovie = year[i].get('data-tconst')
    allMovie.append(perMovie)



for eachMovie in allMovie:
#get Review id
    print(eachMovie)
    main_url = "https://www.imdb.com/title/"+eachMovie+"/reviews?ref_=tt_ql_3"
    #main_url = "https://www.imdb.com/title/tt8579674/reviews?ref_=tt_ql_3"
    html = request.urlopen(main_url).read().decode('utf8')
    html[:400]

    raw = BeautifulSoup(html, 'html.parser')
    data = raw.findAll('div',{'id':'main'})
    review_only = data[0].findAll('div',{'class':'lister-item mode-detail imdb-user-review collapsable'})
    ids = []
    for div in review_only:
        ID = div.get('data-review-id')
        if ID is not None:
            ids.append(ID)

#get review
    for eachid in ids:
    
            url = "https://www.imdb.com/review/"+eachid+"/?ref_=tt_urv"
            html = request.urlopen(url).read().decode('utf8')
            html[:400]

            raw = BeautifulSoup(html, 'html.parser')
        
            #print(raw)

            data = json.loads(raw.find('script', type='application/ld+json').text)
            review = data['reviewBody']
            token = preprocess(review)
            pre = sorted(list(set(token)))
            file.write('[')
            for ele in pre:
                file.write(ele + ',')

            file.write(']'+'\n')
            print("*************************************************************************************************************")
            print(eachid)
            print(pre)

file.close()


