#/usr/bin/python
# coding: utf-8

from django.db import models

from inference import Search
from question import Question
from backend.backend_interface import *
from backend.utils import *
from messages import return_message, error_message
from backend.MongoUserInfo import MongoUser

question = Question()
inferencer = Search()
user = MongoUser()

def answer(perg):
    key = question.genKeyWords(perg)
    files = retrieve(key)
    if files is None:
        return u"Eu não tenho ideia!"
    else:
        data_title = retrieve_by_filename(key)
        res_t = inferencer.search(key, data_title)
        if res_t == 0:
            data_file = retrieve_equal_files(key)
            res_f = inferencer.search(key, data_file)
            if res_f == 0:
                data_commom = retrieve_commom(key)
                res_c = inferencer.search(key, data_commom)
                if res_c == 0:
                    return error_message()
                else:
                    user.insert(perg, len(res_c))
                    return return_data(res_c)
            else:
                user.insert(perg, len(res_f))
                return return_data(res_f)
        else:
            user.insert(perg, len(res_t))
            return return_data(res_t)


def answer_file(perg, file):
    if perg == "" or perg is None or len(perg) <=2:
        return u"Escreva algo para que eu possa responder!"
    key = question.genKeyWords(perg)
    arch = create_bag(file.read().decode('utf-8-sig'))
    res = inferencer.search_file(key, arch)
    return return_data_files(res)

def get_best_files(paragraphs):
    if len(paragraphs) == 1:
        return paragraphs
    elif len(set(paragraphs)) != len(paragraphs):
        para = [p for p in paragraphs if paragraphs.count(p) > 1]
        return list(set(para))
    else:
        return paragraphs

def return_data(result):
    message = u''+return_message()
    for r in result:
        message += "\n\n" +'<p>'+ r + '</p>'
    return message

def return_data_files(result):
    message = u''+return_message()
    message += "\n\n" + ' '.join(result)
    return message