import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://steamcommunity.com/profiles/76561198083882978/myworkshopfiles/?appid=0&sort=score&browsefilter=myfavorites&view=imagewall&p=1&numperpage=30',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

modes =soup.select('#leftContents > div.workshopBrowseItems > div')

#leftContents > div.workshopBrowseItems > div:nth-child(1) > a.item_link

for mode in modes:
    name = mode.select_one('a.item_link').get('href')
    mode_id = name.split('id=')[1]
    mode_title = mode.select_one('a.item_link').text

    print(mode_title,':',mode_id)