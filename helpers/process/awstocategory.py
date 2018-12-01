import re
import wordsdictionaries
import sentiment
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

client = MongoClient('127.0.0.1:27017')
db = client.yuzhiweilaidb
# Issue the serverStatus command and print the results

amzregx1 = re.compile("/headphone|earphone", re.IGNORECASE)
amzregx2 = re.compile("case|hanger", re.IGNORECASE)


amzReviews = db.reviews.find(
    {
        "$and":[
            {"product_title": amzregx1},
            {"product_title": {"$not":amzregx2}}
        ]
    }, 
    {
        "review_body":1, 
        "review_date":1, "_id":0
    }
    ).limit(10)

weightedCategoryCount = {} 
allDictionaries = wordsdictionaries.getCatDicts()


for amzReview in amzReviews:
    for dictionaryName, dictionaryValue in allDictionaries.items():
        if any (x in amzReview['review_body'] for x in dictionaryValue):
            if not dictionaryName in weightedCategoryCount:
                weightedCategoryCount[dictionaryName] = 1
            else:
               weightedCategoryCount[dictionaryName] += 1

print(weightedCategoryCount)

            


