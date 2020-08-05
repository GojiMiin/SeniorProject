from nltk import word_tokenize
from urllib import request
from bs4 import BeautifulSoup

year_url = "https://www.imdb.com/list/ls022596827/"
html = request.urlopen(year_url).read().decode('utf8')
html[:400]

raw = BeautifulSoup(html, 'html.parser')
movieblock = raw.findAll('h3',{'class':'lister-item-header'})

movieName = []
for i in range(len(movieblock)):
    name = movieblock[i].find('a').contents[0]
    movieName.append(str(name))

nameFile = open("ImdbName2019.txt","w")
for j in range(len(movieName)):
    eachName = movieName[j].replace(" ","_")
    print(eachName)
    nameFile.write(eachName + "\n")

nameFile.close()
