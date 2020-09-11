import itertools
import pandas as pd
import re
from nltk.tokenize import RegexpTokenizer
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
import nltk
nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()
reSentence = []
allLabel = []

# bring in sentence from file
readIn = pd.read_csv("IMDB Dataset.csv")
sample = readIn.head(1000)
InFilter = sample['review'].astype('string')
Label = sample['sentiment'].astype('string')
InFilter.drop(InFilter.head(0))

for label in Label:
    allLabel.append(label)

#Encode Label
le = LabelEncoder()
EnLabel = le.fit_transform(allLabel)
print(EnLabel)