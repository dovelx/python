# 临时cookies
cookies = {'JSESSIONID':'A1CF108C3A1FE93839F10438D7FAAB6C1jJmLy'}
import requests
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,FirefoxOptions
from bs4 import BeautifulSoup
import re
def login():
    opt = FirefoxOptions()            # 创建Chrome参数对象
    opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Firefox(options=opt)     # 创建Chrome无界面对象
    #selenium登录测试长庆
    #driver = Firefox()

    driver.get("http://192.168.6.156/passports/login?service=http%3A%2F%2F192.168.6.156%2Fportals%2Fcas&tenantCode=clsh&trial=false")

    driver.find_element(By.ID, "name").send_keys("clshadmin")
    driver.find_element(By.ID, "pwd1").send_keys("1")
    #driver.find_element(By.CSS_SELECTOR, ".justUse").click()
    driver.find_element(By.LINK_TEXT, "登录").click()
    time.sleep(10)
    #获取JSESSIONID
    c= driver.get_cookies()
    #print (c)
    #print (c[0])
    for a in c:
        #print (a)
        if a['name'] == 'JSESSIONID':
            b=a
            #print (b)
    cookies={'JSESSIONID': b['value']}

    #cookies={'JSESSIONID': '3BAB7DF0381948EA376F907859D5321C'}


    #cookies= login()
    #print(cookies)

    url = 'http://192.168.6.156/portals/clsh'
    rs = requests.get(url= url ,cookies =cookies)
    data = rs.content.decode('utf-8')
    #print(data)
    #data = rs.content.decode('utf-8')
    #print(data)
    #soup = BeautifulSoup(data,'lxml')
    #t = rs.content
    #print(soup.prettify())
    #print(soup.body.script)
    #print(soup.find_all("csrf"))
    # soup = BeautifulSoup(data, "html.parser")
    # pattern = re.compile(r"window.csrf = \'")
    #
    # script = soup.find("script type=\"text/javascript\"", text=pattern)
    # print(script)
    #print (pattern.search(script.text).group(1))
    searchObj = re.search("window.csrf = '(.+?)';", data, re.M | re.I)
    # searchObj = re.search('wind(.+?)w', html_data, re.M | re.I)
    csrf = searchObj.group(1)
    if searchObj:
        print("searchObj.group() : ", searchObj.group())
        print("searchObj.group(1) : ", searchObj.group(1))
        # print(    "searchObj.group(2) : ", searchObj.group(2))
    else:
        print("Nothing found!!")
    driver.close()
    driver.quit()
    return cookies,csrf
#a = []

#a = login()

#print(a)