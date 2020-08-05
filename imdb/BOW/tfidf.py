import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_word_value = []

readIn = pd.read_csv("../Clean/lemma_result.csv")
sample = readIn.head(100)

all_review_cleaned = sample['cleaned_review'].astype('string')
all_label = sample['Label'].astype('string')
all_review_cleaned.drop(all_review_cleaned.head(0))

#TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(all_review_cleaned)
#print(X.shape)
tfidf_allword_value = list(zip(vectorizer.get_feature_names(), X.sum(0).getA1()))
print("{0:20}{1:20}".format("Word", "result"))

for word in tfidf_allword_value:
    print(word)

print(X.toarray())

data = {'Word': vectorizer.get_feature_names(), 'Weight': X.sum(0).getA1()}
toFile = pd.DataFrame(data)
toFile.to_csv("./tfidf_result.csv", index=False)

