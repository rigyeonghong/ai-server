from selenium.webdriver.common.by import By
from s3_connect import default_img
from flask import jsonify
import re

def elevenst_get_info(browser):
    try :
        title = browser.find_element(By.CSS_SELECTOR, 'div.dt_title').text # CSS_SELECTOR로 가능 
        # name = browser.find_element(By.XPATH, '//*[@id="cts"]/div[2]/div[2]/div[3]/h1').text # XPATH로 가능
    except: 
        try:
            title = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div > div > h2').text
            # title = browser.find_element(By.XPATH, '//*[@id="cts"]/div[1]/div[3]/div/div/h2').text
        except:
            title = browser.find_element(By.CSS_SELECTOR, '#cts > div.base > div.atf_base > div.dt_title > h1').text
            
    try :
        # price =  browser.find_element(By.CSS_SELECTOR, 'div.price > span > b').text
        price = browser.find_element(By.XPATH, '//*[@id="priceLayer"]/div[2]/span/b').text
    except:
        # price =  browser.find_element(By.CSS_SELECTOR, 'dd.c-product__price > strong').text
        price = browser.find_element(By.XPATH, '//*[@id="cts"]/div[1]/div[3]/div/div/dl/div[1]/dd[3]/strong').text
    
    if price.find("~") != -1:
        idx = price.index("~")
        price = price[idx+1:]
    
    new_price = int(re.sub(r"[^0-9]", "", price))
      
    try:  
        imgs = browser.find_elements(By.CSS_SELECTOR, 'img')
        
        for i in imgs:
            img = i.get_attribute("src")
            print(img)
            if 136 < img.__sizeof__()<= 400:
                break
    except:
        img = default_img
        
    print("[title_11st]", title)
    print("[price_11st]", price)
    print("[img_11st]", img)
    return jsonify({'url': url, 'title': title, 'price': new_price, 'img': img})
