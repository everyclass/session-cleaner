#!/usr/bin/python3

import pymongo
import datetime
import os

mydbuser = os.getenv('MONGODB_USER')
mydbpassword = os.getenv('MONGODB_PASSWORD')
mydbname = os.getenv('DB')
mydblink = os.getenv('MONGODB_LINK')
mydbport = os.getenv('MONGODB_PORT')

try:
    if mydbuser is None:
        if mydbpassword is None:
            mongodb = "mongodb://" + mydblink + ':' + mydbport + "/"
        else:
            mongodb = "mongodb://" + mydbuser + '@' + mydblink + ':' + mydbport + "/"
    else:
        mongodb = "mongodb://" + mydbuser + ':' + mydbpassword + '@' + mydblink + ':' + mydbport + "/"
except TypeError:
    print("请先配置MongoDB连接地址！")

try:
    myclient = pymongo.MongoClient(mongodb)
    mydb = myclient[mydbname]
    mycol = mydb["session"]
    myquery = {"expiration": {"$lt": datetime.datetime.today()}}
    n = mycol.delete_many(myquery)
except TypeError, NameError:
    print("连接失败!")
else:
    print(n.deleted_count, "个session已清理")
