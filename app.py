from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('homework_week4_wooseok.html')

## API 역할을 하는 부분
@app.route('/orders', methods=['POST'])
def write_order():
    title_name = request.form['name_give']
    title_amount = request.form['amount_give']
    title_address = request.form['address_give']
    title_phone = request.form['phone_give']

    order = {
        'name': title_name,
        'amount': title_amount,
        'address': title_address,
        'phone': title_phone
    }

    db.orders.insert_one(order)
    return jsonify({'result':'success', 'msg': '주문이 정상적으로 요청되었습니다'})


@app.route('/orders', methods=['GET'])
def read_reviews():
    orders = list(db.orders.find({},{'_id':0}))
    return jsonify({'result':'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)