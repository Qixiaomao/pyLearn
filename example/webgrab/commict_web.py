# -*- coding:utf-8 -*-

import requests
import json

link = 'https://api-zero.livere.com/v1/comments/list?callback=jQuery112406923952663074842_1587283471192&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1587283471194'

headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
	'Host':'movie.douban.com'
}

r = requests.get(link,headers = headers)
json_data = json.loads(r.text)
com_list = json_data['regdate']['content']

for eachone in com_list:
       message = com_list[eachone]['comment']
       print (message)

