from pymongo import MongoClient
client = MongoClient('mongodb+srv://HAJUN:9965@cluster0.oudgkww.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

user = db.movies.find_one({'title':'가버나움'},{'star'})
print(user['star'])


same = list(db.movies.find({'star':user['star']},{'title'}))

for i in same:
    print(i['title'])

db.movies.update_one({'title':'극장판 바이올렛 에버가든'},{'$set':{'rank':"10"}})