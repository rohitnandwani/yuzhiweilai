# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 14:48:06 2015

@author: Nandwani
"""
import twitterRequest
import ujson


def fetchTwitterData(url):
  #url = "https://stream.twitter.com/1/statuses/sample.json"
  #url = "https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi"

  
  parameters = []
  response = twitterRequest.twitterreq(url, "GET", parameters)
  #for line in response:
    #print line.strip()

  return response
  

def twitterSearch(searchTerm, until, iterations):
  max_id = str(0)
  next_results = "q="+searchTerm+"&result_type=recent&count=1000000"
  all_tweets = []
  for i in range(0, iterations):
    if i==0:
      response = fetchTwitterData("https://api.twitter.com/1.1/search/tweets.json?"+next_results)
      
    else:
      response = fetchTwitterData("https://api.twitter.com/1.1/search/tweets.json?max_id=" + max_id + "&" + next_results)


    for line in response:
      statuses_with_metadata = ujson.loads(line)
      if not 'statuses' in statuses_with_metadata:
        print (line)
      all_tweets.extend(statuses_with_metadata['statuses'])
      
    max_id = statuses_with_metadata['search_metadata']['max_id_str']

    print (searchTerm + ': ' + str(i))

  return {"all_tweets" : all_tweets, "iterations" : i+1}