from flask import Flask, render_template, jsonify, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 을 주는 부분
@app.route('/')
def home():
    return render_template('Main.html')


@app.route('/spring')
def get_spring():
    return render_template('spring.html')


@app.route('/summer')
def get_summer():
    return render_template('summer.html')


@app.route('/autumn')
def get_autumn():
    return render_template('autumn.html')


@app.route('/winter')
def get_winter():
    return render_template('winter.html')


# API 역할을 하는 부분.
# DB에 저장되어 있는 음료 정보를 불러옴.
@app.route('/drinks', methods=['GET'])
def read_drinks():
    drinks = list(db.drinks.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'drinks': drinks})


if __name__ == '__main__':
    app.run('localhost', port=5000, debug=True)
