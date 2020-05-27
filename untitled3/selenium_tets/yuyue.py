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
now2 = now + datetime.timedelta(minutes=10)
fnow1 = now1.strftime("%Y-%m-%d %H:%M:%S")
fnow2 = now2.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")

#selenium登录测试长庆
driver = webdriver.Firefox()
driver.get("http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false")
#driver.set_window_size(1928, 1044)
#driver.find_element(By.ID, "username").click()
driver.find_element(By.ID, "username").send_keys("test")
#driver.find_element(By.ID, "pwd1").click()
driver.find_element(By.ID, "pwd1").send_keys("1")
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
    'csrf': '45c959581a024e6e9607752a6664a313',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }
#rs=s.get(url1,headers=headers,cookies=cookies,verify=False)
#rs.encoding='utf-8'
#print(rs.text)

#作业预约接口地址
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=2000000001767&topFuncCode=HSE_WORK_APPOINT&dataId=2000000001767&0.3707947936681053&contentType=json&ajax=true&tid=1'
#作业预约作业任务名称随机数生成函数
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters+string.digits,num))
    return  salt
name = "create_by_python_"+ranstr(6)

formdatanew ={
	"tableName": "hse_work_appoint",
	"iscontractor": "0",
	"workunitname_no": "",
	"territorialunitid": 2000000003339,
	"worktaskid_no": 0,
	"isreport": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"wf_audit_state": "6",
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"isspecialcondition": "",
	"specialenvironment": "DH0000_000002_SE01",
	"task_worktype_code": "GCN",
	"task_worktype_name": "储罐浮舱内",
	"cywlqfyxzz": "0",
	"isdzdh": "0",
	"projecttype": "rcjx",
	"isupgradedh": "0",
	"persistent_type": "newoperation",
	"issjtssxzy": "0",
	"worklevel_dh": "mcq_dh_workLevel02",
	"worklevel_sx": "",
	"worklevel_gc": "",
	"worklevel_dz": "",
	"worklevel_gx": "",
	"sourcetype": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"worksite": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workname": name,
	"workcontent": "作业内容123",
	"worktypename": "作业许可证,动火作业",
	"worktype": "xkz,dh",
	"appointstarttime": fnow1,
	"appointendtime": fnow2,
	"risksmeasures": "重点防控的风险123",
	"material_medium": "物料介质123"
}
#请求作业预约保存接口
rs=requests.post(url2, json = formdatanew, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
print(cc)
#driver.find_element(By.CSS_SELECTOR, ".icon-headermenu-logout").click()
#开始编写送交接口
pass

time.sleep(2)
driver.close()
driver.quit()
