from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_price import get_price
from selenium_title import get_title
from selenium_img import get_img
from flask import jsonify
from elevenst import elevenst_get_info

DRIVER_PATH = "/app/chrome/chromedriver"
options = Options()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)

class Product:
    def __init__(self):
        self.url = ""
        self.title = ""
        self.price = 0
        self.img = ""
        self.category = ""

def web_scrap(url): 
    try :
        browser = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
        if (url.find("musinsaapp") != -1): # 무신사 앱링크면
            url += "?_imcp=1"
        browser.get(url)
        if (url.find("11st.co.kr") != -1): # 11번가
            return elevenst_get_info(browser)
        else: 
            title = get_title(browser, url)
            print("title", title)
            price = get_price(browser)
            print("price", price)
            img = get_img(browser, url)
            print("img", img)
        print("===Finish Scraping===")
        
        print("===Finish Scraping===")
        product = Product()
        product.url = url
        product.title = title
        product.price = price
        product.img = img
        return product
        # return jsonify({'url': url, 'title': title, 'price': price, 'img': img})
    except :
        print("===SCRAP ERROR===")
        product = Product()
        product.url = url
        product.title = '사이트로 이동하기'
        product.price = '-'
        product.img = 'https://sendwish-img-bucket.s3.ap-northeast-2.amazonaws.com/collection_default.png'
        return product
        
        # return jsonify({'url': url, 'title': '사이트로 이동하기', 'price': '-', 'img': 'https://sendwish-img-bucket.s3.ap-northeast-2.amazonaws.com/collection_default.png'})