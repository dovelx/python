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

#获取当前时间，为作业预约提供时间变量
now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=5)
now2 = now + datetime.timedelta(minutes=55)
fnow1 = now1.strftime("%Y-%m-%d %H:%M:%S")
fnow2 = now2.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")

#selenium登录测试长庆
driver = webdriver.Firefox()
driver.get("http://passport.51gxc.com/login?service=http%3A%2F%2Fhse.51gxc.com%2Fcas&tenantCode=hd&trial=false")
#driver.set_window_size(1928, 1044)
#driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("hdtest09")
#driver.find_element(By.ID, "pwd1").click()
driver.find_element(By.ID, "pwd1").send_keys("123456")
driver.find_element(By.CSS_SELECTOR, ".justUse").click()
#driver.find_element(By.CSS_SELECTOR, ".user-name").click()
#driver.execute_script("window.scrollTo(0,0)")

#获取JSESSIONIDJSESSIONID
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

#s=requests.session()
#url1='http://192.168.6.27:6030/hse/MSG_NOTICE_PORTAL/qryNotice?0.9438818289569333&ajax=true&tid=1'
#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': 'd997f734ce4245d3988f2c4e72ffe62a',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }
#rs=s.get(url1,headers=headers,cookies=cookies,verify=False)
#rs.encoding='utf-8'
#print(rs.text)

#作业预约接口地址
#url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=2000000001732&topFuncCode=HSE_WORK_APPOINT&dataId=2000000001732&0.3707947936681053&contentType=json&ajax=true&tid=1'
url2 = "http://hse.51gxc.com/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_APPOINT&0.44734557659283736&contentType=json&ajax=true&tid=2000000000453"
#作业预约作业任务名称随机数生成函数
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters+string.digits,num))
    return  salt
rranstr = "create_by_python_"+ranstr(6)
formdata ={
	"tableName": "hse_work_appoint",
	"iscontractor": "0",
	"workunitname_no": "",
	"territorialunitid": 2000000003766,
	"worktaskid_no": 0,
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000000453,
	"ts": "",
	"isspecialcondition": "",
	"wf_audit_state": "",
	"territorialunitname": "海顿测试",
	"territorialunitcode": "0003",
	"worksite": "changfang",
	"workunit": 2000000001623,
	"workunitname": "现场总管演示",
	"workname": "zuoyerenwumingcheng1",
	"worktypename": "受限空间",
	"worktype": "sx",
	"appointstarttime": fnow1,
	"appointendtime": fnow2
}
#请求作业预约保存接口
rs=requests.post(url2, json = formdata, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
print(cc)


time.sleep(2)
driver.close()
driver.quit()
