'''
import urllib
from xml.etree import ElementTree
import re

url = 'http://elpuntvalles.com/index.php?lang=es'
xmldata = '<root>' + urllib.urlopen(url).read() + '</root>'
re.sub(r'&', '&amp;', xmldata)
tree = ElementTree.fromstring(xmldata)
codigo = tree.find('codigo').text

print codigo
'''

import urllib2
import re
import json

file = urllib2.urlopen('http://elpuntvalles.com/index.php?lang=es')
data = file.read()
data.replace(" ", "")
data.replace("\t", "")
file.close()


def get_urls_from_mainpage(data):
    index_ref = [m.start() for m in re.finditer('mix 2', data)]

    res = list()

    for i in index_ref:
        str =  data[i:i+200]
        cad_i = "href="
        cad_j = "><img"
        i = str.index(cad_i)
        j = str.index(cad_j)
        res.append(str[i+len(cad_i)+1:j-1])

    return res

def get_data_from_urlfilm(urls):

    res = list()
    for url in urls:
        print url
        film = dict()
        data = get_data_from_url('http://elpuntvalles.com/'+url)

        #Get Img
        img_url_index = data.index("art-fullimg span2")
        img_url_1 = data[img_url_index:img_url_index+300]
        sub_index = img_url_1.index("<img")
        img_url_2 = img_url_1[sub_index:sub_index+250]
        img_url_i = img_url_2.index("src=")
        img_url_j = img_url_2.index("alt=")
        img_url = img_url_2[img_url_i+5:img_url_j-2]
        #print img_url

        #Get Title
        title_index = [m.start() for m in re.finditer('page-header', data)][1]
        title_1 = data[title_index:title_index+500]
        sub_index = title_1.index("<a")
        title_2 = title_1[sub_index:sub_index+300]
        title_i = title_2.index(">")
        title_j = title_2.index("</a>")
        title = title_2[title_i+1:title_j]
        #print title

        film["title"] = title.lstrip()
        film["url"] = 'http://elpuntvalles.com/'+img_url
        res.append(film)

    return res

def get_data_from_url(url):
    file = urllib2.urlopen(url)
    data = file.read()
    data.replace(" ", "")
    data.replace("\t", "")
    file.close()

    return data

urls = get_urls_from_mainpage(data)
res = get_data_from_urlfilm(urls)
print json.dumps(res)