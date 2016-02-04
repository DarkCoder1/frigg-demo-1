#/usr/bin/python
# coding: utf-8

from pymongo import MongoClient
import time, datetime

__author__ = 'Bruno'

class MongoUser:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['Frigg-database']
        self.collection = db['userInfo']

    def gen_date(self):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        return st

    def insert(self, question, para):
        data = {"_id" :self.gen_date(), 'question': question, 'numPara': para}
        self.collection.insert(data)

    def search(self, date, time):
       data = self.collection.find(date + ' ' + time)
       results = []
       for d in data:
           results.append(d)
       if results == 0:
           return 0
       else:
           return results