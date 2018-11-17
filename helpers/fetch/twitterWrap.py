import twitter


twitterApi = twitter.Api(consumer_key='BeJvMbvBdYoptsvMiTxCg', consumer_secret='Ny6nzkkPh3IIR56fY2jrBpqBjR547nBnxEeohDRlVo', access_token_key='306720614-JnMHe5U5XHGjlQ33IHkrsUcfmOFUChlHa2Jqtbgd', access_token_secret='eD7HxdD9u6zR0voZyvY5hiLGi9Kv6SoWplhV9w0tuXojE')


def fetchUserTimeline(screenName): 
    statuses = twitterApi.GetUserTimeline(screen_name=screenName)
    return statuses







