#!/usr/bin/python3

import pymongo
import datetime
import os

dbuser = os.getenv('MONGODB_USER')
dbpassword = os.getenv('MONGODB_PASSWORD')
dbname = os.getenv('DB')
dblink = os.getenv('MONGODB_LINK')
dbport = os.getenv('MONGODB_PORT')

try:
    if dbuser is None:
        if dbpassword is None:
            mongodb = "mongodb://" + dblink + ':' + dbport + "/"
        else:
            mongodb = "mongodb://" + dbuser + '@' + dblink + ':' + dbport + "/"
    else:
        mongodb = "mongodb://" + dbuser + ':' + dbpassword + '@' + dblink + ':' + dbport + "/"
except TypeError:
    print("请先配置MongoDB连接地址！")

try:
    client = pymongo.MongoClient(mongodb)
    db = client[dbname]
    col = db["session"]
    query = {"expiration": {"$lt": datetime.datetime.today()}}
    n = col.delete_many(query)
except (TypeError, NameError):
    print("连接失败!")
else:
    print(n.deleted_count, "个session已清理")
