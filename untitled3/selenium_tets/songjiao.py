import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import requests
import random
import string
import datetime



#selenium登录测试长庆
driver = webdriver.Firefox()
driver.get(
            "http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false")

driver.find_element(By.ID, "username").send_keys("test")
driver.find_element(By.ID, "pwd1").send_keys("1")
driver.find_element(By.CSS_SELECTOR, ".justUse").click()


#获取JSESSIONID
c= driver.get_cookies()
#print (c)
print (c[0])
for a in c:
    #print (a)
    if a['name'] == 'JSESSIONID':
        b=a
        #print (b)
cookies={'JSESSIONID': b['value']}
#cookies={'JSESSIONID': '59E80FDA10220D88AB9A643E9CC4F314TcoeKm'}
print(cookies)
num = 2000000001774
#送交接口地址
url3='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(num,num)
print("送交请求url",url3)

#请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '45c959581a024e6e9607752a6664a313',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }


formdata ={"opinion":"申请审批","nodeStr":"2000000009070","2000000009070":"测试用户","2000000009070_id":1000}
formdata2={
	"opinion": "申请审批",
	"nodeStr": "2000000009070",
	"2000000009070": "测试用户",
	"2000000009070_id": 1000
}
#请求接口
rs=requests.post(url3, json = formdata, headers = headers,cookies=cookies)
rs.encoding='utf-8'
rsp = str(rs.content, 'utf8')
print(rsp)


time.sleep(2)
driver.close()
driver.quit()
