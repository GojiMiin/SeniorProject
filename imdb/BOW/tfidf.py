import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

tfidf_word_value = []
X = []

readIn = pd.read_csv("../Clean/lemma_result.csv")

X_temp = readIn.iloc[:10, :-1].values
Y = readIn.iloc[:10, -1].values

for sentence in X_temp:
    X.append(sentence[0])

#split data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

# TF-IDF
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)



#test = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
#test.to_csv("./tfidf_result.csv", index=False)


# print(X.shape)
#tfidf_allword_value = list(zip(vectorizer.get_feature_names(), X.sum(0).getA1()))
#print("{0:20}{1:20}".format("Word", "result"))

# for word in tfidf_allword_value:
#    print(word)

# print(X.toarray())

#data = {'Word': vectorizer.get_feature_names(), 'Weight': X.sum(0).getA1()}
#toFile = pd.DataFrame(data)
#toFile.to_csv("./tfidf_result.csv", index=False)
