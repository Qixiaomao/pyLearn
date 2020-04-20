# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
import os


def get_movies():
    headers = {
	'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
	'Host':'movie.douban.com'
}
    movie_list = []
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start='+str(i *25)
        r=requests.get(link,headers=headers,timeout=10)
        print(str(i+1),"status code:",r.status_code)

        soup = BeautifulSoup(r.text,'lxml')
        div_list = soup.find_all('span', class_='rating_num')
        for each in div_list:
                movie = each.text.strip() #这部分的代码还不是很清楚具体意思；
                movie_list.append(movie)
    return movie_list



if __name__ == "__main__":
    movies = get_movies()
    #with open('douban250_en.csv','ab+') as openfile:
        #openfile.write(codecs.BOM_UTF8)
    with open('douban250_stars.csv','a+',encoding='utf-8-sig',errors='ignore',newline='') as csvfile:
        csvw = csv.writer(csvfile)
        csvw.writerow(movies)
