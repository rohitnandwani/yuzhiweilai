import twitter

import nltk



import collections



api = twitter.Api(consumer_key='l4nKhphV5g5KNpBtUglaw', consumer_secret='1U6cCn5oKulzn5aNtZY90iSTJZXDuU3mph5AeJ8aE', access_token_key='306720614-ADqPkQjbPAiPuKr9n2OgQVfVprUt4UZhinCVHKuZ', access_token_secret='LdcPlH0m02zxL8hpj3yV0BgKULVXrSkuRPbz1pw814Y')

print(api.VerifyCredentials())

statuses = api.GetUserTimeline(screen_name='wirecutter')

print(type(statuses))

print(len(statuses))

all_status_text = ''

for status in statuses:

    if(status.text):

        all_status_text += status.text + '\n'

tokenized_statuses = nltk.word_tokenize(all_status_text)

tagged_statuses = nltk.pos_tag(tokenized_statuses)

frequency_array = []

for tagged_status in tagged_statuses:

    frequency_array.append(tagged_status[0])



counter=collections.Counter(frequency_array)

print (counter)