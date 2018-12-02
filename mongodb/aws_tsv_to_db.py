#read the file
import csv
import sys
import datetime


#establish connection with database
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

connection = MongoClient('ds123976.mlab.com', 23976)
db = connection['yuzhiweilaidb']
db.authenticate('admin', 'admin1')
# Issue the serverStatus command and print the results


datapath = "/Users/rohit/Documents/Assignments/data_mining/final_project/data/amazon_reviews_us_Electronics_v1_00.tsv"
with open(datapath, "rt") as amazonReviews:
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
            for i in range(0, len(keyArray)):
                key = keyArray[i]
                try:
                    value = amazonReview[i]
                    if key == 'review_date':
                        value = datetime.datetime.strptime(value, '%Y-%m-%d')
                    reviewDictionary[key] = value
                except:
                    pass
            toDatabase.append(reviewDictionary)

    
result = db.reviews.insert_many(toDatabase)
print(result)
