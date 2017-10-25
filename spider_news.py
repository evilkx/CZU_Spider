# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

f = open("C:\\Users\Administrator\Desktop\\news.html", 'w')
back = '<body bgcolor="#d0d0d0">'
img = '<img src="D:\\1.jpg" align="right" right-padding="200dp">'
f.write(back)
f.write(img)
line = '---------------------------------------------------------------------------------'
home = '<h1>学校主页新闻</h1>'
jwc = '<h1>教务处新闻</h1>'
ops_home = '<h1>主页君去月球了...</h1>'
ops_jwc = '<h1>教务君去三体世界了...</h1>'

def home_get():
    url_home = requests.get("http://www.czu.cn/s/21/t/28/p/100/i/1/list.htm")
    response_home = url_home.text
    soup_home = BeautifulSoup(response_home, 'html.parser')
    f.write(home)
    for a in soup_home.find_all('a', target="_blank", limit=22):
        # print(a)
        url = "http://www.czu.cn" + a["href"]
        text = '<a href = ' + url + ' target="_blank">' + '<h3>' + a.string + '</h3>' + '</a>'
        f.write(text)

def jwc_get():
    url_jwc = requests.get("http://jwc.czu.cn/s/48/t/443/p/21/list.htm")
    response_jwc = url_jwc.text
    soup_jwc = BeautifulSoup(response_jwc, 'html.parser')
    f.write(jwc)
    for a in soup_jwc.find_all('a', target="_blank", limit=14):
        # print(a)
        url = "http://jwc.czu.cn" + a["href"]
        text = '<a href = ' + url + ' target="_blank">' + '<h3>' + a.string + '</h3>' + '</a>'
        f.write(text)

try:
    home_get()
except:
    f.write(ops_home)
f.write(line)
try:
    jwc_get()
except:
    f.write(ops_jwc)
f.close()
