from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = '/chromedriver'
options = Options()
options.headless = True
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

'''
네이버 쇼핑 모바일, 웹, 카탈로그 크롤링 예시 url
'''
# 모바일
url = "https://m.smartstore.naver.com/yongsan/products/7762895541?NaPm=ct%3Dlcefumtc%7Cci%3D4098bec1f843d7e3e0eaeebb2dbccf4d57ad9585%7Ctr%3Dslbrc%7Csn%3D958071%7Chk%3Db15086f2940e945b34c9023fc3eea1adaf9ea118"
# url = "https://m.shopping.naver.com/play/play/stores/1000020568/products/7175898155?NaPm=ct%3Dlcehowm8%7Cci%3Df7077022204e34c7fd7b8a2fba59d157ef31ea31%7Ctr%3Dslsbrc%7Csn%3D205878%7Chk%3Dcce2261dd8c8590cc5e324f5022cbb7e773907c8#REVIEW"
# 웹
# url = "https://smartstore.naver.com/smartinter/products/7574962786?NaPm=ct%3Dlcekxb7c%7Cci%3D4ac9502013df0ea687116a5f07aaad6c4969029d%7Ctr%3Dslsbrc%7Csn%3D6781927%7Chk%3Dccd5fa6ae7f60812834f278e96715e2f5c1c8a28"
# 모바일 카탈로그
# url = "https://msearch.shopping.naver.com/catalog/34161823619?NaPm=ct%3Dlcehnyo0%7Cci%3De4dcdec1a4ab478017f40e172e84e81c301fd39c%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D01970cd757f67828342377cf9e6802d7a70d3630&cat_id=50002932&frm=NVSCDIG&purchaseConditionSequence=20166681&query=%ED%95%9C%EC%84%B1%20%ED%82%A4%EB%B3%B4%EB%93%9C&sort=LOW_PRICE"

browser.get(url)

try: 
    name = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/span').text
except:
    try: name = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div[2]/h3').text
    except: name = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/h2').text

try: 
    price = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div/span[2]').text
except:
    try: price = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div[1]/div[3]/div[2]/div/div[2]/div/span[2]').text
    except: price = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div/div[1]/div[2]/span[1]/em').text
                                            

try:
    img = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]/div/img').get_attribute("src")
except:
    try: img = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/img').get_attribute("src")
    except: img = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/div/div[2]/img').get_attribute("src")

print("상품 이름 : ", name)
print("가격 : ", price)
print("이미지 : ", img)
browser.quit()