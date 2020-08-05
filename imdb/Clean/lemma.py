import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re
import pandas as pd
import itertools
wordnet_lemmatizer = WordNetLemmatizer()
reSentence = []
allLabel = []
#print(stopwords.words('english'))
#print("--------------------------------------")

# bring in sentence from file
readIn = pd.read_csv("IMDB Dataset.csv")
sample = readIn.head(100)
InFilter = sample['review'].astype('string')
Label = sample['sentiment'].astype('string')
InFilter.drop(InFilter.head(0))
print(InFilter)


for label in Label:
    allLabel.append(label)

print(allLabel)
#sentence = "One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked. They are right, as this is exactly what happened with me.<br /><br />The first thing that struck me about Oz was its brutality and unflinching scenes of violence, which set in right from the word GO. Trust me, this is not a show for the faint hearted or timid. This show pulls no punches with regards to drugs, sex or violence. Its is hardcore, in the classic use of the word.<br /><br />It is called OZ as that is the nickname given to the Oswald Maximum Security State Penitentary. It focuses mainly on Emerald City, an experimental section of the prison where all the cells have glass fronts and face inwards, so privacy is not high on the agenda. Em City is home to many..Aryans, Muslims, gangstas, Latinos, Christians, Italians, Irish and more....so scuffles, death stares, dodgy dealings and shady agreements are never far away.<br /><br />I would say the main appeal of the show is due to the fact that it goes where other shows wouldn't dare. Forget pretty pictures painted for mainstream audiences, forget charm, forget romance...OZ doesn't mess around. The first episode I ever saw struck me as so nasty it was surreal, I couldn't say I was ready for it, but as I watched more, I developed a taste for Oz, and got accustomed to the high levels of graphic violence. Not just violence, but injustice (crooked guards who'll be sold out for a nickel, inmates who'll kill on order and get away with it, well mannered, middle class inmates being turned into prison bitches due to their lack of street skills or prison experience) Watching Oz, you may become comfortable with what is uncomfortable viewing....thats if you can get in touch with your darker side."


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
        # delIter = ''.join(ch for ch, _ in itertools.groupby(w)) #delete repeat alphabet
        if not w in stopwords.words('English'):  # delete stopwords
            cleaned.append(w)

#result = " ".join(token_word)

# lemma ---------------

#sentence_words = nltk.word_tokenize(result)
    lemma_word_cleaned = []
    for word in cleaned:
        lemma_word_cleaned.append(wordnet_lemmatizer.lemmatize(word, pos="v"))

    lemma_sentence_cleaned = " ".join(lemma_word_cleaned)
    reSentence.append(lemma_sentence_cleaned)


data = {'cleaned_review': reSentence, 'Label': allLabel}
toFile = pd.DataFrame(data)
toFile.to_csv("./lemma_result.csv", index=False)


    
