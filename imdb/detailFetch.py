import pandas as pd
from urllib import request
from bs4 import BeautifulSoup
import re

movieName = []
movieCode = []
movieSource = []
movieYear = []
movieTime = []
movieRate = []

all_url = "https://www.imdb.com/list/ls022596827/" #2019
openn = request.urlopen(all_url).read().decode('utf8')
openn[:400]

getPost = BeautifulSoup(openn, 'html.parser')
movieCodeLocation = getPost.findAll('div',{'class':'lister-item-image ribbonize'})
movieBlock = getPost.findAll('div',{'class':'lister-item-content'})

for i in range(len(movieBlock)):
    #get name
    name = movieBlock[i].find('a').contents[0]

    #get movie code
    code = movieCodeLocation[i].get('data-tconst')

    #get movie year
    year = movieBlock[i].find('span',{'class':'lister-item-year text-muted unbold'}).contents[0]
    yearNum = re.findall(r'\d+', str(year))

    #get movie time
    time = movieBlock[i].find('span',{'class':'runtime'}).contents[0]

    #get movie rate
    rate = movieBlock[i].find('span',{'class':'certificate'})

    movieName.append(str(name))
    movieSource.append("imdb")
    movieCode.append(str(code))
    movieYear.append(yearNum[0])
    movieTime.append(time)
    if(rate != None):
        clearRate = re.sub(r'/<\/?span[^>]*>/g',"", str(rate))
        movieRate.append(clearRate)
    else:
        movieRate.append("None")

print(movieRate)