from flask import Flask, request
from selenium_main import web_scrap
from machine_learning import categorization

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
    result = web_scrap(url_receive)
    print("===Start categorization===")
    category = categorization(result['img'])
    result['category'] = category
    return result

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)

# 실행 명령어
# gunicorn app:app -b 0.0.0.0:5000 -w 2 --timeout=360 -k gevent 