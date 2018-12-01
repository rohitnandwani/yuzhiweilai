import re
import wordsdictionaries
import frequencies
import datetime
import time
from datetime import timedelta

#import sentiment
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

client = MongoClient('127.0.0.1:27017')
db = client.yuzhiweilaidb
# Issue the serverStatus command and print the results

amzregx1 = re.compile("/headphone|earphone", re.IGNORECASE)
amzregx2 = re.compile("case|hanger", re.IGNORECASE)

amazonReviewsDictionaryWithTime = {}

allDictionaries = wordsdictionaries.getCatDicts()
#create time periods
endTimeString = "2011-12-01"
endTime = time.mktime(datetime.datetime.strptime(endTimeString, "%Y-%m-%d").timetuple())
amzReviewsWithTimePeriods = {}
endTime = datetime.datetime.fromtimestamp(endTime)

startTime = endTime - timedelta(days=365*10)
intervalType = 'weeks'
intervalValue = 12

timePeriods = frequencies.createTimePeriods(startTime, endTime, intervalType, intervalValue)

#add amazon reviews w.r.t timeperiod
#if review_date is start date upto start date + 3months
#    add all the amazon reviews lying in this range to dictionary with key of these 3 months as timeVariable

weightedCategoryCount = {}
for i in range (0, len(timePeriods)-1):
    startTime = timePeriods[i]
    endTime   = timePeriods[i+1]
    amzReviews = db.reviews.find(
        {
            "$and":
            [
                {"product_title": amzregx1},
                {"product_title": {"$not":amzregx2}},
                {"review_date": {"$gt":startTime}},
                {"review_date": {"$lt":endTime}}
            ]
        }, 
        {
            "review_body":1, 
            "review_date":1, "_id":0
        }
    )
    print (amzReviews)

    for amzReview in amzReviews:
        for dictionaryName, dictionaryValue in allDictionaries.items():
            if any (x in amzReview['review_body'] for x in dictionaryValue):
                if not dictionaryName in weightedCategoryCount:
                    weightedCategoryCount[dictionaryName] = 1
                else:
                    weightedCategoryCount[dictionaryName] += 1
    
    amazonReviewsDictionaryWithTime[startTime] = weightedCategoryCount
    print (amazonReviewsDictionaryWithTime)

import csv
f = csv.writer(open("test.csv", "w+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["time_period", "category", "count"])
 
for timePeriod, weightedCategoryCounts in amazonReviewsDictionaryWithTime.items():
    for key, value in weightedCategoryCounts.items():
        timePeriod = "{:'%Y-%m-%d'}".format(timePeriod)
        f.writerow([timePeriod, key, value])


#for timePeriod in timePeriods:
#    for amzReview in amzReviews:
#        for dictionaryName, dictionaryValue in allDictionaries.items():
#            if any (x in amzReview['review_body'] for x in dictionaryValue):
#                if not dictionaryName in weightedCategoryCount:
#                    weightedCategoryCount[dictionaryName] = 1
#                else:
#                    weightedCategoryCount[dictionaryName] += 1
#print(weightedCategoryCount)

            


