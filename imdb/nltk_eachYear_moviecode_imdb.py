import nltk
import pandas as pd
from urllib import request
from bs4 import BeautifulSoup

#get all id from list
all_url = "https://www.imdb.com/list/ls022596827/" #2019
openn = request.urlopen(all_url).read().decode('utf8')
openn[:400]

allMovie = []
getPost = BeautifulSoup(openn, 'html.parser')
year = getPost.findAll('div',{'class':'lister-item-image ribbonize'})
#print(len(year))


for i in range(len(year)):
    #print(i)
    perMovie = year[i].get('data-tconst')
    allMovie.append(perMovie)

print(allMovie)

#save code to csv file
data = {'Movie Code': allMovie}
toFile = pd.DataFrame(data)
toFile.to_csv("./2019MovieCode.csv", sep=',', index=False)
