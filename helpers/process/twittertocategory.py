import re
import wordsdictionaries
import frequencies
import datetime
import time
from datetime import timedelta


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

client = MongoClient('127.0.0.1:27017')
db = client.yuzhiweilaidb
# Issue the serverStatus command and print the results

twitterregx = re.compile("case|hanger", re.IGNORECASE)

twitterReviewsDictionaryWithTime = {}

allDictionaries = wordsdictionaries.getCatDicts()
#create time periods
endTimeString = "2013-12-01"
endTime = time.mktime(datetime.datetime.strptime(endTimeString, "%Y-%m-%d").timetuple())
twitterWithTimePeriods = {}
endTime = datetime.datetime.fromtimestamp(endTime)

startTime = endTime - timedelta(days=365*10)
intervalType = 'weeks'
intervalValue = 12

timePeriods = frequencies.createTimePeriods(startTime, endTime, intervalType, intervalValue)

#add amazon reviews w.r.t timeperiod
#if review_date is start date upto start date + 3months
#    add all the amazon reviews lying in this range to dictionary with key of these 3 months as timeVariable


for i in range (0, len(timePeriods)-1):
    weightedCategoryCount = {}
    startTime = timePeriods[i]
    endTime   = timePeriods[i+1]

    '''
    allTweets = db.twitter.find(
        {
            "$and":
            [
                {"text": {"$not":twitterregx}},
                #{"created_at": {"$gt":startTime}},
                #{"created_at": {"$lt":endTime}}
            ]
        }, 
        {
            "text":1, 
            "created_at":1, "_id":0
        }
    )
    '''
    allTweets = db.twitter.aggregate([
        {
            "$match": {
                "$and":
                [
                    {"text": {"$not":twitterregx}},
                    {"created_at": {"$gt":startTime}},
                    {"created_at": {"$lt":endTime}}
                ]
            }
        }, 
        {
            "$group": {
                "_id": "$id_str",
                "id" : { "$first": "$_id" }, 
                "text": { "$first": "$text" }, 
                "created_at": { "$first": "$created_at" }, 
            }
        }
    ])

    countx = 0
    for tweet in allTweets:
        countx += 1
        #if not analyzer.polarity_scores(tweet['text'].encode('ascii', 'ignore').decode('ascii'))["compound"] < 0.3:
        #    continue
        for dictionaryName, dictionaryValue in allDictionaries.items():
            if any (x in tweet['text'] for x in dictionaryValue):
                if not dictionaryName in weightedCategoryCount:
                    weightedCategoryCount[dictionaryName] = 1
                else:
                    weightedCategoryCount[dictionaryName] += 1
    print (countx)
    
    twitterReviewsDictionaryWithTime[startTime] = weightedCategoryCount
    #print (twitterReviewsDictionaryWithTime)

import csv
f = csv.writer(open("twitterdata.csv", "w"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["time_period", "category", "count"])
 
for timePeriod, weightedCategoryCounts in twitterReviewsDictionaryWithTime.items():
    for key, value in weightedCategoryCounts.items():
        #timePeriod = "{:'%Y-%m-%d'}".format(timePeriod)
        f.writerow([timePeriod, key, value])


