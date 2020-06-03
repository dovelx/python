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
print("作业预约名称",name)

#获取当前时间，为作业预约提供时间变量
now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=5)
now2 = now + datetime.timedelta(minutes=10)
fnow1 = now1.strftime("%Y-%m-%d %H:%M:%S")
fnow2 = now2.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")
#临时cookies
cookies={'JSESSIONID': 'DE61E05A5A4D82731810443381EE5EAFBjjOS8'}
#暂时关闭登录
'''
#selenium登录测试长庆
driver = webdriver.Firefox()
driver.get("http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false")

driver.find_element(By.ID, "username").send_keys("test")
driver.find_element(By.ID, "pwd1").send_keys("1")
driver.find_element(By.CSS_SELECTOR, ".justUse").click()

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

'''
print(cookies)
#用例信息变量定义
testsuit = []
caseinfo = {}

caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = 0


#预约列表用例信息
caseid = 1
casename = '预约列表接口获取'
count =1

caseinfo['id'] = caseid
caseinfo['name'] = casename

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
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#获取列表最大work_appoint_id
data = data['data']['voset']['voList']
temp = []
for a in data:
    temp.append(a['work_appoint_id'])
work_appoint_id = temp[0]
#当前最大work_appoint_id加1
c =work_appoint_id+1




#=====================开始作业预约
#用例信息

casename = '作业预约'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#拼写预约URL

num = c
print("作业预约列表NEW ID:",num)
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.3707947936681053&contentType=json&ajax=true&tid=1'%(num,num)
#作业预约作业任务名称随机数生成函数
#print ("预约url\n",url2)

#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': 'bd95a01c276341b89715228e81d0ca3f',
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
'''
rs.encoding='utf-8'
rsp = str(rs.content, 'utf8')
#if rsp['status'] == 3200:
#	print("预约接口访问成功:")
print ("作业预约保存返回:",rsp)
'''
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
#获取接口返回状态
sta= data['status']
if sta == 3200:
    print("作业预约成功", sta)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())

#送交用例信息

casename = '作业预约送交'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#送交接口地址
url3='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(num,num)

formdata2={
	"opinion": "申请审批",
	"nodeStr": "2000000009070",
	"2000000009070": "测试用户",
	"2000000009070_id": 1000
}
#time.sleep(15)
#请求送交接口
rs=requests.post(url3, json = formdata2, headers = headers,cookies=cookies)
#rs.encoding='utf-8'
#rsp = str(rs.content, 'utf8')
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#作业预约审批用例信息

casename = '作业预约审批'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
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
#rs.encoding='utf-8'
#cc = str(rs.content, 'utf8')
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#print(cc)
#安全分析第一个保存用例信息
#caseid = 5
casename = '安全分析及交底保存'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename

urlfenxi ='http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK_RISK&0.6529845051499572&contentType=json&ajax=true&tid=1'
formdatafenxi ={
	"tableName": "hse_safety_task",
	"wf_create_user": 1000,
	"iscontractor": "0",
	"analyze_type": "jsa,aqjd",
	"work_appoint_name": name,
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"workstatus": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",

	"work_appoint_id": num,
	"workcontent": "作业内容123",
	"workname": name,
	"worktickettype": "xkz,dh",
	"worktickettype_name": "作业许可证,动火作业",
	"workunitname": "长庆石化分公司",
	"workunit": 1688712,
	"planstarttime":fnow1,
	"planendtime": fnow2,
	"site": "作业地点123",
	"equipmentname": "",
	"work_position_name": "制氢北区",
	"work_position_id": 2000000002019,
	"equipmentnumber": "",
	"equipmentcode": "",
	"constructionscheme": "",
	"standardmaintenance": ""
}
#time.sleep(5)
#请求接口
rs=requests.post(urlfenxi, json = formdatafenxi, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')

#print("安全分析及交底保存",cc)
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)

#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#获取worktaskid
data = data['data']['data']['worktaskid']
print("worktaskid",data)
worktaskid = data
#获取安全分析接口用例信息
#caseid = 6
casename = '获取安全分析列表'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename

#预约安全分析接口地址
url11 = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/getMetaData?0.26386458099914045&contentType=json&ajax=true&tid=1'

#请求接口
rs=requests.get(url11, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)

#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#print (sta)
a = data['data']["voset"]["voList"]
b =[]
for i in range(len(a)):

    if a[i]['worktaskid'] !="" and a[i]['worktaskid'] !="None":
        b.append(a[i]['worktaskid'])
#print (b)
num1 = worktaskid
print ("安全分析列表使用ID:",num1)

#安全分析步骤添加
#安全分析步骤添加接口用例信息
#caseid = 7
casename = '安全分析步骤添加'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.5426692795870303&contentType=json&ajax=true&tid=1'%(num1,num1)
url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.8939960513657317&contentType=json&ajax=true&tid=1'%(num1,num1)
data = {
	"tableName": "hse_safety_analysis_step",
	"qualify_level": "no_qualify",
	"duty_name": "",
	"jsaid": num1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"step_type": "02",
	"evaluate_type": "",
	"risk_level": "02",
	"remain_risk_accept": "",
	"risk_value": 0,
	"risk_harm": "风险及危害123",
	"gravity": "1",
	"consequence": "后果123",
	"accident_possibility": "2",
	"step_name": "步骤活动123"
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#time.sleep(5)
#安全分析保存
#安全分析步保存加接口用例信息

casename = '安全分析保存'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
#num1 = num1
print("num1:",num1)
#url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.2955948527813328&contentType=json&ajax=true&tid=1'%(num1,num1,num1)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.09494809285755568&contentType=json&ajax=true&tid=1'%(num1,num1,num1)
data = {
	"tableName": "hse_safety_analysis",

	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": "2020-06-01 13:50:32",
	"updated_by": 1000,
	"updated_dt": "2020-06-01 13:50:32",
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"jsaid": num1,
	"jsa_templete_name": "",
	"jsa_templete_id": "",
	"temp_type": "newWorkTask",
	"jsa_monitor_userid": 1000,
	"jsa_monitor_name": "测试用户",
	"jsa_menber_userids": "1000",
	"jsa_menber_username": "测试用户",
	"analyze_time": "2020-06-03 13:51:20",
	"worktickettype": "",
	"equip_stuff": "",
	"worktaskid": num1,
	"workstatus": "",
	"worktype": "jsa",
	"revampandadvide": "",
	"inspection_name": "",
	"work_position_id": 2000000002019,
	"projecttype": "",
	"workname": "",
	"workunitname": "",
	"reference": "",
	"iscontractor": "",
	"territorialunitid": "",
	"territorialunitname": "",
	"planendtime": "",
	"reviewer": "",
	"site": "",
	"worknumber": "",
	"workunit": "",
	"craftprocess": "",
	"planstarttime": "",
	"workcontent": "",
	"isnew": "",
	"wf_instance": "",
	"wf_current_user": "",
	"wf_audit_time": "",
	"wf_current_nodeid": "",
	"wf_type": "",
	"wf_create_user": "",
	"wf_audit_state": "",
	"sourcejsaid": "",
	"remainsrisk_level": "",
	"risk_level": "04"
}
#time.sleep(5)
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#安全交底
#安全交底接口用例信息

casename = '安全交底'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
num2 = num1+17
print ("送交ID:",num2)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_DISCLOSURE/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.7447101068947941&contentType=json&ajax=true&tid=1'%(num1,num1,num2)
data = {
	"tableName": "hse_safety_disclosure",
	"additional_content": "",
	"confirm_content": "1、已清楚作业区域及周边生产作业情况\r\n2、已清楚本次作业的安全风险（JSA）\r\n3、已清楚本次作业的具体安全要求（作业许可证中的控制措施）\r\n4、已对本次作业现场安全措施进行了检查确认\r\n5、已清楚本次作业涉及的作业许可证的有限期限 \r\n6、已掌握个人防护用具正确佩戴使用方法\r\n7、已清楚突发情况下的应急避险方法",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"safeclarid": num2,
	"projecttype": "",
	"safe_name": "长庆石化安全交底",
	"worktype": "aqjd",
	"workstatus": "draft",
	"scopeandenv": "",
	"workrisk": "",
	"preventmeasure": "",
	"emermeasure": "",
	"othermatter": "",
	"safe_content": "长庆石化安全交底",
	"safe_clar_temp_id": 2000000001040,
	"safe_clar_temp_name": "",
	"worktaskid": num1,
	"work_position_id": 2000000002019
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())

#安全送交
#安全送交接口用例信息

casename = '安全送交'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.9498759321537273&contentType=json&ajax=true&tid=1'%(num1,num1)
data = {}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#作业任务添加
#作业任务添加接口用例信息

casename = '作业任务添加'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename

url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK_MCQ&0.9079012038155838&contentType=json&ajax=true&tid=1'
data  = {
	"tableName": "hse_work_task",
	"iscontractor": "0",
	"isupgrade": "0",
	"work_appoint_name": name,
	"territorialunitid": 2000000003339,
	"applyunitname": "长庆石化分公司",
	"task_pause": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"applyunitid": "1688712",
	"workstatus": "draft",
	"autorisklevel": 1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"isrecord": "",
	"eq_position": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"jsaid": 2000000001860,
	"work_appoint_id": 2000000001860,
	"jsa_code": "Created_by_Python_HmNEGR",
	"site": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"workcontent": "作业内容123",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"standardmaintenance_name": "",
	"constructionscheme": 0,
	"worktickettype": "xkz,dh",
	"worktickettype_name": "作业许可证,动火作业",
	"standardmaintenance": "",
	"equipmentname": "",
	"equipmentnumber": "",
	"equipmentcode": "",
	"workname": name
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#请求作业任务列表
#请求作业任务列表添加接口用例信息

casename = '请求作业任务列表'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/getMetaData?0.8715056152376748&contentType=json&ajax=true&tid=1'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '6363382b59f6435eb243fab57ea5a5e0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }

#请求接口
rs=requests.get(url, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())
#print (data['status'])
#print (data['data']["voset"]["voList"])
a = data['data']["voset"]["voList"]
b =[]
for i in range(len(a)):

    if a[i]['worktaskid'] !="" and a[i]['worktaskid'] !="None":
        b.append(a[i]['worktaskid'])
#print (b)
#print (max(b))
num2 = max(b)
print("作业任务列表ID-num2==:",num2)
#作业任务提交
#作业任务提交接口用例信息

casename = '作业任务提交'
count =count+1
caseid = count
caseinfo['id'] = caseid
caseinfo['name'] = casename
url =  'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.7819922897402813&contentType=json&ajax=true&tid=1'%(num2,num2)
#url1= 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=2000000004176&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=2000000004176&topFuncCode=HSE_WORK_TASK_MCQ&dataId=2000000005557&ts=1590655157270&0.9150744998075542&contentType=json&ajax=true&tid=1'
data ={
	"tableName": "hse_work_task",
	"task_worktype_code": "",
	"hasrescueplan": "",
	"territorialdeviceid": 2000000003454,
	"drawshow": "",
	"cywlqfyxzz": "",
	"autorisklevel": 1,
	"worktools": "",
	"othercontent": "",
	"equipmentcode": "",
	"ishasworker": "",
	"territorialdevicename": "制氢装置",
	"hasdrawpaper": "",
	"hassafetyplan": "",
	"worker": "",
	"card_code": "",
	"reminder": "",
	"constructionscheme": 0,
	"reminderid": "",
	"worktickettype_name": "作业许可证,动火作业",
	"task_worktype_name": "",
	"standardmaintenance": "",
	"attaches": "",
	"material_medium": "",
	"risksmeasures": "",
	"isrecord": "",
	"persistent_type": "",
	"flights": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"worktaskid": num2,
	"workname": name,
	"work_position_name": "制氢北区",
	"work_appoint_name": name,
	"actualstarttime": "",
	"actualendtime": "",
	"isgas_detection": "",
	"delayreason": "",
	"cancelreason": "",
	"pause": 0,
	"isupgrade": "0",
	"sourcetaskid": "",
	"nlglnumber": "",
	"isreport": "",
	"iswfnotreport": 0,
	"gas_standard_type": "",
	"parentid": "",
	"lsydticketid": "",
	"dqyzticketid": "",
	"dqezticketid": "",
	"task_pause": "0",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"site": "作业地点123",
	"work_property": "bespeak",
	"equipmentnumber": "",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"projecttype": "rcjx",
	"iscontractor": "0",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"worktickettype": "xkz,dh",
	"workstatus": "draft",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"workcontent": "作业内容123",
	"woid": "",
	"wo_code": "",
	"territorialunitcode": "CS8082020",
	"equt_position": "",
	"position_name": "",
	"equipmentname": "",
	"safeclar": "",
	"safecode": "",
	"work_position_id": 2000000002019,
	"jsa_code": name,
	"jsaid": num,
	"work_appoint_id": num,
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"task_risklevel": "",
	"task_closereason": "",
	"task_closetype": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_instance": "",
	"wf_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"jobstatus": "",
	"weekplanid": "",
	"plan_type": 3,
	"gasdetecttype": "",
	"close_type": "",
	"closereason": "",
	"jsa_code2": "",
	"jsaid2": "",
	"isproprietor": "",
	"planendtime_org": "",
	"specialenvironment": "",
	"gas_aging": "",
	"safetyanalysisid": "",
	"safetyanalysiscode": "",
	"isspecialcondition": "",
	"specialcondition": "",
	"task_risklevel_org": "",
	"eq_position": ""
}
#time.sleep(3)
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("获取列表成功", status)
    caseinfo['result'] = 1
else:
    caseinfo['result'] = 0
#收集用例执行信息
testsuit.append(caseinfo.copy())

#作业许可证保存
#作业票ID
num3 = 2000000005848+2+2+4+2
ts = 1591086843103+1+2+1
print(num3)
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1590652813735&0.27372678355625824&contentType=json&ajax=true&tid=1'%(num2,num2,num3)
#url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=2000000005573&ts=1590656443277&0.7178753893110355&contentType=json&ajax=true&tid=1'%(num2,num2)
#print(url)
data = {
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "",
	"radiosourcenum": "",
	"relevantdoc": "",
	"safedistance": "",
	"issjtssxzy": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "9002",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": 1590656443277,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": num3,
	"worktaskid": num2,
	"equipmentnumber": "",
	"worktype": "xkz",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "",
	"site": "作业地点123",
	"workway": "",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "0",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "0",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "1",
	"gas_aging": "1",
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "作业许可证",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
#print ("作业许可证保存",cc)

#作业许可证提交
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/hse_work_ticket_submit?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1591086843103&0.5776995917838637&contentType=json&ajax=true&tid=1'%(num2,num2,num3)
#print(url)
data ={
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "",
	"radiosourcenum": "",
	"relevantdoc": "",
	"safedistance": "",
	"issjtssxzy": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "无",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": ts,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": num3,
	"worktaskid": num2,
	"equipmentnumber": "",
	"worktype": "xkz",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "",
	"site": "作业地点123",
	"workway": "",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "0",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "0",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "0",
	"gas_aging": "",
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "作业许可证",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}
#print("last::", data)
#请求接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
print (cc)
#driver.close()
#driver.quit()
#作业票提交
#url
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/hse_work_ticket_submit?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1591086298901&0.7738920409000762&contentType=json&ajax=true&tid=1'%(num2,num2,num3)
data = {
	"tableName": "hse_work_ticket",
	"clause": "",
	"tasktype": "",
	"radiosourcenum": "",
	"relevantdoc": "",
	"safedistance": "",
	"issjtssxzy": "",
	"isupgradedh": "",
	"isdzdh": "",
	"isrecord": "",
	"excavation_eqp": "",
	"territorialunitcode": "CS8082020",
	"worker": "9002",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": 1591086298901,
	"istaskpause": 0,
	"classgroup": "",
	"isend": "",
	"end_reason": "",
	"end_dt": "",
	"groundwire_num": "",
	"groupknife_num": "",
	"groundwire_code": "",
	"othercontent": "",
	"sent_overdueclose_message": 0,
	"isupgrade": "0",
	"isfireday": "0",
	"isdue": "0",
	"operator": "",
	"worktimeconsum": "",
	"task_pause": "0",
	"projecttype": "",
	"is_pause": 0,
	"workticketid": 2000000005846,
	"worktaskid": 2000000004306,
	"equipmentnumber": "",
	"worktype": "xkz",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"applyunitid": 1688712,
	"applyunitname": "长庆石化分公司",
	"worknumber": "",
	"worklevel": "",
	"site": "作业地点123",
	"workway": "",
	"planstarttime": fnow1,
	"planendtime": fnow2,
	"actualstarttime": "",
	"actualendtime": "",
	"otherwork": "",
	"workname": name,
	"workcontent": "作业内容123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workstatus": "draft",
	"equipmentpipename": "",
	"medium": "",
	"temperature": "",
	"pressure": "",
	"blindplate_material": "",
	"blindplate_spec": "",
	"blindplate_code": "",
	"blindplate_mapandcode": "",
	"workhighly": "",
	"objectmass": "",
	"poweraccesspoint": "",
	"workvoltage": "",
	"equipmentandpower": "",
	"otherunit": "",
	"workreason": "",
	"isharmconfirm": "",
	"ismeasureconfirm": "",
	"isgascomplate": "",
	"issigncomplate": "",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"closereason": "",
	"gastestaging": "",
	"blindplate_worktype": "",
	"gasket_material": "",
	"gasket_spec": "",
	"close_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"isppeconfirm": "",
	"invalidreason": "",
	"hassafetyplan": "0",
	"hashseplan": "",
	"hasemergencyplan": "",
	"hasdrawpaper": "0",
	"haschecklist": "",
	"hasrescueplan": "",
	"loadradius": "",
	"loaddegree": "",
	"loadrate": "",
	"objectnorm": "",
	"loadmass": "",
	"haslineopensitemap": "",
	"radiosourcetype": "",
	"sourcecode": "",
	"sourcestrength": "",
	"suprange": "",
	"controlrange": "",
	"drawshow": "",
	"hashookcheck": "",
	"hasfacadecheck": "",
	"hasdrivermedical": "",
	"objectname": "",
	"cancelreason": "",
	"hidesituation": "",
	"work_position_id": 2000000002019,
	"isgas_detection": "1",
	"gas_aging": "1",
	"isqualgasdetection": "",
	"dig_size_l": "",
	"dig_size_w": "",
	"dig_size_h": "",
	"attaches": "",
	"lock_status": 0,
	"lock_equipment_id": "",
	"dl_uuid": "",
	"dl_time": "",
	"level_upgrade": 0,
	"loadgoodsname": "",
	"loadhigh": "",
	"worktask_name": name,
	"worktype_name": "作业许可证",
	"dz_craneno": "",
	"gas_standard_type": "",
	"isproprietor": "",
	"worksite": "",
	"workticketmbcdid": "",
	"isstoppower": "",
	"work_position_name": "制氢北区",
	"gas_detector_no": "",
	"additional_requirements": "",
	"worklevel_org": ""
}
#请求接口
#rs=requests.post(url, json = data, headers = headers,cookies=cookies)
rs.encoding='utf-8'
cc = str(rs.content, 'utf8')
#print(cc)
for i in range(len(testsuit)):
    print(testsuit[i])


import requests
import execjs
import os
import json

def getEntryPwd(encryptType,pwd,modulus,publicExponent):
    # 返回加密后的密码
    path=os.path.abspath(os.path.dirname(__file__))
    file=os.path.join(path,'./hdEncrypt_merge.js')
    #logging.debug("path:%s"%path)
    data=open(file,'r',encoding= 'utf8').read()
    jss=execjs.compile(data)
    #logging.debug(jss)
    return  jss.call("login",encryptType,pwd,modulus,publicExponent)
#移动端登录
url = "http://192.168.6.27:6030/m/passport/login/getEncryptType.json"
url1 ="http://192.168.6.27:6030/m/passport/login/login.json"

headers ={
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
    'Connnection':'Keep-Alive'
    }
sr = requests.get(url,headers=headers)

eq = sr.json()

USER_NAME = "test"
password ="1"
loginStoken=eq['data']['loginStoken']
encryptType=eq['data']['encryptType']
modulus = eq['data']['pubKeyVO']['modulus']
publicExponent = eq['data']['pubKeyVO']['publicExponent']
pwd = getEntryPwd(encryptType,password,modulus,publicExponent)
#print (eq)
#print (eq['status'])
#print(loginStoken)
#print(encryptType)
#print( pwd)
#print(eq['data']['pubKeyVO'])
headers={
    'Accept': 'application/json',
     'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
    'Connnection': 'Keep-Alive'
    }

data={"appVersion":"01.20.0530","loginStoken":loginStoken,"password":pwd,"username":"test",'tenantid':0}
#data = base64.b64encode(json.dumps(data))
rs= requests.post(url=url1,json =data,headers = headers)

cookies = requests.utils.dict_from_cookiejar(rs.cookies)

#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
loginStoken = data['data']['st']
#print(data)
print(loginStoken)
#encryptType = eq['data']['encryptType']
#print (encryptType)

#cookies={'JSESSIONID': '0F5ED4C32181CF4F223E2984DFCE086A0afqB2'}
#保存作业许可票
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/cardSave.json?level=1"
headers = {
            "Accept":"application/json",
"Accept-Encoding": "gzip",
"user-agent":"ONEPLUS A6010(Android/10) (com.hayden.hap.fv/1.0.2) Weex/0.16.0 1080x2134",
"Content-Type": "application/json;charset=UTF-8",
    "st":loginStoken,
    "tid":"1"

}
data = {
	"children": {
		"HSE_WORK_TASK_HARM_MCQ_M": [{
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008710,
				"harmcode": "gzxy001",
				"harmname": "爆炸性气体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019723,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008711,
				"harmcode": "gzxy002",
				"harmname": "易燃性物质",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019724,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008712,
				"harmcode": "gzxy003",
				"harmname": "腐蚀性液体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019725,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008713,
				"harmcode": "gzxy004",
				"harmname": "有毒有害化学品",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019726,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008714,
				"harmcode": "gzxy005",
				"harmname": "高压气体/液体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019727,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008715,
				"harmcode": "gzxy006",
				"harmname": "蒸汽",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019728,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008716,
				"harmcode": "gzxy007",
				"harmname": "爆炸性粉尘",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019729,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008717,
				"harmcode": "gzxy008",
				"harmname": "惰性气体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019730,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008718,
				"harmcode": "gzxy009",
				"harmname": "危险物料混窜",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019731,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008719,
				"harmcode": "gzxy010",
				"harmname": "转动设备",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019732,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008720,
				"harmcode": "gzxy011",
				"harmname": "物料自然",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019733,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008721,
				"harmcode": "gzxy012",
				"harmname": "中毒窒息",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019734,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008722,
				"harmcode": "gzxy013",
				"harmname": "辐射",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019735,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008723,
				"harmcode": "gzxy014",
				"harmname": "化学反应",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019736,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008724,
				"harmcode": "gzxy015",
				"harmname": "隐蔽工程泄漏",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019737,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008725,
				"harmcode": "gzxy016",
				"harmname": "不利天气",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019738,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008726,
				"harmcode": "gzxy017",
				"harmname": "坠落",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019739,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008727,
				"harmcode": "gzxy018",
				"harmname": "产生火花",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019740,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008728,
				"harmcode": "gzxy019",
				"harmname": "噪音",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019741,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008729,
				"harmcode": "gzxy020",
				"harmname": "灼伤/烫伤",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019742,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008730,
				"harmcode": "gzxy021",
				"harmname": "物体打击",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019743,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008731,
				"harmcode": "gzxy022",
				"harmname": "触电/静电",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019744,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008732,
				"harmcode": "gzxy023",
				"harmname": "湿滑跌倒",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019745,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008733,
				"harmcode": "gzxy024",
				"harmname": "淹溺/坍塌",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019746,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmid": 2000000008734,
				"harmcode": "gzxy025",
				"harmname": "其他请注明：（）",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019747,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": num2,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"dataStatus": 0,
				"worktype": "xkz",
				"harmname": "风险及危害123",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000019748,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"workticketid": num3,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_EQUIPMENT_M": [{
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全眼镜",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000100,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010018,
				"equipmentcode": "aqyj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "全封闭眼罩",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000101,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010019,
				"equipmentcode": "qfbyz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "焊接护目镜",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000102,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010020,
				"equipmentcode": "hjhmj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全帽",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000103,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010021,
				"equipmentcode": "aqm",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防静电服装",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000104,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010022,
				"equipmentcode": "fjdfz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "护耳",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000105,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010023,
				"equipmentcode": "he",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全鞋",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000106,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010024,
				"equipmentcode": "aqx",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防毒面罩",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000107,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010025,
				"equipmentcode": "fdmz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "正压式呼吸器",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000108,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010026,
				"equipmentcode": "zyshxq",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防化服",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000109,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010027,
				"equipmentcode": "fhf",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "手套",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000110,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010028,
				"equipmentcode": "st",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "绝缘服",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000111,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010029,
				"equipmentcode": "jyfz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防弧面具",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000112,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010030,
				"equipmentcode": "fhmj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全带",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000113,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010031,
				"equipmentcode": "aqd",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "安全绳",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000114,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010032,
				"equipmentcode": "aqs",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "逃生设施",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000115,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010033,
				"equipmentcode": "tsss",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "人员培训已完成",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000116,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010034,
				"equipmentcode": "rypx",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "其他（）",
				"dataStatus": 0,
				"worktype": "xkz",
				"personequipmentid": 2000000000117,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000010035,
				"equipmentcode": "qtfh",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": num3,
				"worktaskid": num2,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "切断工艺流程",
				"riskrepositoryid": 2000000004946,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042204,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "设路障",
				"riskrepositoryid": 2000000004947,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042205,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "设备隔离、吹扫、置换",
				"riskrepositoryid": 2000000004948,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042206,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "工作警示牌",
				"riskrepositoryid": 2000000004949,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042207,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "电源切断",
				"riskrepositoryid": 2000000004950,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042208,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "通讯工具",
				"riskrepositoryid": 2000000004951,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042209,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "完成上锁挂牌",
				"riskrepositoryid": 2000000004952,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042210,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "火花防护罩",
				"riskrepositoryid": 2000000004953,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042211,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "通风",
				"riskrepositoryid": 2000000004954,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042212,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "气体检测仪",
				"riskrepositoryid": 2000000004955,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042213,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "气体检测",
				"riskrepositoryid": 2000000004956,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042214,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "防爆机具",
				"riskrepositoryid": 2000000004957,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042215,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "工作区域围栏、警戒线",
				"riskrepositoryid": 2000000004958,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042216,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "急救设施",
				"riskrepositoryid": 2000000004959,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042217,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "紧急疏散指示",
				"riskrepositoryid": 2000000004960,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042218,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "消防设施",
				"riskrepositoryid": 2000000004961,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042219,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "需要夜间照明和警示灯具",
				"riskrepositoryid": 2000000004962,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042220,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "安全冲淋设施",
				"riskrepositoryid": 2000000004963,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042221,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "设备安全检查合格并已贴标签",
				"riskrepositoryid": 2000000004964,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042222,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "安全工作方案审核通过",
				"riskrepositoryid": 2000000004965,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042223,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "特种作业人员均持有效资质",
				"riskrepositoryid": 2000000004966,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk21",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042224,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他措施：（）",
				"riskrepositoryid": 2000000004967,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gzxk22",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "xkz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gzqaqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000042225,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": num3,
				"worktaskid": num2,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"hse_work_task_harm_mcq_m": 26,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"otherunit": "",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "测试用户",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"othercontent": "",
		"hse_work_task_equipment_m": 18,
		"worktype_name": "作业许可证",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "0",
		"hassafetyplan": "0",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"worker": "长庆石化分公司",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": fnow2,
		"applyunitname": "长庆石化分公司",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"task_pause": 0,
		"updated_by": 1000,
		"planstarttime": fnow1,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 22,
		"workcontent": "作业内容123",
		"workticketid": num3,
		"close_type": "",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "测试用户",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "xkz",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"gas_detector_no": "",
		"applyunitid": 1688712,
		"ticketdealphoto": 0,
		"gas_aging": "1",
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": num2,
		"ts": 1591065322626
	}
}

#rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']