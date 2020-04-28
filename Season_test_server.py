from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('season.html')


# API 역할을 하는 부분.
@app.route('/drinks', methods=['GET'])
def read_drinks():
    # 1. DB에서 리뷰 정보 모두 가져오기
    drinks = list(db.drinks.find({}, {'_id': 0}))
    # 2. 성공 여부 & 리뷰 목록 반환하기
    return jsonify({'result': 'success', 'drinks': drinks})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
