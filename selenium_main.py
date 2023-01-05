from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_price import get_price
from selenium_title import get_title
from selenium_img import get_img
from flask import jsonify
from elevenst import elevenst_get_info

DRIVER_PATH = "/chromedriver"
options = Options()
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")
options.add_argument('--disable-blink-features=AutomationControlled')
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)


def web_scrap(url): 
    browser.get(url)
    if (url.find("11st.co.kr") != -1): # 11번가
        return elevenst_get_info(browser)
    else: 
        title = get_title(browser, url)
        price = get_price(browser)
        img = get_img(browser, url)

    return jsonify({'url': url, 'title': title, 'price': price, 'img': img})