# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:30:51 2018

@author: owner
"""

import tweepy
from tweepy.auth import OAuthHandler
#Twitter API credentials
consumer_key = 'l4nKhphV5g5KNpBtUglaw'
consumer_secret = '1U6cCn5oKulzn5aNtZY90iSTJZXDuU3mph5AeJ8aE'
access_key = '306720614-ADqPkQjbPAiPuKr9n2OgQVfVprUt4UZhinCVHKuZ'
access_secret = 'LdcPlH0m02zxL8hpj3yV0BgKULVXrSkuRPbz1pw814Y'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#refer http://docs.tweepy.org/en/v3.2.0/api.html#API
#tells tweepy.API to automatically wait for rate limits to replenish

search = tweepy.Cursor(api.search, q="headphone", 
                       since="2013-11-01",
                       until="2018-11-01",
                       lang="en").items()
 
for item in search:    
    # print tweet text
    print (item.text)
    
    # print tweet created date 
    print (item.created_at)
    
    # print the username who published the tweet
    print (item.user.name)
    
    # print the language code of the tweet
    print (item.metadata['iso_language_code'])
    
    # print the search result type
    print (item.metadata['result_type'])
    
    # print the device/source from which the tweet has been published
    # e.g. Twitter for Android, Twitter for iPhone, Twitter Web Client, etc.
    print (item.source)
    
search1 = tweepy.Cursor(api.search, q="headphone", result_type="recent", lang="en",since='2013-11-01', until='2018-11-01').items(20)
for item in search1:
    # print list of hashtags present in the tweet 
    # print empty list when no hashtag is present
    hashtags = item.entities['hashtags']
    if hashtags:
        ht = [ht['text'] for ht in hashtags]
        print (ht)
    else:
        print (hashtags) 
        
for tweet in tweepy.Cursor(api.search, q="headphone",lang="en").items():
    print (tweet.created_at, tweet.text)