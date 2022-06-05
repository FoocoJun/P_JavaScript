from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://HAJUN:9965@cluster0.oudgkww.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name = request.form['name_give'].strip()
    comm = request.form['comm_give'].strip()
    print(name,comm)

    if not name:
        return jsonify({'msg': '닉네임을 남겨주세요!'})
    elif not comm:
        return jsonify({'msg': '응원댓글을 남겨주세요!'})
    else:
        doc = {
            'name':name,'comment':comm
        }
        db.fans.insert_one(doc)
        return jsonify({'msg':'응원을 남겼습니다!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    all_fans = list(db.fans.find({}, {'_id': False}))
    return jsonify({'fans':all_fans})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)