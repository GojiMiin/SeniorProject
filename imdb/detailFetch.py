from urllib import request
from bs4 import BeautifulSoup
import re
import pandas as pd

movieName = []
movieCode = []
movieYear = []
movieTime = []
movieRate = []
movieCate = []
moviePoster = []
movieDesciption = []
clean_des = []
imdbScore = []

allurl = ["https://www.imdb.com/list/ls058813655/", "https://www.imdb.com/list/ls022596827/"] #2018,2019
for link in allurl:
    openn = request.urlopen(link).read().decode('utf8')
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

        #get movie description
        des = movieBlock[i].find('p',{'class':''}).contents

        #get movie score
        score = movieBlock[i].find('span',{'class':'ipl-rating-star__rating'}).contents[0]

        movieName.append(str(name))
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

        #Clean movie description
        for i in des:
            des_del_n = re.sub("\n","", str(i))
            des_del_link = re.sub("<[^>]*>","", str(des_del_n))
            clean_des.append(des_del_link)

        full_sentence = " ".join(clean_des)
        clean_des = []
        movieDesciption.append(full_sentence.strip())
        imdbScore.append(score)

for i in movieCode:
    openn = request.urlopen("https://www.imdb.com/title/"+i+"/?ref_=ttls_li_tt").read().decode('utf8')
    openn[:400]
    mPage = BeautifulSoup(openn, 'html.parser')
    pBlock = mPage.find('div',{'class':'poster'})
    posterLink = pBlock.find('a', href=True).get('href')

    new_open = request.urlopen("https://www.imdb.com"+posterLink).read().decode('utf8')
    new_open[:400]
    fpPage = BeautifulSoup(new_open, 'html.parser')
    posterBlock = fpPage.find('div',{'class':'MediaViewerImagestyles__PortraitContainer-sc-1qk433p-2 gIroZm'})
    fullPoster = posterBlock.find('img').get('src')
    moviePoster.append(fullPoster)

data = {'code': movieCode,
        'year': movieYear,
        'name': movieName,
        'time': movieTime,
        'category': movieCate,
        'rate': movieRate,
        'imdbscore': imdbScore,
        'poster': moviePoster,
        'description': movieDesciption}
toFile = pd.DataFrame(data)

toFile.to_csv("./18_19.csv", index=False)

