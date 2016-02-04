#/usr/bin/python
# coding: utf-8

from nltk.stem import RSLPStemmer
#from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
import re

class Heuristics:
    """
    classe que na verdade é apenas uma estrutura de dados para guardar os 
    pipparágrafos.
    """
    heuristic_data = {}

    def add_data(self, key, data):
        if self.heuristic_data.has_key(key):
            if data not in self.heuristic_data[key]:
                self.heuristic_data[key].append(data)
        else:
            self.heuristic_data.update({key:[data]})
        #print self.heuristic_data[key]

    def search_biggest(self):
        print self.heuristic_data
        if len(self.heuristic_data) > 0:
            return max(self.heuristic_data)

class Search:
    heu = Heuristics()
    """
    classe que realiza as operações de NLP.
    """
    def search(self, key_word, files):
        if files == -1:
            return 0
        """
        método que será usado "lá fora". ja está otimizado e não dá mais o 
        "first match"
        """
        i = 0
        self.heu.heuristic_data = {}
        print len(files)
        for paragraph in files:
            list_words = word_tokenize(paragraph)
            k = 0 # conta palavras chave detectadas
            for key in key_word:
                for word in list_words:
                    calc = self.compare(word, key[0])
                    if calc > 0: # se o calculo da heuristica ocorreu...
                        i += calc #acumula o valor
                        k += 1
                        break
            if k == len(key_word):
                self.heu.add_data(i, paragraph)
            i = 0
        data = self.heu.search_biggest()
        if data is not None or data != None:
            p = self.heu.heuristic_data[data]
            return p
        else:
            return 0

    def compare(self, word, key):
        """
        Metodo que faz comparações para definir se uma palavra é igual, possui o mesmo radical ou se é similar a outra.
        verificar encoding (ueff/) isso está fazendo com que falhe no radical(Na verdade, desde o começo).
        :rtype : object
        """
        if word == key or word.lower() == key.lower():
            return 0.5
            print 'foi até aqui'
        else:
            stemmer = RSLPStemmer()
            tok = stemmer.stem(key)
            if re.match(tok, word[0]):
                return 0.3
            '''syn = self.isSyn(key, word)
            if syn > 0:
                return syn * 0.2'''
        return 0

    def search_file(self, keys, arch):
        for paragraph in arch:
            i = 0
            for k in keys:
                for word in paragraph:
                    if k[0] == word:
                        i += 1
                    stemmer = RSLPStemmer()
                    tok = stemmer.stem(k[0])
                    if re.match(tok, word):
                        i += 1
                if i >= len(keys):
                    return paragraph
            i = 0
        return u"Me desculpe, mas não sei"

