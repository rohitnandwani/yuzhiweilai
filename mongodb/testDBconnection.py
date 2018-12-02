import csv
import sys
import datetime


#establish connection with database
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string


connection = MongoClient('ds123976.mlab.com', 23976)
db = connection['yuzhiweilaidb']
db.authenticate('admin', 'admin1')


print (db)

result = db.new.insert_many([{'hello_biatch' : 1}, {'hello_biatch' : 2}])