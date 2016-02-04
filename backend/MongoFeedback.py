from pymongo import MongoClient
import time, datetime

__author__ = 'Bruno'

class MongoFeedback:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['Frigg-database']
        self.collection = db['userFeedback']

    def gen_date(self):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S')
        return st

    def insert(self, json):
        print 'foi'
        data = {"_id" :self.gen_date(), 'opinion': json['opinion'], 'sugestion': json['sugestion'],
                'rating':json['rating']}
        self.collection.insert(data)

    def search(self, param):
       data = self.collection.find(param)
       results = []
       for d in data:
           results.append(d)
       if results == 0:
           return 0
       else:
           return results