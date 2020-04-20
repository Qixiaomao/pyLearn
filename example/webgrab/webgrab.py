# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup


link = "http://www.santostang.com/2018/07/14/4-2-%e8%a7%a3%e6%9e%90%e7%9c%9f%e5%ae%9e%e5%9c%b0%e5%9d%80%e6%8a%93%e5%8f%96/"

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1;en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

r = requests.get(link, headers = headers)

#解析代码
soup = BeautifulSoup(r.text,'lxml')
title = soup.find('h1',class_ = 'view-title').a.strip()
print (title)

#存取数据
with open('title.txt',"a+") as f:
	f.write(title)
	f.close()
