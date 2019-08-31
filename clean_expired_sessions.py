#!/usr/bin/python3

import pymongo
import datetime
import os

mydbuser = os.getenv('MONGODB_USER')
mydbpassword = os.getenv('MONGODB_PASSWORD')
mydbname = os.getenv('DB')
mydblink = os.getenv('MONGODB_LINK')
mydbport = os.getenv('PORT')
mongodb = "mongodb://" + mydbuser + ':' + mydbpassword + '@' + mydblink + ':' + mydbport + "/"

myclient = pymongo.MongoClient(mongodb)
mydb = myclient[mydbname]
mycol = mydb["session"]
myquery = {"expiration": {"$lt": datetime.datetime.today()}}
n = mycol.delete_many(myquery)
print(n.deleted_count, "个session已清理")
