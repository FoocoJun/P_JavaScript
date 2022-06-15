from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://HAJUN:9965@cluster0.oudgkww.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    all_buckets = list(db.buckets.find({}, {'_id': False}))
    count =len(all_buckets) +1

    doc = {
        'num':count,
        'bucket':bucket_receive,
        'done':0
    }

    db.buckets.insert_one(doc)

    return jsonify({'msg': '버킷 기록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    number_receive = request.form['number_give']
    db.buckets.update_one({'num':int(number_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '버킷 완료!'})

@app.route("/bucket/cancle", methods=["POST"])
def bucket_cancle():
    number_receive = request.form['number_give']
    db.buckets.update_one({'num':int(number_receive)},{'$set':{'done':0}})
    return jsonify({'msg': '취소되었습니다.'})

@app.route("/bucket/comp", methods=["POST"])
def bucket_comp():
    number_receive = request.form['number_give']
    date_receive = request.form['date_give']
    comment_receive = request.form['comment_give']

    if not date_receive:
        return jsonify({'msg': '날짜를 입력해주세요!'})
    elif not comment_receive:
        return jsonify({'msg': '후기를 남겨주세요!'})
    else:
        db.buckets.update_one({'num':int(number_receive)}, {'$set': {'done':2}})
        db.buckets.update_one({'num':int(number_receive)}, {'$push': {'date': date_receive}})
        db.buckets.update_one({'num':int(number_receive)}, {'$push': {'comment': comment_receive}})
        return jsonify({'msg': '등록 완료!'})

@app.route("/bucket", methods=["GET"])
def bucket_get():
    all_buckets = list(db.buckets.find({}, {'_id': False}))
    return jsonify({'all_buckets':all_buckets})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)