#!/usr/bin/python3

import pymongo
import datetime
import os
import re

username = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASSWORD')
db_name = os.getenv('DB')
host = os.getenv('MONGODB_HOST')
port = os.getenv('MONGODB_PORT')
expiration = os.getenv('SESSION_EXPIRATION')

print(f"Current time: {datetime.datetime.now()}")

try:
    if username is None or username == '':
        mongodb = "mongodb://" + host + ':' + port + "/"
    else:
        mongodb = "mongodb://" + username + ':' + password + '@' + host + ':' + port + "/"
except TypeError:
    print("请先配置MongoDB连接地址！")


client = pymongo.MongoClient(mongodb)
db = client[db_name]
col = db["session"]

days = re.compile(r'\d+d',re.I)
hours = re.compile(r'\d+h',re.I)
num = re.compile(r'\d+')
now = datetime.datetime.today()
d = int(num.search(days.search(expiration).group(0)).group(0))
h = int(num.search(hours.search(expiration).group(0)).group(0))
query = {"expiration": {"$lt": (now + datetime.timedelta(days=d,hours=h))}}

n = col.delete_many(query)
print(n.deleted_count, "个session(s)已清理")
