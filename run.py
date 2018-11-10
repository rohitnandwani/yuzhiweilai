import collections
import nltk

from datetime import date, datetime, timedelta

from helpers.fetch import twitterWrap
from helpers.filter import keywords
from helpers.process import frequencies

statuses = twitterWrap.fetchUserTimeline('wirecutter')

for status in statuses:
    status.tokenized_tweet = nltk.word_tokenize(status.text)
    status.tagged_tweet = nltk.pos_tag(status.tokenized_tweet)
    status.filteredKeywords = keywords.filterKeywords(status.tagged_tweet)
    

endTime = datetime.now()
startTime = endTime - timedelta(days=365)
intervalType = 'weeks'
intervalValue = 2

timePeriods = frequencies.createTimePeriods(startTime, endTime, intervalType, intervalValue)
frequencies = {}


for status in statuses:


#frequency_array = []

#for tagged_status in tagged_statuses:
#
#    frequency_array.append(tagged_status[0])



#counter=collections.Counter(frequency_array)

#print (counter)