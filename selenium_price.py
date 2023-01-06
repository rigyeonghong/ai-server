from selenium.webdriver.common.by import By
import re

def get_price(browser):
    try:
        prices = browser.find_elements(By.XPATH, '//*[contains(text(), "원") and not(contains(text(), "배송")) and not(contains(text(), "천원"))]') # 네이버
        for price in prices:
            if 100 < price.location['y'] <= 980:
                break
            
        if price.text == "원":
            price = browser.find_element(By.XPATH, '//*[contains(text(), "원") and not(contains(text(), "배송")) and not(contains(text(), "천원"))]//preceding::span[1]') # 네이버

        price = price.text
        if price.find(":") != -1:
            p_list = list(price.split())
            for p in p_list:
                if p.find(",") != -1:
                    price = p
        
        if price.find("~") != -1:
            idx = price.index("~")
            price = price[idx+1:]
        new_price = int(re.sub(r"[^0-9]", "", price))
    
    except Exception as e: 
        print(e)
        new_price = 0
    
    return(new_price)