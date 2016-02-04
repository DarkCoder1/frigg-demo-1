#/usr/bin/python
# coding: utf-8

from nltk.tokenize import sent_tokenize, word_tokenize
import os, codecs

def get_files():
    """
    Função auxiliar que retorna um array de arquivos. e os paths dos arquivos
    que vão para a tupla.(creio que um loop deve ser criado para esse fim)
    """
    path_name = os.path.abspath('backend')
    #path_name = os.path.abspath('')
    path_files = os.listdir(os.path.abspath(path_name + '/texts/'))
    files = []
    for p in path_files:
        full_path = path_name+'\\texts'+'\\'+p
        content = codecs.open(full_path, "r", "ISO-8859-1") #open(path_name+'\\texts'+'\\'+p)
        #files.append(content)
        files.append((content.name.decode('mbcs')[:-4], content.read()))
        content.close()
    return files

def encode_file(file):
    enc = "ISO-8859-1"
    f = open(file, "r")
    content = f.read() # raw encoded content
    u_content = content.decode(enc) # decodes from enc to unicode
    utf8_content = u_content.encode("utf-8")
    f.close()
    return utf8_content

def create_bag(text):
    paragraph = sent_tokenize(text)
    word_list = []
    for p in paragraph:
        words = word_tokenize(p)
        word_list.append(words)
    return word_list

#  fim do arquivo