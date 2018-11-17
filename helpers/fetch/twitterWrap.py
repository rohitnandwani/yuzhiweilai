import twitter
##################################
import tweepy
from tweepy import OAuthHandler
import json
import datetime as dt
import time
import os
import sys

def load_api():
    ''' Function that loads the twitter API after authorizing
        the user. '''
 
    consumer_key = 'l4nKhphV5g5KNpBtUglaw'
    consumer_secret = '1U6cCn5oKulzn5aNtZY90iSTJZXDuU3mph5AeJ8aE'
    access_token = '306720614-ADqPkQjbPAiPuKr9n2OgQVfVprUt4UZhinCVHKuZ'
    access_secret = 'LdcPlH0m02zxL8hpj3yV0BgKULVXrSkuRPbz1pw814Y'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # load the twitter API via tweepy
    return tweepy.API(auth)

hashtags = []
mentions = []
    tweet_count = 0
    end_date = datetime.utcnow() - timedelta(days=30)
    for status in Cursor(auth_api.user_timeline, id=target).items():
      tweet_count += 1
      if hasattr(status, "entities"):
        entities = status.entities
        if "hashtags" in entities:
          for ent in entities["hashtags"]:
            if ent is not None:
              if "text" in ent:
                hashtag = ent["text"]
                if hashtag is not None:
                  hashtags.append(hashtag)
        if "user_mentions" in entities:
          for ent in entities["user_mentions"]:
            if ent is not None:
              if "screen_name" in ent:
                name = ent["screen_name"]
                if name is not None:
                  mentions.append(name)
      if status.created_at < end_date:
        break
###########################
twitterApi = twitter.Api(consumer_key='l4nKhphV5g5KNpBtUglaw', consumer_secret='1U6cCn5oKulzn5aNtZY90iSTJZXDuU3mph5AeJ8aE', access_token_key='306720614-ADqPkQjbPAiPuKr9n2OgQVfVprUt4UZhinCVHKuZ', access_token_secret='LdcPlH0m02zxL8hpj3yV0BgKULVXrSkuRPbz1pw814Y')

def fetchUserTimeline(screenName): 
    statuses = twitterApi.GetUserTimeline(screen_name=screenName,include_entities=True)
    return statuses







