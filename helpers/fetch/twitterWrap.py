import urllib.parse

import twitter
import twitterFetch

twitterApi = twitter.Api(consumer_key='BeJvMbvBdYoptsvMiTxCg', consumer_secret='Ny6nzkkPh3IIR56fY2jrBpqBjR547nBnxEeohDRlVo', access_token_key='306720614-JnMHe5U5XHGjlQ33IHkrsUcfmOFUChlHa2Jqtbgd', access_token_secret='eD7HxdD9u6zR0voZyvY5hiLGi9Kv6SoWplhV9w0tuXojE')

def fetchUserTimeline(screenName): 
    statuses = twitterApi.GetUserTimeline(screen_name=screenName)
    return statuses

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

def getQuery(brand, product, since, count):
    query = urllib.parse.quote_plus(brand + product) + '&result_type=recent&since=' + since + '&count='+count

for brand in headphoneBrands:
    getQuery(brand, 'headphone', '2013-11-01', 1000)
    getQuery(brand, 'earphones', '2013-11-01', 1000)