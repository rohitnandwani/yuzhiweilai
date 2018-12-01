import csv
import sys
import datetime


#establish connection with database
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

db = MongoClient('mongodb://admin:admin1@ds123976.mlab.com:23976/yuzhiweilaidb')

result = db.reviews.insert([{'hello_biatch' : 1}, {'hello_biatch' : 2}])