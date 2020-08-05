import pandas as pd

positive_sentence = []
negative_sentence = []
positive_label = []
negative_label = []


readIn = pd.read_csv("lemma_result.csv")
sample = readIn.head(100)

#print(type(sample))

for i in range(len(sample)):
    if (sample.values[i][1] == "positive"):
        positive_sentence.append(sample.values[i][0])
        positive_label.append(sample.values[i][1])

    elif (sample.values[i][1] == "negative"):
        negative_sentence.append(sample.values[i][0])
        negative_label.append(sample.values[i][1])
    
    
positive_data = {'cleaned_review': positive_sentence, 'Label': positive_label}
negative_data = {'cleaned_review': negative_sentence, 'Label': negative_label}

toPosFile = pd.DataFrame(positive_data)
toNegFile = pd.DataFrame(negative_data)

toPosFile.to_csv("./posFile.csv", index=False)
toNegFile.to_csv("./negFile.csv", index=False)
