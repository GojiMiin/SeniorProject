import nltk, re, pprint
import pandas as pd
import numpy as np
import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

#min_df = delete word occur under n times
vectorizer = CountVectorizer(min_df=2)

readIn = pd.read_csv("IMDB Dataset.csv")
InFilter = readIn['review'].astype('string')
InFilter.drop(InFilter.head(0))
count = 0

for i in range(len(InFilter)):
    allWord = InFilter[i].split()
    new = []
    FilteredSentence = ""

    #detect repeat alphabet
    for word in allWord:
        repeat_pattern = re.compile(r'(.)\1{2}') 
        new_word = repeat_pattern.sub(" ",word)
        new.append(new_word)
        if(new_word!=" "):
            count += 1
            
    #put filtered sentense into obj
    FilteredSentence = ' '.join(new)
    InFilter[i] = FilteredSentence

#print(InFilter)

#put data into vectorizer to make occurance
vec = vectorizer.fit_transform(InFilter)
print(list(zip(vectorizer.get_feature_names(), vec.sum(0).getA1()))) #print occurance with word
#print(vectorizer.get_feature_names())

#save to csv
data = {'word': vectorizer.get_feature_names(), 'Occurance': vec.sum(0).getA1()}
toFile = pd.DataFrame(data)
toFile.to_csv("./occurance.csv", sep=',', index=False)