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


#作业预约作业任务名称随机数生成函数
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters+string.digits,num))
    return  salt
name = "Created_by_Python_"+ranstr(6)
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

#预约列表接口地址
url1 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/getMetaData?0.3897117454385264&contentType=json&ajax=true&tid=1'
#请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '6363382b59f6435eb243fab57ea5a5e0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }

#请求接口
rs=requests.get(url1, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
#获取接口返回状态
sta= data['status']
print ("获取列表成功",sta)
#获取列表最大work_appoint_id
data = data['data']['voset']['voList']
b = []
for a in data:
    b.append(a['work_appoint_id'])
c = b[0]
#当前最大work_appoint_id加1
c =c+1
print ("work_appoint_id:",c)

#拼写预约URL

num = c
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.3707947936681053&contentType=json&ajax=true&tid=1'%(num,num)
#作业预约作业任务名称随机数生成函数
#print ("预约url\n",url2)

#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '45c959581a024e6e9607752a6664a313',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }
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
rsp = str(rs.content, 'utf8')
#if rsp['status'] == 3200:
#	print("预约接口访问成功:")

#送交接口地址
url3='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(num,num)
print("送交请求url",url3)
#请求头
formdata2={
	"opinion": "申请审批",
	"nodeStr": "2000000009070",
	"2000000009070": "测试用户",
	"2000000009070_id": 1000
}
time.sleep(15)
#请求送交接口
rs=requests.post(url3, json = formdata2, headers = headers,cookies=cookies)
#rs.encoding='utf-8'
rsp = str(rs.content, 'utf8')
#if rsp['status'] == 3200:
#	print("预约接口访问成功:")
#rsp = str(rs.content, 'utf8')
#print('送交接口反馈:',rsp)


#审批接口地址
url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(num)
#参数
formdata ={
	"opinion": "同意",
	"cC": "1000",
	"cCName": "测试用户",
	"nickName": "用户",
	"is_normal_finish": "true",
	"nodeStr": ""
}
#请求接口
rs=requests.post(url4, json = formdata, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
#print(cc)



time.sleep(2)
driver.close()
driver.quit()
