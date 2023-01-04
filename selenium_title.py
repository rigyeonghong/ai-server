from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_title(browser, url):
    try:
        window_height = browser.get_window_size()['height']

        # 쿠팡
        if (url.find("coupang.com") != -1):   
            close_btn = browser.find_element(By.XPATH, '//*[@id="fullBanner"]/div/div/a[2]')
            close_btn.click()
            WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pdpImages"]/ul/li[1]/img')))


        #2. 텍스트 스크래핑 (meta 활용)
        # 마켓컬리, 네이버 
        title_scrap = False

        try:
            meta_title = browser.find_element(By.XPATH, "//meta[@property='og:title']")
            
            if (meta_title != 0 and url.find("11st.co.kr") == -1):
                title = meta_title.get_attribute("content")
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
                            title_scrap = True
                            break

            except:
                pass

        # 11번가, 무신사
        if title_scrap == False: 
            try :
                title = browser.find_element(By.CSS_SELECTOR, 'div.dt_title').text # CSS_SELECTOR로 가능 
            except:
                title = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(3) > div > div > h2').text
    except:
        title = "사이트에서 상품 보기"
    return(title)