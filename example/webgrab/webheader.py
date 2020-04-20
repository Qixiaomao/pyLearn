# -*- coding:utf-8 -*-

import requests

headers={
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
	'Host':'www.santostang.com'
}

key_dict = {'key1':'value1','key2':'value2'}

r = requests.post('http://httpbin.org/post',headers = headers,data=key_dict)
#print ('status code: ', r.status_code)
print (r.text)
