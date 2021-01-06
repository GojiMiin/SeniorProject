from urllib import request
from bs4 import BeautifulSoup
import re

movieName = []
movieCode = []
movieSource = []
movieYear = []
movieTime = []
movieRate = []
movieCate = []
moviePoster = []
movieDesciption = []
clean_des = []
movieScore = []

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

    #get movie category
    cate = movieBlock[i].find('span',{'class':'genre'}).contents[0]

    #get movie poster link
    plink = movieCodeLocation[i].find('img',{'class':'loadlate'}).get('loadlate')

    #get movie description
    des = movieBlock[i].find('p',{'class':''}).contents

    #get movie score
    score = movieBlock[i].find('span',{'class':'ipl-rating-star__rating'}).contents[0]

    movieName.append(str(name))
    movieSource.append("imdb")
    movieCode.append(str(code))
    movieYear.append(yearNum[0])
    movieTime.append(time)

    #Clean movie rate
    if(str(rate) != "None"):
        clearRate = re.sub("<[^>]*>","", str(rate))
        movieRate.append(clearRate)
    else:
        movieRate.append("None")

    #Clean movie category
    del_n = re.sub("\n", "", str(cate))
    movieCate.append(del_n.rstrip())

    moviePoster.append(plink)

    #Clean movie description
    for i in des:
        des_del_n = re.sub("\n","", str(i))
        des_del_link = re.sub("<[^>]*>","", str(des_del_n))
        clean_des.append(des_del_link)

    full_sentence = " ".join(clean_des)
    clean_des = []
    movieDesciption.append(full_sentence.strip())
    movieScore.append(score)


print(movieScore)