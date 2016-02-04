#/usr/bin/python
# coding: utf-8

from bs4 import BeautifulSoup
import requests
import re, os

__author__ = 'Bruno'

def gen_url(url, base_words, n):
    for base in base_words:
        n_url = url + base
        links = trade_spider(n_url)
        get_data(links, n)

def trade_spider(url):
    l = []
    #url = 'https://pt.wikipedia.org/wiki/Economia'
    source = requests.get(url)
    plain = source.text
    soup = BeautifulSoup(plain)
    main_content = soup.find('div', {'class':'mw-body-content'})
    for link in main_content.find_all('a', href = True):
        if re.match('/wiki/',link['href']):
            if link['href'].find(':') == -1:
                href = 'https://pt.wikipedia.org'+link.get('href')
                l.append(href)
    urls = list(set(l))
    #return urls.append(url)
    urls.append(url)
    #get_data(urls)
    return urls

def get_data(links, n):
    for l in links[:n]:
        print l
        source = requests.get(l)
        plain = source.text
        soup = BeautifulSoup(plain)
        text = soup.find('div',{'class':'mw-body-content'})
        #print type(text)
        p_tags = text.find_all('p')
        #print len(p_tags)
        title = soup.find('title').text
        save(title, p_tags)

def save(name, paragraphs):
    text = '\n'.join(str(p.text.encode('utf-8')) for p in paragraphs)
    path = os.path.abspath('texts')
    if name.find('/'):
        name = name.replace('/', '-')
    archive = open(path+'\\'+ name+'.txt', 'w')
    archive.write(text)
    archive.close()

#links = trade_spider()

base = ['Ciência_da_computação', 'Economia', 'Ciência','Física', 'Quimica','Biologia','Engenharia','Universo','Brasil',
        'Geografia','Arte','Filosofia']

gen_url('https://pt.wikipedia.org/wiki/',base,110)