import json
from flask import Flask, request
from selenium_main import web_scrap
from machine_learning import categorization
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello sendwish web scrapper!'

@app.route('/webscrap', methods=['POST'])
def webscrap():
    data = request.get_json()
    url_receive = data['url'][0]
    print("url", url_receive)
    # [todo] 예외처리 필요
    print("===Start Scraping===")
    product = web_scrap(url_receive)
    
    print("===Start categorization===")
    if product.img != "https://sendwish-img-bucket.s3.ap-northeast-2.amazonaws.com/default_image.png":
        category = categorization(product.img)
    else: category = "etc"
    
    result = jsonify({'url': product.url, 'title': product.title, 'price': product.price, 'img': product.img, 'category' : category})
    return result

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

# 실행 명령어
# gunicorn app:app -b 0.0.0.0:5000 -w 2 --timeout=360 -k gevent 