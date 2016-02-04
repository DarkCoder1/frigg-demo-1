#/usr/bin/python
# coding: utf-8

# mude depois para SearchEngine caso funcione!

__author__ = 'Bruno'

from nltk.tokenize import sent_tokenize, word_tokenize
from tagger import Tagger
import os, re

class SearchEngine:
    """
    classe que considero a principal desse modulo. É a estrutura de dados que
    contém os arquivos para o processamento da engine.
    """

    def __init__(self):
        self.tagger = Tagger('portugues')

    def insert(self, files):
        """
        Esse método tem como entrada um array de arquivos, retornando uma lista de indexação reversa.
        """
        dataset = []
        for f in files:
            paragraph = sent_tokenize(f[1].lower())
            for index, p in enumerate(paragraph):
                words = word_tokenize(p)
                classes = self.tagger.classify(words)
                for c in classes:
                    if re.match('N', c[1]):
                        keysId = [item['_id'] for item in dataset]
                        print 'qtd chaves: ' + str(len(keysId))
                        if c[0] in keysId:
                            ind = keysId.index(c[0])
                            files = dataset[ind]
                            if os.path.basename(f[0]) in files.keys():
                                if not index in dataset[ind][os.path.basename(f[0])]:
                                    dataset[ind][os.path.basename(f[0])].append(index)
                            else:
                                dataset[ind][os.path.basename(f[0])] = [index]
                        else:
                            dataset.append({'_id':c[0], os.path.basename(f[0]):[index]})
        return dataset

    def extract(self, data):
        """
        Algoritmo de busca simples que retorna um tupla com os arquivos.
        """
        print 'vim pelo método extract'
        for d in data:
            paragraphs = []
            try:
                d.pop('_id')
            except KeyError:
                'ok'
            for k in d.keys(): # o [1:] para eliminar a primeira chave!
                #path_name = os.path.abspath('backend')
                path_name = os.path.abspath('backend') + '/texts/'
                #text = open(path_name+'\\texts\\'+ k + '.txt').read().decode('utf-8')
               # print path_name+'\\'+ k + '.txt'
                text = open(path_name+ k + '.txt').read().decode('utf-8')
                text_sent = sent_tokenize(text)
                for index in d[k]:
                    paragraphs.append(text_sent[index])
        print paragraphs
        return set(paragraphs)
        #return paragraphs
