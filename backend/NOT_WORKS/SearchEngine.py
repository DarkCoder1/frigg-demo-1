#/usr/bin/python
# coding: utf-8

__author__ = 'Bruno'

from nltk.tokenize import sent_tokenize, word_tokenize
from pickle import load, dump
#from tagger import Tagger
import os, re

class SearchEngine:
    """
    classe que considero a principal desse modulo. É a estrutura de dados que
    contém os arquivos para o processamento da engine.
    """
    def __init__(self, load):
        #  código para carregar o pickle
        self.search_data = {}
        if load is True:
            self.load_data()
        #  carregando o tagger
 #       self.tagger = Tagger('portugues')

    def save(self):
        output = open('data.pkl', 'wb')
        dump(self.search_data, output)
        output.close()

    def insert(self, files):
        """
        Esse método tem como entrada um array de arquivos e uma tupla de path e
        retorna uma lista de indexação reversa.
        """
        for f in files:
            p_count = -1
            paragraph = sent_tokenize(f[1].read().decode('utf-8').lower())
            for p in paragraph:
                p_count +=1
                words = word_tokenize(p)
                classes = self.tagger.classify(words)
                for c in classes:
                    if re.match('N', c[1]):
                        if self.search_data.has_key(c[0]):
                            names = [n for n,_ in self.search_data[c[0]]]
                            if os.path.basename(f.name) in names:
                                self.search_data[c[0]][names.index(os.path.basename(f[0]))][1].append(p_count)
                            else:
                                self.search_data[c[0]].append(((os.path.basename(f[0])),[p_count]))
                        else:
                            self.search_data.update({c[0]:[((os.path.basename(f[0])),[p_count])]})
        self.save()

    def search(self, name):
        """
        Algoritmo de busca simples que retorna um tupla com os arquivos.
        """
        if name in self.search_data:
            files = self.search_data[name]
            path_name = os.path.abspath('backend')
            text_files = []
            if files is not None:
                for f in files:
                    text = open(path_name+'\\texts\\'+f[0]).read().decode('utf-8-sig')
                    #  tokenização
                    text_sent = sent_tokenize(text)
                    for i in f[1]:
                        element = text_sent[i] #  modificado aqui
                        text_files.append(element)
            return set(text_files)
        else:
            return None

    def load_data(self):
        """
        função simples para carregar o arquivo
        """
        path = os.path.abspath('backend')+'/pickle/'
     #   path = os.path.abspath('pickle')+'\\'
        input_data = open(path + 'data.pkl')
        self.search_data = load(input_data)
        input_data.close()
