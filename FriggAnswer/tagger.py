from pickle import load
from nltk.tag import BigramTagger, UnigramTagger, DefaultTagger
import os

class Tagger:

    def __init__(self, idiom):
        self.tagger0 = DefaultTagger('N')
        self.tagger1 = UnigramTagger(None, self.tagger0)
        self.tagger2 = BigramTagger(None, self.tagger1)
        self.lang = os.path.abspath('FriggAnswer')+'/pickle/'
        #self.lang = os.path.abspath('pickle')+'\\'
        self.loadIdiom(idiom)

    def loadIdiom(self, idiom):
        input = open(self.lang +idiom +'1.pkl', 'rb')
        self.tagger = load(input)
        input.close()
        input = open(self.lang +idiom+'2.pkl', 'rb')
        self.tagger2 = load(input)
        input.close()

    def classify(self, question):
        tags = self.tagger2.tag(question)
        return tags

