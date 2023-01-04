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

        new_price = int(re.sub(r"[^0-9]", "", price.text))
    except:
        new_price = 0
    return(new_price)