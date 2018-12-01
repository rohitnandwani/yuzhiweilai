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
  next_results = "?q="+searchTerm+"&result_type=recent&count=100"
  trends_tweets = [None] * iterations
  trend_tweets_dict_aggregated = []
  for i in range(0, iterations):
    '''
    if i==0:
      trends_tweets[i] = fetchTwitterData("https://api.twitter.com/1.1/search/tweets.json?q="+query+"&result_type=mixed&count=100")
      
    else:
      trends_tweets[i] = fetchTwitterData("https://api.twitter.com/1.1/search/tweets.json?max_id=" + max_id + "&q="+query+"&result_type=mixed&count=100")
      #trends_tweets[i] = fetchTwitterData("https://api.twitter.com/1.1/search/tweets.json"+next_results)
    '''
    trends_tweets[i] = fetchTwitterData("https://api.twitter.com/1.1/search/tweets.json"+next_results)
    
 
    for line in trends_tweets[i]:
      statuses_with_metadata = ujson.loads(line)
      trend_tweets_dict_aggregated.extend(statuses_with_metadata['statuses'])
      
    max_id = statuses_with_metadata['search_metadata']['max_id_str']
    
    if i==0:
      first_since_id = statuses_with_metadata['search_metadata']['since_id_str']
    
    if 'next_results' in statuses_with_metadata['search_metadata']:
      next_results = statuses_with_metadata['search_metadata']['next_results']
    else:
      break

    print ('For searchTerm: '+searchTerm+' Iteration: '+str(i))
    #print 'Max_id: '+str(max_id)
    #print 'Next_results: '+str(next_results)
    
    
  return trend_tweets_dict_aggregated
    
