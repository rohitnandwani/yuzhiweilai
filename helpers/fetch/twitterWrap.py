import twitter


twitterApi = twitter.Api(consumer_key='BeJvMbvBdYoptsvMiTxCg', consumer_secret='Ny6nzkkPh3IIR56fY2jrBpqBjR547nBnxEeohDRlVo', access_token_key='306720614-JnMHe5U5XHGjlQ33IHkrsUcfmOFUChlHa2Jqtbgd', access_token_secret='eD7HxdD9u6zR0voZyvY5hiLGi9Kv6SoWplhV9w0tuXojE')


def fetchUserTimeline(screenName): 
    statuses = twitterApi.GetUserTimeline(screen_name=screenName)
    return statuses
 

def searchManyTweets(searchTerm, resultType, since, until, numberOfTweets):
    results = twitterApi.GetSearch(raw_query="q=Xiaomi%20earphone%20&result_type=recent&since=2013-11-01&count=1000")
    print (results)
    return


searchManyTweets(1, 2, 3, 4, 10000)







