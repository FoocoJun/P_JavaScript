from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('mongodb+srv://HAJUN:9965@cluster0.oudgkww.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/movie", methods=["POST"])
def movie_post():
    movie_receive = request.form['url_give']
    star_receive = request.form['star_give']
    com_receive = request.form['com_give']

    url = movie_receive
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get(url, headers=headers)
        soup = BeautifulSoup(data.text, 'html.parser')

        title = soup.select_one('meta[property="og:title"]')['content']
        image = soup.select_one('meta[property="og:image"]')['content']
        desc = soup.select_one('meta[property="og:description"]')['content']

        doc = {'title': title, 'image': image, 'desc': desc, 'star': star_receive, 'comment': com_receive}
        db.movies_review.insert_one(doc)
    except:
        return jsonify({'msg': '유효한 네이버 영화 URL을 입력하세요.'})

    return jsonify({'msg': '영화 기록 완료!'})


@app.route("/movie", methods=["GET"])
def movie_get():
    all_movies = list(db.movies_review.find({},{'_id':False}))

    return jsonify({'movies': all_movies})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
