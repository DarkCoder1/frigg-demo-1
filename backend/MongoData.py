#/usr/bin/python
# coding: utf-8

__author__ = 'Bruno'

from pymongo import MongoClient
#from bson import BSON
#import bson

"Teste passou que é uma beleza! Vamos iniciar os testes nessa porra!"

__author__ = 'Bruno'

class MongoConn:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        db = client['Frigg-database']
        self.collection = db['Frigg']

    def multi_insert(self, data):
        #item = BSON.encode(data)
        self.collection.insert(data)

    def search(self, keys):
        doc = []
        for k in keys:
            data = self.collection.find_one({'_id':k[0]})
            if data is not None:
                doc.append(data)
        return doc

'''
for document in doc: #bagulho é bixão mesmo morô cara? já vem como array de dict porra, morô?
    print document
'''