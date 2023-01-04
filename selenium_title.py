import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "/chromedriver"
options = Options()
options = webdriver.ChromeOptions()
# options.headless = True
options.add_argument('headless')
options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)

# url = "https://www.kurly.com/goods/5065323" # 마켓컬리
# url = "https://m.smartstore.naver.com/yongsan/products/7762895541?NaPm=ct%3Dlcefumtc%7Cci%3D4098bec1f843d7e3e0eaeebb2dbccf4d57ad9585%7Ctr%3Dslbrc%7Csn%3D958071%7Chk%3Db15086f2940e945b34c9023fc3eea1adaf9ea118" # 네이버
# url = "https://www.musinsa.com/app/goods/2826643" # 무신사
url = "http://m.11st.co.kr/products/m/1017175152?prdNo=1017175152" # 11번가 # 수정필요
# url = "https://m.coupang.com/vm/products/6335468410?vendorItemId=80524121180&sourceType=HOME_PERSONALIZED_ADS&searchId=feed-8e73a28dd2b1491a8291b0372d0e3ec4-personalized_ads&clickEventId=4b164f80-c05c-4f34-9181-10972e2c1914&isAddedCart="
browser.get(url)

window_height = browser.get_window_size()['height']

if (url.find("coupang.com") != -1):   
    close_btn = browser.find_element(By.XPATH, '//*[@id="fullBanner"]/div/div/a[2]')
    close_btn.click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pdpImages"]/ul/li[1]/img')))


## === title === 
## 2. 텍스트 스크래핑 (meta 활용) ##
title_scrap = False

try:
    meta_title = browser.find_element(By.XPATH, "//meta[@property='og:title']")
    
    if (meta_title != 0 and url.find("11st.co.kr") == -1):
        title = meta_title
        print("제목 :", title.get_attribute("content"))
        title_scrap = True
except:
    pass


# 2-2. 텍스트 스크래핑 (클래스 활용)
if title_scrap == False:
    try:
        if(url.find("11st.co.kr") == -1):
            class_title = browser.find_elements(By.XPATH, "//*[contains(@class, 'title')]")
            
            for t in class_title:
                if (t.text != "" and t.location['y'] <= window_height*1):
                    title = t.text
                    print("제목 :", title)
                    title_scrap = True
                    break

    except:
        pass

if title_scrap == False: 
    try :
        title = browser.find_element(By.CSS_SELECTOR, 'div.dt_title').text # CSS_SELECTOR로 가능 
    except:
        title = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div > div > h2').text
    print("제목 :", title)

browser.quit()