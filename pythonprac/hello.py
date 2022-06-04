import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://HAJUN:9965@cluster0.oudgkww.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

#old_content > table > tbody > tr:nth-child(2) > td.title > div > a

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

movies =soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')
    b = movie.select_one('td:nth-child(1) > img')
    c = movie.select_one('td.point')
    if a != None:
        title = a.text
        rank = b['alt']
        star = c.text
        print(rank, title, star)
        doc = {
            'title':title,
            'rank':rank,
            'star':star
        }
