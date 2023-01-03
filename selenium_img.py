from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import shortuuid
from s3_connect import s3_connection, s3_img_upload, s3_get_img_url, default_img

DRIVER_PATH = "/chromedriver"
options = Options()
options = webdriver.ChromeOptions()
options.headless = True
# options.add_argument('headless')
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
# url = "https://m.11st.co.kr/products/m/2218563579" # 11번가
# url = "https://m.coupang.com/vm/products/6335468410?vendorItemId=80524121180&sourceType=HOME_PERSONALIZED_ADS&searchId=feed-8e73a28dd2b1491a8291b0372d0e3ec4-personalized_ads&clickEventId=4b164f80-c05c-4f34-9181-10972e2c1914&isAddedCart="
browser.get(url)

if (url.find("coupang.com") != -1):   
    close_btn = browser.find_element(By.XPATH, '//*[@id="fullBanner"]/div/div/a[2]')
    close_btn.click()
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pdpImages"]/ul/li[1]/img')))

# 쿠팡일 경우
if (url.find("coupang.com") != -1):
    # 1. 이미지 스크래핑
    img_collector = browser.find_element(By.ID, "pdpImages")
    imgs = img_collector.find_elements(By.TAG_NAME, 'img')

else:
    imgs = browser.find_elements(By.CSS_SELECTOR, 'img')

for i in imgs:
    img = i.get_attribute("src")
    if 136 < img.__sizeof__()<= 400:
        break 

#[todo] Img_url에 http,s 가 없는 경우 

# 이미지 스크래핑 안되는 url은 캡처 후 s3에 올려서 이미지 url 생성
if "data:image/svg+xml" in img:
    img = browser.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[1]/img')
    img_id = shortuuid.uuid()
    img.screenshot(f"./capture/kurly.{img_id}.png")
    filename = f"kurly.{img_id}.png"
    
    s3 = s3_connection()
    if s3:
        if s3_img_upload(s3, filename):
            img = s3_get_img_url(filename)
        else: # 이미지 불러오기 및 업로드로 url 요청 실패시 기본 이미지 url 반환
            img = default_img
    else:
        img = default_img

# [todo] capture 폴더 안 이미지 시간되면 삭제할 수 있도록 스케줄링

print("상품 이미지 : ", img)
browser.quit()