#coding:utf8
from pymongo import MongoClient

class MG:
    def __init__(self):
        #建立连接
        uri = 'mongodb://127.0.0.1:27017/'
        self.client = MongoClient(uri)
        # self.client = MongoClient("localhost", 27017)
        self.db = self.client.zhihu