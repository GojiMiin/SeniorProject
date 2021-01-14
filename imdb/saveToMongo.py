from pymongo import MongoClient
import pandas as pd

data = pd.read_csv('18_19.csv')
client =  MongoClient("mongodb+srv://GojiMiin:342510@movieweb.r4ob8.mongodb.net/test?retryWrites=true&w=majority")
db = client['MovieDetail']
collection = db['Imdb']

data.reset_index(inplace=True)
data_dict = data.to_dict("records")
collection.insert_many(data_dict)
