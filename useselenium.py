import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

env_dist = os.environ

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)

def main():
    loginUrl = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/casValidate.do?service=/xsfw/sys/swmxsyqxxsjapp/*default/index.do'

    params = {
        'login_url': loginUrl,
        'username': env_dist['username'],
        'password': env_dist['password']
    }
    print(params['username'])
    res = requests.post(
        'http://cas.ge2dan.top/wisedu-unified-login-api-v1.0/api/login', params)
    cookieStr = str(res.json()['cookies'])
    
    driver.get("http://stu.hfut.edu.cn/")

    for line in cookieStr.split(';'):
        cookies = {}
        name, value = line.strip().split('=', 1)
        cookies['name'] = name
        cookies['value'] = value
        driver.add_cookie(cookie_dict=cookies)

    driver.get("http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/*default/index.do#/add")
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[6]/div/button').click()
    driver.quit()

if __name__ == '__main__':
    main()
