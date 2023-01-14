from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium_price import get_price
from selenium_title import get_title
from selenium_img import get_img
from flask import jsonify
from elevenst import elevenst_get_info
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
# import pyautogui

DRIVER_PATH = "/app/chrome/chromedriver"
options = Options()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")
options.add_argument('User-Agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')
options.add_argument('Accept-Language=ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7')
options.add_argument("lang=ko_KR")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
mobile_emulation = { "deviceName": "iPhone X" }
options.add_experimental_option("mobileEmulation", mobile_emulation)


def web_scrap(url): 
    browser = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
    # if (url.find("link.coupang") != -1): # 쿠팡 앱링크면
    #     # os.environ['DISPLAY'] = ':0'
    #     # os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
    #     # caps = DesiredCapabilities
    #     # # caps['loggingPrefs'] = {'perfomance': 'ALL'}
    #     # # browser = webdriver.Chrome(desired_capabilities=caps)
    #     # browser = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
    #     # browser_log = browser.get_log('performance')
    #     # print(browser_log)
    #     # return;
        
    #     # print(ActionChains(browser).context_click().perform().location())
    #     print(pyautogui.size())
    #     print(pyautogui.position())
    #     print("================끝==================")
    #     return;
        
    #     res = browser.get(url, headers=headers)
    #     print(res.text)
        
            
        # return jsonify({'url': url, 'title': title, 'price': price, 'img': img})
    
    if (url.find("musinsaapp") != -1): # 무신사 앱링크면
        url += "?_imcp=1"
    browser.get(url)
    if (url.find("11st.co.kr") != -1): # 11번가
        return elevenst_get_info(browser)
    else: 
        title = get_title(browser, url)
        print("title", title)
        price = get_price(browser)
        print("price", price)
        img = get_img(browser, url)
        print("img", img)

    return jsonify({'url': url, 'title': title, 'price': price, 'img': img})