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
readIn = pd.read_csv("../SeniorProjectFile/imdb_master.csv")
sample = readIn
InFilter = sample['review'].astype('string')
Label = sample['sentiment'].astype('string')
InFilter.drop(InFilter.head(0))

for label in Label:
    allLabel.append(label)

# Encode Label
le = LabelEncoder()
EnLabel = le.fit_transform(allLabel)
print(EnLabel)

# lowercase & remove html tag -----------
for sentence in InFilter:
    lower_sentence = sentence.lower()
    clean = re.compile('<.*?>')
    sentence_no_tag = re.sub(clean, '', lower_sentence)

# tokenization and clean word -----------
    cleaned = []
    tokenizer = RegexpTokenizer(r'\w+')
    token_sentence = tokenizer.tokenize(sentence_no_tag)
    for w in token_sentence:
        if not w in stopwords.words('English'):  # delete stopwords
            cleaned.append(w)

# lemma ---------------
    lemma_word_cleaned = []
    for word in cleaned:
        lemma_word_cleaned.append(wordnet_lemmatizer.lemmatize(word, pos="v"))

    lemma_sentence_cleaned = " ".join(lemma_word_cleaned)
    reSentence.append(lemma_sentence_cleaned)


data = {'cleaned_review': reSentence, 'Label': EnLabel}
toFile = pd.DataFrame(data)
toFile.to_csv("./lemma_result.csv", index=False)
