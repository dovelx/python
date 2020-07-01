# 临时cookies
cookies = {'JSESSIONID':'A1CF108C3A1FE93839F10438D7FAAB6C1jJmLy'}
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,FirefoxOptions
import re

def login1():
    print("开始登录")
    opt = FirefoxOptions()            # 创建Chrome参数对象
    opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Firefox(options=opt)     # 创建Chrome无界面对象

    for i in range(3):
        # selenium登录测试长庆
        time.sleep(i)
        driver.get("http://192.168.6.156/passports/login?service=http%3A%2F%2F192.168.6.156%2Fportals%2Fcas&tenantCode=clsh&trial=false")
        driver.find_element(By.ID, "name").send_keys("clshadmin")
        driver.find_element(By.ID, "pwd1").send_keys("1")
        driver.find_element(By.LINK_TEXT, "登录").click()
        j=i+10
        #time.sleep(j)
        # 获取JSESSIONID1
        c = driver.get_cookies()
        for a in c:
            if a['name'] == 'JSESSIONID':
                b = a
        cookies = {'JSESSIONID': b['value']}
        print("登录成功,cookies", cookies)
        time.sleep(j)
        url = 'http://192.168.6.156/portals/clsh'
        rs = requests.get(url= url ,cookies =cookies)
        print(rs.status_code,i)
        data = rs.content.decode('utf-8')

        searchObj = re.search("window.csrf = '(.+?)';", data, re.M | re.I)
        if searchObj:
            #print("searchObj.group() : ", searchObj.group())
            #print("searchObj.group(1) : ", searchObj.group(1))
            csrf = searchObj.group(1)
            print("csrf found!!",csrf)
            break

        else:
            time.sleep(1)
            if i == 19:
                print("Csrf Not found!!")
                csrf = i
            # driver.close()
            # driver.quit()
            # return cookies, 0
            driver.close()
            driver.quit()

    driver.close()
    driver.quit()
    print("quit browser")
    return cookies, csrf

def login():
    cookies = {'JSESSIONID': 'EC29C41A993DCEFB1307EBEC8B542913vrmfsF'}
    csrf = '1ccdf44c6a544f579b5d6c6afd483a89'
    return cookies, csrf

if __name__=='__main__':

    login1()