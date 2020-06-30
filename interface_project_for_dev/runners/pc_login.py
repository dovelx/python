# 临时cookies
cookies = {'JSESSIONID': '3F4CFCA46A130205CB6F275B33464EF7o7BdGv'}

from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,FirefoxOptions
import time
def login():
    opt = FirefoxOptions()            # 创建Chrome参数对象
    opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Firefox(options=opt)     # 创建Chrome无界面对象
    #selenium登录测试长庆
    #driver = webdriver.Firefox()

    driver.get("http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false")

    driver.find_element(By.ID, "username").send_keys("test")
    driver.find_element(By.ID, "pwd1").send_keys("1")
    driver.find_element(By.CSS_SELECTOR, ".justUse").click()

    time.sleep(5)
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
    driver.close()
    driver.quit()
    return cookies

cookies= login()

print(cookies)