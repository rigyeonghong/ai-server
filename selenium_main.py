from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_price import get_price
from selenium_title import get_title
from selenium_img import get_img

DRIVER_PATH = "/chromedriver"
options = Options()
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)

url = "https://www.kurly.com/goods/5065323" # 마켓컬리
# url = "https://m.smartstore.naver.com/yongsan/products/7762895541?NaPm=ct%3Dlcefumtc%7Cci%3D4098bec1f843d7e3e0eaeebb2dbccf4d57ad9585%7Ctr%3Dslbrc%7Csn%3D958071%7Chk%3Db15086f2940e945b34c9023fc3eea1adaf9ea118" # 네이버
# url = "https://www.musinsa.com/app/goods/2826643" # 무신사
# url = "https://m.11st.co.kr/products/m/2218563579" # 11번가 (price : x) => bysite
# url = "https://m.coupang.com/vm/products/6335468410?vendorItemId=80524121180&sourceType=HOME_PERSONALIZED_ADS&searchId=feed-8e73a28dd2b1491a8291b0372d0e3ec4-personalized_ads&clickEventId=4b164f80-c05c-4f34-9181-10972e2c1914&isAddedCart="
browser.get(url)

title = get_title(browser, url)
price = get_price(browser)
img = get_img(browser, url)

browser.quit()