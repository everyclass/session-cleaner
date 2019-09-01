#!/usr/bin/python3

import pymongo
import datetime
import os

username = os.getenv('MONGODB_USER')
password = os.getenv('MONGODB_PASSWORD')
db_name = os.getenv('DB')
host = os.getenv('MONGODB_HOST')
port = os.getenv('MONGODB_PORT')

print(f"Current time: {datetime.datetime.now()}")

try:
    if username is None or username == '':
        if password is None or password == '':
            mongodb = "mongodb://" + host + ':' + port + "/"
        else:
            mongodb = "mongodb://" + username + '@' + host + ':' + port + "/"
    else:
        mongodb = "mongodb://" + username + ':' + password + '@' + host + ':' + port + "/"
except TypeError:
    print("请先配置MongoDB连接地址！")

try:
    client = pymongo.MongoClient(mongodb)
    db = client[db_name]
    col = db["session"]
    query = {"expiration": {"$lt": datetime.datetime.today()}}
    n = col.delete_many(query)
except (TypeError, NameError, pymongo.errors.ServerSelectionTimeoutError):
    print("连接失败!")
except ValueError:
    print("端口值有误!")
except pymongo.errors.OperationFailure:
    print("验证失败!")
except pymongo.errors.ConfigurationError:
    print("请配置密码!")
else:
    print(n.deleted_count, "个session(s)已清理")
