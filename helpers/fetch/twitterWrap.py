import twitter

twitterApi = twitter.Api(consumer_key='l4nKhphV5g5KNpBtUglaw', consumer_secret='1U6cCn5oKulzn5aNtZY90iSTJZXDuU3mph5AeJ8aE', access_token_key='306720614-ADqPkQjbPAiPuKr9n2OgQVfVprUt4UZhinCVHKuZ', access_token_secret='LdcPlH0m02zxL8hpj3yV0BgKULVXrSkuRPbz1pw814Y')

def fetchUserTimeline(screenName): 
    statuses = twitterApi.GetUserTimeline(screen_name=screenName)
    return statuses
