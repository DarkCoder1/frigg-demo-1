#/usr/bin/python
# coding: utf-8

from nltk.tokenize import sent_tokenize, word_tokenize
from tagger import Tagger
import numpy as np
import h5py, re

__author__ = 'Bruno'

tagger = Tagger('portugues')

def insert(file):
    ds = h5py.File('Dataset', 'w')
    paragraph = sent_tokenize(file[1])
    p_count = -1
    for p in paragraph:
        p_count += 1
        words = word_tokenize(p)
        classes = tagger.classify(words)
        for c in classes:
            if re.match('N',c[1]):
                if c[0] in ds.keys():
                    if file[0] in ds[c[0]].attrs['filename']: #se a palavra já está armazenada e está no mesmo arquivo:
                        index = ds[c[0]].attrs['filename'].index(file[0])
                        ds[c[0]].attrs['paragraphs'][index].append(p_count) #anexar indice do paragrafo
                    ds.attrs['filename'].append(file[0]) # apenas anexa um nome e um array novo.
                    ds.attrs['paragraphs'].append(p_count)
                ds[c[0]].attrs['filename'].append(file[0])
                ds[c[0]].attrs['paragraph'] = np.array([[p_count]])


def search(key):
    ds = h5py.File('Dataset','r')
    texts = []
    if key in ds.keys():
        files = ds[key]
        for f in files:
            text = open(f[0])
            paragraphs = sent_tokenize(text)
            del(f[0])
            for count in f:
                sent = paragraphs[count]
                texts.append(sent)
        ds.close()
        return set(texts)
    ds.close()
    return None
'''
ds = h5py.File('Dataset', 'w')
ds['isso'] = [2,3,4]
ds['como'] = 'teste.txt'
ds['pode'] = np.array([[0,1,4],[0,1,3]])
#ds['aconteceu'] = np.array([['a.txt',[0,1]],['b.txt',[2,3,4]],['c.txt',[5,6,7,8]]])
ds['aconteceu'] = np.array([['isso',0],['no',0.76]])
ds.close()

tes = h5py.File('Dataset', 'r')
a = tes['isso']
print a[0]

b = tes['pode']
print b[0]
#b = np.array([[0,1,4],[0,1,3]])

c = tes['aconteceu']
print c[1]
#print b

d = tes.keys()
print d

tes.close()
'''

a = np.array([1])
print a
a = np.append([a], [[2]], axis = 0)
print a
#a = np.insert(a[0], 0, 0)
#print a
a = np.append(a,[[3]], axis = 0)
print a
a = np.append(a, [[4,5]], axis = 0)
#a = np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]], axis = 0)
print len(a)
print a.shape
print a