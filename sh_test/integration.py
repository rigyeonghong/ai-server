# 크롬 브라우저 기준
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


# https://sites.google.com/chromium.org/driver/?pli=1
DRIVER_PATH = '../chromedriver'

options = Options()
options = webdriver.ChromeOptions()

# 쿠팡 헤드리스 사용 불가 (막아놓은듯)
options.add_argument('headless')

options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)

# chrome_driver = ChromeDriverManager().install()
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# URL (쿠팡, 네이버, 무신사 순)
# url = 'https://m.coupang.com/vm/products/6552462584?itemId=14634004658&vendorItemId=81875544125' # 쿠팡
url = 'https://m.coupang.com/vm/products/6335468410?vendorItemId=80524121180&sourceType=HOME_PERSONALIZED_ADS&searchId=feed-8e73a28dd2b1491a8291b0372d0e3ec4-personalized_ads&clickEventId=4b164f80-c05c-4f34-9181-10972e2c1914&isAddedCart=' # 쿠팡 2
# url = "https://m.shopping.naver.com/kids/stores/1000016176/products/4847841465?NaPm=ct%3Dlcfs8ykw%7Cci%3D6ae6545058bf0a5b6906fdb0e42605ec5ab66f78%7Ctr%3Dbrc%7Csn%3D203038%7Chk%3Dafd41c17626461775eeac008bf5481009bea4150" # 네이버
# url = "https://www.musinsa.com/app/goods/2926375?loc=goods_rank" # 무신사

driver.get(url)
print(driver.get_window_size())
window_height = driver.get_window_size()['height']


# 모바일 환경 닫기 (추후 예외처리)
if (url.find("coupang.com") != -1):   
    close_btn = driver.find_element(By.XPATH, '//*[@id="fullBanner"]/div/div/a[2]')
    close_btn.click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pdpImages"]/ul/li[1]/img')))


# ## 1. 이미지 스크래핑 == ##
# # 쿠팡일 경우
# if (url.find("coupang.com") != -1):
#     # 1. 이미지 스크래핑
#     img_collector = driver.find_element(By.ID, "pdpImages")
#     imgs = img_collector.find_elements(By.TAG_NAME, 'img')

# # # 그 외의 경우
# else:
#     # 1. 이미지 스크래핑
#     imgs = driver.find_elements(By.TAG_NAME, 'img')
    

# for i in imgs:
#     img = i.get_attribute("src")
#     # print(img)
#     if 136 < img.__sizeof__()<= 400:
#         print("이미지: ", img)
#         break
    


## 2. 텍스트 스크래핑 (meta 활용) ##
title_scrap = False

try:
    meta_title = driver.find_element(By.XPATH, "//meta[@property='og:title']")
    
    if (meta_title != 0):
        title = meta_title
        print("제목 :", title.get_attribute("content"))
        title_scrap = True
except:
    pass


# 2-2. 텍스트 스크래핑 (클래스 활용)
if title_scrap == False:
    try:
        class_title = driver.find_elements(By.XPATH, "//*[contains(@class, 'title')]")
        
        for t in class_title:
            if (t.text != "" and t.location['y'] <= window_height*1):
                title = t.text
                print("제목 :", title)
                title_scrap = True
                break

    except:
        pass
    

## 3. 가격 스크래핑 (meta 활용) ##
# 1) window height 체크
# 2) 텍스트 크기 체크해서
# price_scrap = False


# wons = driver.find_elements(By.XPATH, '//*[contains(@class, "price")]')
# for w in wons:
#     if (w.location['y'] <= window_height) and ("원" in w.text) and (w.text != ""):
#         print("가격: ", w.text)
#         price_scrap = True

# if (price_scrap == False) :
#     wons = driver.find_elements(By.XPATH, '//*[contains(@div, "원")]')
#     for w in wons:
#         if (w.location['y'] <= window_height) and ("원" in w.text) and (w.text != ""):
#             print("가격: ", w.text)


# won = driver.find_element(By.XPATH, f'//*[contains(text(), "원")]/preceding-sibling::span').text

        





# 2. 이미지

# print("이미지: ", img)
# print("할인가: ", discount_price.text)

driver.quit()

