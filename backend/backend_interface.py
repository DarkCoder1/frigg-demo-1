#/usr/bin/python
# coding: utf-8

from utils import get_files
from TextDAO import SearchEngine
#from Crawler import *
from MongoData import MongoConn

__author__ = 'Bruno'

def get_data():
    a = get_files()
    se = SearchEngine()
    data = se.insert(a) # mais de 1000!
    return data

def save(data):
    con = MongoConn()
    con.multi_insert(data)

def search_base(keys):
    con = MongoConn()
    result = con.search(keys)
    return result

#items = get_data()

#save(items)

def retrieve(words):
    dataset = search_base(words)
    return dataset

def retrieve_by_filename(words):
    se = SearchEngine()
    opt_data = {}
    dict_list = retrieve(words)
    if dict_list > 0:
        for data in dict_list:
            k = data['_id']
            data.pop('_id')
            for d in data.keys():
                if k in d.lower():
                    opt_data[d] = data[d]
        if opt_data > 0:
            keys = opt_data.keys()
            print 'valor de k: ' + str(len(keys))
            print opt_data
            return se.extract([opt_data])
        else:
            return -1
    else:
        return -1

def retrieve_commom(words):
    se = SearchEngine()
    dataset = search_base(words)
    paragraphs = se.extract(dataset)
    return paragraphs

def retrieve_equal_files(words):
    se = SearchEngine()
    opt_data = {}
    dict_list = retrieve(words)
    if dict_list > 0:
        for d in dict_list:
            for k, v in d.items ():
                if k not in opt_data:
                    opt_data[k] = []
                else:
                    opt_data[k].append(v)
        if opt_data > 0:
            return se.extract([opt_data])
        else:
            return -1
    else:
        return -1