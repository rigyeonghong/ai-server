from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import shortuuid
from s3_connect import s3_connection, s3_img_upload, s3_get_img_url

DRIVER_PATH = "/chromedriver"
options = Options()
options.headless = True
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

url = "https://www.kurly.com/goods/5065323" # 마켓컬리
# url = "https://m.smartstore.naver.com/yongsan/products/7762895541?NaPm=ct%3Dlcefumtc%7Cci%3D4098bec1f843d7e3e0eaeebb2dbccf4d57ad9585%7Ctr%3Dslbrc%7Csn%3D958071%7Chk%3Db15086f2940e945b34c9023fc3eea1adaf9ea118" # 네이버
# url = "https://www.musinsa.com/app/goods/2826643" # 무신사
# url = "https://m.11st.co.kr/products/m/2218563579" # 11번가
browser.get(url)

imgs = browser.find_elements(By.CSS_SELECTOR, 'img')
for i in imgs:
    img = i.get_attribute("src")
    if 136 < img.__sizeof__()<= 400:
        break 

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
        else: # [todo] 이미지 불러오기 및 업로드로 url 요청 실패시 기본 이미지 url 반환
            img = "default_img"
    else:
        img = "default_img"

# [todo] capture 폴더 안 이미지 시간되면 삭제할 수 있도록 스케줄링

print("상품 이미지 : ", img)
browser.quit()