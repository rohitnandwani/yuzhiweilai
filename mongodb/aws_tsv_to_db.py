#read the file
import csv
import sys

#establish connection with database
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("127.0.0.1:27017")
db = client.yuzhiweilaidb
# Issue the serverStatus command and print the results


datapath = "/Users/anand/Documents/dmProject/yuzhiweilai/awsData/amazon_reviews_us_Electronics_v1_00.tsv"
with open(datapath, "rt", encoding = "utf8") as amazonReviews:
    amazonReviews = csv.reader(amazonReviews, delimiter='\t')

    #loop over all the records
    count = 0
    toDatabase = []                                #Storing actual values in a dictionary
    for amazonReview in amazonReviews:
        count += 1
        if count == 1:
            keyArray = amazonReview
        else:
            reviewDictionary = {}
            for i in range(0, len(keyArray)-1):
                key = keyArray[i]
                value = amazonReview[i]
                reviewDictionary[key] = value
            toDatabase.append(reviewDictionary)
    
result = db.reviews.insert_many(toDatabase)
print(result)

        #print(index, amazonReview)
        #print(type(amazonReview), amazonReview)





#dump