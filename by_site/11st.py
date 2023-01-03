from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "/chromedriver"
options = Options()
options.headless = True
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)
browser = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

# url = "https://m.11st.co.kr/products/m/4700403909?prdNo=4700403909"
url = "https://m.11st.co.kr/products/m/2218563579"
# url = "https://m.11st.co.kr/products/ma/3690859819?prdNo=3690859819" # 11번가 내부 아마존 제품
browser.get(url)

try :
    name = browser.find_element(By.CSS_SELECTOR, 'div.dt_title').text # CSS_SELECTOR로 가능 
    # name = browser.find_element(By.XPATH, '//*[@id="cts"]/div[2]/div[2]/div[3]/h1').text # XPATH로 가능
except:
    name = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div > div > h2').text
    # name = browser.find_element(By.XPATH, '//*[@id="cts"]/div[1]/div[3]/div/div/h2').text

try :
    price =  browser.find_element(By.CSS_SELECTOR, 'div.price > span > b').text
    # price = browser.find_element(By.XPATH, '//*[@id="priceLayer"]/div[2]/span/b').text
except:
    price =  browser.find_element(By.CSS_SELECTOR, 'dd.c-product__price > strong').text
    # price = browser.find_element(By.XPATH, '//*[@id="cts"]/div[1]/div[3]/div/div/dl/div[1]/dd[3]/strong').text
    
imgs = browser.find_elements(By.CSS_SELECTOR, 'img')
for i in imgs:
    img = i.get_attribute("src")
    if 136 < img.__sizeof__()<= 400:
        break 

print("상품 이름 : ", name)
print("가격 : ", price)
print("상품 이미지 : ", img)

browser.quit()