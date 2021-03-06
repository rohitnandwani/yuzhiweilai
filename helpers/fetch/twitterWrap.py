import urllib

import twitter
import twitterFetch
import time


#establish connection with database
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

client = MongoClient('127.0.0.1:27017')
db = client.yuzhiweilaidb
# Issue the serverStatus command and print the results


number_of_results = 10000
results_per_iteration = 100
number_of_iterations = number_of_results / results_per_iteration
number_of_iterations = 1

twitterApi = twitter.Api(consumer_key='BeJvMbvBdYoptsvMiTxCg', consumer_secret='Ny6nzkkPh3IIR56fY2jrBpqBjR547nBnxEeohDRlVo', access_token_key='306720614-JnMHe5U5XHGjlQ33IHkrsUcfmOFUChlHa2Jqtbgd', access_token_secret='eD7HxdD9u6zR0voZyvY5hiLGi9Kv6SoWplhV9w0tuXojE')

def fetchUserTimeline(screenName): 
    statuses = twitterApi.GetUserTimeline(screen_name=screenName)
    return statuses

#print (fetchUserTimeline('RohitNandwani'))

#import sys

#sys.exit(0)

headphoneBrands = [
    "Sony", 
    "Beats", 
    "Bose", 
    "AKG", 
    "Apple", 
    "AudioTechnica", 
    "Beyerdynamic", 
    "Brainwavz", 
    "Creative", 
    "Grado", 
    "Harman Kardon", 
    "JBL", 
    "JLab", 
    "JVC", 
    "Klipsch", 
    "KOSS", 
    "Logitech", 
    "MEEAudio", 
    "Monster", 
    "Panasonic", 
    "Philips", 
    "Pioneer", 
    "Plantronics", 
    "Sennheiser", 
    "Shure", 
    "Skullcandy", 
    "SoundPeats", 
    "V-Moda", 
    "Westone", 
    "Xiaomi"
]

products = ['headphones', 'earphones']



start_time_window = time.time()
count = 0 
results = []
for brand in headphoneBrands:
    for product in products:
        if count >= 180:
            result = db.twitter2.insert_many(results)
            time.sleep(16*60 - (time.time() - start_time_window))
            start_time_window = time.time()
            count = 0
            print(result)
            results = []
        search_term = urllib.quote_plus(brand + ' ' + product)
        print (search_term)
        twitterResponse = twitterFetch.twitterSearch(search_term, '2013-12-01', number_of_iterations)
        currentResults = twitterResponse["all_tweets"]
        count = count + twitterResponse["iterations"]
        results.extend(currentResults)

result = db.twitter2.insert_many(results)
print(result)
