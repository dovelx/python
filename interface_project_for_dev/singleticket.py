#2020-6-4 PC和手机端主流程，单票
import json
import requests
from globalpkg.global_var import *
from globalpkg.global_var import logger
from case.datas import *
from case.case1 import *
from tools import post
#临时cookies
cookies={'JSESSIONID': 'D7032D29FE8DF9C25AE83C0ED4745132D1ayKL'}
print(cookies)
logger.info("作业预约名称：%s",name)

#ids
tsi = tsi
worktaskid = worktaskid
#work_appoint_id = work_appoint_id

#post.p(caseinfo,url2,headers,cookies,data)
post.pa(caseinfo,headers,cookies)
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

#请求送交接口
rs=requests.post(url3, json = formdata2, headers = headers,cookies=cookies)
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
	"planstarttime":starttime,
	"planendtime": endtime,
	"site": "作业地点123",
	"equipmentname": "",
	"work_position_name": "制氢北区",
	"work_position_id": 2000000002019,
	"equipmentnumber": "",
	"equipmentcode": "",
	"constructionscheme": "",
	"standardmaintenance": ""
}

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
	"safeclarid": 2000000002100,
	"projecttype": "",
	"safe_name": "自动化测试用不要删除",
	"worktype": "aqjd",
	"workstatus": "draft",
	"scopeandenv": "",
	"workrisk": "",
	"preventmeasure": "",
	"emermeasure": "",
	"othermatter": "",
	"safe_content": "",
	"safe_clar_temp_id": 2000000001050,
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

#单票
data = {
	"tableName": "hse_work_task",
	"iscontractor": "0",
	"isupgrade": "0",
	"work_appoint_name": "",
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
	"projecttype": "",
	"isrecord": "",
	"eq_position": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"jsaid": 2000000002082,
	"work_appoint_id": "",
	"jsa_code": "任务名称",
	"site": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"workcontent": "作业内容123",
	"planstarttime": starttime,
	"planendtime": endtime,
	"standardmaintenance_name": "",
	"constructionscheme": 0,
	"worktickettype": "xkz",
	"worktickettype_name": "作业许可证",
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
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.412998005925274&contentType=json&ajax=true&tid=1'%(num2,num2)

data = {
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
	"worktickettype_name": "作业许可证",
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
	"work_appoint_name": "",
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
	"device_id": "",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"site": "作业地点123",
	"work_property": "rush_to_repair",
	"equipmentnumber": "",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"projecttype": "",
	"iscontractor": "0",
	"planstarttime": starttime,
	"planendtime": endtime,
	"worktickettype": "xkz",
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
	"work_appoint_id": "",
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
    print(data)
#收集用例执行信息
testsuit.append(caseinfo.copy())

#作业许可证保存
#作业票ID
num3 = workticketid+1
ts = tsi+1
print(num3)
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_XKZ/cardSave?parentEntityId=%d&parentFuncCode=HSE_WORK_TASK_MCQ&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&ts=1590652813735&0.27372678355625824&contentType=json&ajax=true&tid=1'%(num2,num2,num3)


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
	"worker": "3123213",
	"pipeline_level": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": 1591170000174,
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
	"device_id": "",
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
	"planstarttime": starttime,
	"planendtime": endtime,
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
	"planstarttime": starttime,
	"planendtime": endtime,
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
#print (cc)
#driver.close()
#driver.quit()


#for i in range(len(testsuit)):
 #   print(testsuit[i])


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

headers={
    'Accept': 'application/json',
     'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
    'Connnection': 'Keep-Alive'
    }

data={"appVersion":"01.20.0530","loginStoken":loginStoken,"password":pwd,"username":"test",'tenantid':0}

rs= requests.post(url=url1,json =data,headers = headers)

cookies = requests.utils.dict_from_cookiejar(rs.cookies)

#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
loginStoken = data['data']['st']
#print(data)
#print(loginStoken)

#保存作业许可票
num3 = workticketid+1
ts = tsi+1
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
		"planendtime": endtime,
		"applyunitname": "长庆石化分公司",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"task_pause": 0,
		"updated_by": 1000,
		"planstarttime": starttime,
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
		"ts": ts
	}
}

#rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

#print(data)
#获取接口返回状态
status= data['status']

#手机提交作业许可票

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/submit.json?dataId=%d&ts=%d"%(num3,ts)
data = {
	"vo": {
		"hse_work_task_harm_mcq_m": 52,
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
		"hse_work_task_equipment_m": 36,
		"worktype_name": "作业许可证",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": 0,
		"hassafetyplan": 0,
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"worker": "长庆石化分公司",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "长庆石化分公司",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"task_pause": 0,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 44,
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
		"gas_aging": 1,
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": num2,
		"ts": ts
	}
}
#rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

#print(data)
#获取接口返回状态
status= data['status']

#现场确认-危害
num5 = workticketid +1
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/harmAudit.json?workticketid=%d&workType=xkz&tabtype=harm"%(num3)
data = {
	"mainAttributeVO": {},
	"voList": [{
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
		"worktaskharmid": 2000000024223,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024224,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024225,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024226,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024227,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024228,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 1
	}, {
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
		"worktaskharmid": 2000000024229,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024230,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024231,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024232,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024233,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024234,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024235,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024236,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024237,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024238,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024239,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024240,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024241,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024242,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024243,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024244,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024245,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024246,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
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
		"worktaskharmid": 2000000024247,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"worktaskid": num2,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": now,
		"dataStatus": 0,
		"worktype": "xkz",
		"harmname": "名字123",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000024248,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"workticketid": num5,
		"ismustconfirm": 0,
		"isconfirm": 0
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']


#措施确认人属地签名

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=xkz&tabtype=measure&businesstype=gzqaqcs"%(num3)
data = {
	"mainAttributeVO": {
		"businesstype": "gzqaqcs"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000005634",
		"latitude": 39.982786,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n/wEhsy3ZGuy6kwAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "措施确认人属地",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n/wEhsy3ZGuy6kwAAAABJRU5ErkJggg==\n",
		"isbrushposition": 0,
		"disporder": 1,
		"longitude": 116.338397
	}],
	"voList": [{
		"measuredesc": "设路障",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 1,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000004947,
		"isselect": 0,
		"ver": 1,
		"created_dt": "2020-06-03 17:11:35",
		"measurecode": "gzxk02",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 1,
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "gzqaqcs",
		"updated_dt": "2020-06-03 17:11:35",
		"worktaskmeasureid": 2000000046607,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#措施确认人作业方

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=xkz&tabtype=measure&businesstype=gzqaqcs"%(num3)
data = {
	"mainAttributeVO": {
		"businesstype": "gzqaqcs"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007134",
		"latitude": 39.982786,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "措施确认人作业方",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 0,
		"disporder": 2,
		"longitude": 116.338397
	}],
	"voList": [{
		"measuredesc": "设路障",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAABICSURBVHic7d15rG13VQfw1cm20GIneEyFapnSMD1qQaQgtITYEiCKGsNYCQYUjRUS\nIUiCICHRgApYnIoIBASCSCOIzAWhWLA2rzYIVhDaAmUoDUPn9j3/eC333bfXvufec8/5rb33+XyS\nnSar7Tnf89t577fO77f3PhEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAw20siYs8+BwDAQt031jcbeyLiH0oTAQCTs3+zsScirixNBABMyjWRNxyn\nVYYCAKbj9yNvNq6oDAUATMdhkTcbLhgFABamr9m4a2UoAGA63hd5s/GXlaEAgOm4c+TNxs2VoYBp\nOqA6AFCm7xqNgyJid8sgwPQdWB0AKPGJnvrzQ7MBACzA3SPfSvleZShg2mypwOrp20rx9wGwNLZU\nYLV8rKd+ctMUAMBS/E30P+9i1vH5iPiriHhORDxwGxl29Lz+l7bxmgCbYgkVluu/I+IBDd7nG7G3\nMfl8RFx02z+v3u+/sZUCABPz8Jh/RWMZx6U99VOWNQAAwHI9I+objM0cX17WAAAAy1fdSGz1+ExE\nPGgpIwEALE3fxP7EOV7rhIh4akS8OiI+FBHXbPD6izh+EBHPnCMnANDY78b6SfxTjd730RHxqth7\nweiiGpAXNcoOAMzhjhHxsog4tjDDv8TiGo8rIuK4tvEBgKE7PPLG4byIeHDsvW5j3ubj+IafAwAY\nsJsibxb2d0hEnNPz3250fH258QGAoTs98ibhcZv4f38nIm7u+f+z4/ELzg4AjETWGFw3x+s8JSKu\n73m9fY9Pbj8yADAm74zNbaVs1ZU9r7vI9wAARiJrBPp+IXarju95/X2Pwxb0XgDAQH0n2qw87Op5\nn9uP+y7hPQGAAbhP5JP/c5b0fk/reT8XkwLAhFVcV3GHDd53T0S8dMnvDwA0dHbkE/7dGr3/LT3v\nvyci/rFRBgBgybKJ/huNM3yzJ8eeiLikcRYAYME+EcO5RfXCnix7IuK7RZkAgG06JPLJ/S2Fmd7U\nk2neh48BAMWujeGsbuzrN6K/6bi5MBcAsEUPjXxCf2plqH08Ifqbjt2FuQCALRjD48VPio1vmwUA\nBuwVkU/gR1eG6nHv6G84bizMBQDMkE3el5Um2tiO6G86rinMBQD0uDjGuT1xdPQ3HZcX5gIA9nNk\n5BP26ypDbcFdor/p+HxhLgBgHzfFOFc39nW/6G86XlWYCwCIiMdEPkk/pjLUnE6J/qbjkYW5AGDl\nTe3W0idH/2c6pjAXAKys10c+MR9ZGWoBXhvTa6QAYLSyCfni0kSLsyvyz3drZSgAWDWXxfRXAH4U\n+We8oDIUAKyKO0c+Eb+yMtSS9G2tPKkyFACsgt0x/dWN2x0a/U3HoYW5AGDSfjnyyffkylBL9sRw\nESkANJVNuteWJmrjgsg/+3sqQwHAFL01Vntr4ebIP/8RlaEAYGqyyfb8ykAFbK3AxBxUHQBY56sR\ncVRS/6nGOap9O/Ze07G/myLi042zAMCk3Cnyb/UvrAxVqG9rBQDYhin8Guwi9d0qe05lKAAYs52R\nT647K0MNwF+HJgwAFiabVG8qTTQc2dicXZoIAEbotyKfVI+uDDUg7wirHACwbdlkenlpouHJxuiM\n0kQAMCLnhm/vm/G56I7RdaWJAGBEsmbjvNJEw6UxA4A5vDNMoluRjdWTSxMBwAhkE+hrShMN23ui\nO15fK00EAAP3gbC6sVXHhTEDgC3JJs6XlyYaBw0HAGzShWHinNdV0R23Xy9NBAADlTUbLypNNB6v\niO7Y7SpNBAADdFFY3diOe4TxA4CZssnyeaWJxkfDAQAbeF+YLBfBGALABrKJ8vmlicbpW9Edx9NL\nEwHAQJwTvpkvyh9HdxxfV5oIAAYiazZeVZpovE6N7lh+pTQRAAzAH4TVjUUzngCwn2xyfHNpovHT\ncADAPs4Kk+MyGFMA2Ec2MX64NNE0ZON6aGkiAChy//BNfFkuiO64PqU0EbChA6sDwIRdktSubJ5i\nmrJVoic0TwEAxQ6OfHXjyMpQE/Jz0R3by0oTAUCBXdGdEHeXJpoe21UArLxsMvT47cXScACw0l4f\nJsMWjDEAKy2bCP+oNNE0aTgAWFlPDBNhK1dGd5x3liYCerktFhbr/Unt35qnWA0fTWqnNU8BbIqG\nAxan70mXJsHl+FRSe2TzFADQ2Geju8R/a2miaTspuuN9RWkiAGjArbDtuV4GgJXy3DD5VTDmAKyU\nbOL7+8pAK0LDAcDKODRMfFWMO4yEu1Rg+z6e1G5sngIAmLTsW/ajShOtji9Hd+wfXJoISFnhgO05\no6f+maYpVtdFSe0BzVMAM2k4YHvOS2r/3DzF6vpKUjuxeQpgJg0HbM8hSe2pzVOsLg0HjISGA+b3\nyp76zU1TrDYNBwCTl10senZpotXz09E9B5eXJgKABTokPANiCA4M5wFGwZYKzOfNSe2G5inYXR0A\nAJYp+1b9C6WJVpcVDgAm6fAwyQ2JcwEjYEsFtu4tSe1bzVMAAJOWfaM+tTTRarPCASNwQHUAGJmD\nIuKWpO7PUp2swXA+YGBsqcDWvDap/bB5CgBg0rLl+6eUJsKWCoyAZUfYGsv3w+OcwAjYUoHNe1J1\nAABg+i6J7tL960oTEWFLBYCJySa2O5YmIkLDAaNgnxM2z7UCw+S8wAi4hgM254yklj2PAwBgbudH\nd9n+TyoD8WO2VACYjGxSO7Y0EbfTcMAI2OeEzXGdwHA5NzACruGA2e5XHQBg7DQcMNsLktp7m6cA\nACbtuuheI/C40kTsyzUcMAL2OWE21wgMm/MDI2BLBQBYOg0HbOzBSW138xQAI6fhgI09N6m9rXkK\nAGDSronuBYmnliZify4ahRFwYRVszAWJw+ccwQjYUgEAlk7DAf38+QBYEH+hQr9fTWqXNE8BMAEa\nDuj3a0nt7c1TAACTdkt07364V2ki9ndUdM+R56QAMCputxy+k6N7jr5YmghI2VIBxuzEpPa/zVMA\nM2k4gDG7T1LTcMAAaTggd3JS+0bzFMxihQNGQsMBuTOT2nnNUzBL1nBc1jwFMJOGA3KnJ7UPN0/B\nLLZUABi17A6VQ0sTkcnOk99RgQHyBxNyfhBsHJwnGAlbKgDA0mk4AICl03BA17FJ7dbmKQAmRMMB\nXY9Oap9qngJgQjQc0PWopPaZ5imY5YFJ7evNUwCbouGArqzhuKB5CmZ5eFL7XPMUwKZoOKDrZ5Pa\n+a1DMNMjktqFzVMAm6LhgK7sOQ7XN0/BLFY4ABi17OmVDE92nu5Qmgjo5Yl80OXplePgPMGI2FIB\nAJZOwwHrHZHUbKkAbJOGA9Z7WFK7qHkKZvHLvTAyGg5Yb2dS+8/mKZjljKTmllgYMA0HrPeQpHZx\n8xTM8vik9uHmKYBN03DAevdPal9onoJZNBwAjNrV0X22w47SRGQ8KwVGxj3rsJ5nO4yD8wQjY0sF\nAFg6DQcAsHQaDmBsHpvUvtg6BLA1Gg5gbH4pqf1T8xQAsA3ufhi+K6J7jn6mNBEwk6u6YT13Pwyf\ncwQjZEsFAFg6DQesuVtSu7p5CoAJ0nDAmmOT2nebp2AjJyW1a5unALZMwwFrjklqGo5hye5QeVfz\nFMCWaThgjRWO4fvFpPbe5imALdNwwBoNx/A9LKl9oHkKYMs0HLDmqKR2TfMUABOk4YA1hyW1G5qn\nAJggDQesOTSpaTiG4/Sk9pXmKYC5aDhgjYZj2J6V1N7aPAUwFw0HrNFwDNszkpqGA0ZCwwFrDk5q\nNzdPQZ/s76v/a54CmIuGA9bclNSyVQ8AtkjDAWtuTGqHNE9B5u7VAYDt0XDAGiscw/XbSe3dzVMA\nc9NwwJpshUPDMQxnJ7U/b54CmJuGA9Z8L6ndtXkKMocntc82TwHMTcMBa76V1HY0TwEwQRoOWHNV\nUrPCUe/MpHZ18xQAsCAnRsSe/Q6Pzq73keielxeXJgKAbTgiuhPbdaWJiOiekz2R/9AeMGAHVAeA\ngdmT1Pw5qeWcwAS4hgMYsp+sDgAAy5At31Pn3Oiej/eXJgKABdBwDEt2PnaWJgLmYh8U1nO9wLA4\nHzARruEAhuoR1QEAYFlsqQzH+dE9F2+sDAQAi7I7upPcT5QmWl1Z8+euFRgpWyqw3heS2kObp6DP\n96sDAPPRcMB6lya1BzZPwdOS2o3NUwALo+GA9f4rqWk42ntDUntp8xQAsCRPiu51Ax8qTbSaXLwL\nwKSdEN2Jzk+ht/WQ0HAAsAJMdrUuje74v6M0EQAsgYajVjb+h5cmArbNRaPAkNy1p3590xQA0IAV\njjofj+7Yf7Q0EQAsyTXRnfT8rkcbWbPXt+oBjIgtFej6YFJ7XPMUq6fvOo2rmqYAlkLDAV3ZczdO\na55i9WSNXvYgNgCYhB3RXda/tTTRasi2U+5XmggAlsyFo22dEcYcgBVk8mvrpuiO99tLEwFAA1nD\ncUxpomnLxvuA0kTAQrloFHKXJLWnN0+xGs7pqVtVAmDyXhrdb9z/XppourLVjbMqAwFAK8eF6zha\nOD6MMwArzkS4fD+I7hh/tTIQALSm4Vi+bIzvWZoIABr7WnQnw2eXJpqWT4amDgDiBdGdDC8tTTQt\nWbPxtNJEAFDgwPANfFleHcYWAH7MpLgc2bj2PY8DACbv1uhOjKeUJhq/M0MjBwDr/EV0J8Z3lyYa\nv6zZ2FWaCACK3Tt8G1+knZGP58GVoQBgCDQci5ON5Q9LEwHAQNwQ3UnyOaWJxumkyBuOoypDAcBQ\nvDC6k+SPShONU3YB7nWliQBgYGyrbM+9Ih/D4ypDAcDQZJPlCZWBRiYbv2tLEwHAAH08uhPml0sT\njcc9wuoGAGzKPcO2yrxcuwEAW5A1HM8sTTR8j4583HZUhgKAIfu76E6cu0sTDV/WbHy/NBEAjIBt\nlc17ceTjdVhlKAAYg93RnUDfU5pouLJm40uliQBgJJ4dVjk2Y1cYJwDYlmwiPbc00bDsiHyMXlMZ\nCgDGJvvJet/e12RjY3wAYA6+wefOjXxsdlaGAoCx+tvwLX5/R0c+JldWhgKAscsm13eVJqplKwUA\nluCtkU+wh1SGKnJxeBIrACxNNsmu2q+gnhr5OHy7MhQATMkzIp9sH1UZqjFbKQDQwC2xuhPu9ZF/\n9odXhgKAKToy8kn30spQDbwh8s99YWUoAJiyT0c++Z5ZGWqJjglbKQBQom8CPrAy1JL0fdY7VIYC\ngFWwM/JJeHdlqCV4e+Sf8yWVoQBglXwk8sn4i5WhFuhOkX++H1WGAoBVtDvySfmDlaEWxHUbADAQ\nB0f/xPzqwlzb9e7IP9PzKkMBwCo7Lfqbjl8pzDWvu4WtFAAYpN+L/qbjxYW55mErBQAG7G3RP1m/\nrzDXVlwSef6zCjMBAPv5j+hvOoZ+98pvRp7bD7MBwAD1/Xz77cdhddF63TdspQDA6LwpNm46hnS3\nx0HRn/NhhbkAgE14emzcdHwzIg4oS7fXRs3G2wpzAQBb8KDYuOnYE3tXQ6r0ZfpaYSYAYE4/jNmN\nxx82zNP3WzB7Ynq/BwMAK+VPY3bTcfvqwl2WmOMdM94fABi5Y6P/91f6VhveGItpQPp++VWzAQAT\n9bzYfNORHVfG3pWKF0XEz0fEkbe97hGx9xbXx0bEn0XE5Vt4TQBgoi6K7TUeizhcIAoAK+JlUdNs\nvLzFhwMAhuX42Pt8jmU3Gv/a6gMBAMN3VkT8TyymybgqIp7VND2wkqqfaAgsxikRcWZEnBgR94qI\nEyLi3rf9uxsi4ju3Hbti750pH2sfEQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbp\n/wEhsy3ZGuy6kwAAAABJRU5ErkJggg==\n",
		"riskrepositoryid": 2000000004947,
		"isselect": 0,
		"ver": 1,
		"created_dt": "2020-06-03 17:11:35",
		"measurecode": "gzxk02",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 1,
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "gzqaqcs",
		"updated_dt": "2020-06-03 17:11:35",
		"worktaskmeasureid": 2000000046607,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#个人防护

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/ppeAudit.json?workticketid=%d&workType=xkz&tabtype=ppe"%(num3)
data = {
	"mainAttributeVO": {},
	"voList": [{
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "安全眼镜",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000100,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012300,
		"equipmentcode": "aqyj",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 1
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "全封闭眼罩",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000101,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012301,
		"equipmentcode": "qfbyz",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "焊接护目镜",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000102,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012302,
		"equipmentcode": "hjhmj",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "安全帽",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000103,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012303,
		"equipmentcode": "aqm",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "防静电服装",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000104,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012304,
		"equipmentcode": "fjdfz",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "护耳",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000105,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012305,
		"equipmentcode": "he",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "安全鞋",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000106,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012306,
		"equipmentcode": "aqx",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "防毒面罩",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000107,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012307,
		"equipmentcode": "fdmz",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "正压式呼吸器",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000108,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012308,
		"equipmentcode": "zyshxq",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "防化服",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000109,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012309,
		"equipmentcode": "fhf",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "手套",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000110,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012310,
		"equipmentcode": "st",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "绝缘服",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000111,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012311,
		"equipmentcode": "jyfz",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "防弧面具",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000112,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012312,
		"equipmentcode": "fhmj",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "安全带",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000113,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012313,
		"equipmentcode": "aqd",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "安全绳",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000114,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012314,
		"equipmentcode": "aqs",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "逃生设施",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000115,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012315,
		"equipmentcode": "tsss",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "人员培训已完成",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000116,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012316,
		"equipmentcode": "rypx",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}, {
		"isselect": 0,
		"ver": 1,
		"df": 0,
		"created_dt": now,
		"ismust": 1,
		"equipmentname": "其他（）",
		"dataStatus": 0,
		"worktype": "xkz",
		"isshowphoto": 0,
		"personequipmentid": 2000000000117,
		"created_by": 1000,
		"tableName": "hse_work_task_equipment",
		"worktaskequipmentid": 2000000012317,
		"equipmentcode": "qtfh",
		"updated_dt": now,
		"updated_by": 1000,
		"tenantid": 1,
		"workticketid": num5,
		"worktaskid": num2,
		"isconfirm": 0
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#会签前检查

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/beforeSignValidate.json?workticketid=%d"%(num3)
rs = requests.get(url = url,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#申请人会签

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=xkz&worklevel=&datatype=sign&actionCode=sign"%(num3)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000005636",
		"latitude": 39.982701,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"alarm_type": "nextstep_alarm",
		"electronicSignature": [{
			"imgStr": "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\nXxf7AAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "申请人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nXxf7AAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.337833
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#批准人会签

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=xkz&worklevel=&datatype=sign&actionCode=sign"%(num3)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000005637",
		"latitude": 39.982701,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"alarm_type": "nextstep_alarm",
		"electronicSignature": [{
			"imgStr": "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\nRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "批准人",
		"audittype": "sign,face,card",
		"specialworktype": "",
		"value": "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\nRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 3,
		"longitude": 116.337833
	}]
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#作业票关闭申请人

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketAudit.json?actionCode=close&workticketid=%d"%(num3)
data = {
	"reason": "已经完工",
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000005642",
		"latitude": 39.982738,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"alarm_type": "nextstep_alarm",
		"electronicSignature": [{
			"imgStr": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAt8SURBVHic7d3Pi15XGQfwk8YocRHbaqJVF7VZVCKlKoYiVNAqtqBCEKy6UKMLBVEQ\n/wj/BxeuFDcN6MIuLJKq2CKaQGkjEUvSRZHS+qNVG02sybgINJO5z8y8M3fOc+499/OBLPKsvpt5\n+fKe55y3FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nmKIvl1LW1v0DANhzaxv+PdI2DkzPvtYBADoQfavh8xXWuaV1AACgfwoHwHiXgtlH0lPAhCkcAON9\nP5jdn54CJkzhABjvTDD7QHoKmDCFA2C8C8Hs3ekpYMIUDoDx/hrMDqengAlTOADG+1swuz09BUyY\nwgEw3pVg9sb0FDBhCgfAeFeDmcIB63gJD2BveG0UtuAbDoDx3hDMXktPAROmcACM96ZgFu11wGIp\nHADjRfsal9NTwIQpHADjHQxm/0lPAROmcACM95Zg9o/0FDBhCgfAeLcGM4UD1lE4AMZTOGAbCgfA\neNGRyivpKWDCFA6A8aIfans5PQVMmMIBMN6RYPZSegqYMIUDYLy3BzOFA9ZROADG8w0HbEPhABhP\n4YBtKBwA470jmL2YngIA6Nrlcv3n6df/e3PTRDAx+1oHAOjAWjDz+QrrOFIBAKpTOACA6hQOAKA6\nhQMAqE7hAACqUzgAgOoUDgCgOoUDYJzoga/oXQ5YNIUDYJyjweyP6Slg4hQOgHGiwnEhPQVMnMIB\nMM6xYPan9BQwcQoHwDj3BLNz6Slg4hQOgHGiwvFMegoAoGvXyvCn6Q80TQQT5OeTAcbx0/SwAkcq\nAEB1CgcAUJ3CAQBUp3AAANUpHAC7d2cweyk7BMyBwgGwe8eD2e/TU8AMKBwAuxcVjjPpKWAGFA6A\n3fMNBwBQ3aUyfGX0SNNEMFFewwPYPa+MwoocqQAA1SkcAEB1CgcAUJ3CAbA70XLo/9JTwEwoHAC7\nc38w+3V6CpgJhQNgd6LC8UR6CpgJhQNgd6LC8Zv0FABA166V4aNfB5smggnzQA3A7nj0C3bAkQoA\nUJ3CAQBUp3AA7Nz+1gFgbhQOgJ37ZDA7k54CZkThANi5B4LZ6fQUAEDXzpbhldgHmyYCALqzsWys\nFXsdsCV3xgF2zhscsEN2OACA6hQOAKA6hQNgZ+4KZlfSU8DMKBwAOxPdRnk0PQXMjMIBsDPRo1+P\npacAALp2uQyvxN7ZMhDMgWtcADvjSizsgiMVAKA6hQMAqE7hAFjdW1sHgLlSOABW96lg9nh6Cpgh\nhQNgdZ8OZt7gAAD2VHQl9u6miWAmXOUCWJ0rsbBLjlQAgOoUDgCgOoUDYDVHg5lfiYUVKRwAq4mu\nxLqhAitSOABWE12J/Vl6CgCgaxuvw66VUg43TQQz4joXwGpciYURHKkAANUpHABAdQoHwPYeCmbn\n01PAjCkcANs7Ecx+kp4CAOjaC2V4Q+V400QwMzasAbbnhgqM5EgFAKhO4QAAqlM4ALZ2LJj9Kz0F\nzJzCAbC1zwezU+kpAICunS/DGyrRuxzAFmxZA2zNDRXYA45UAIDqFA4AoDqFA2Bz9wazS+kpoAMK\nB8DmHg5mP05PAQB07dkyvKHyiaaJYKZsWgNszg0V2COOVACA6hQOAKA6hQMg9mAwu5ieAjqhcADE\nvhTMfpieAgDo2tUyvKFytGkimDHb1gAxN1RgDzlSAQCqUzgAhu5oHQB6o3AADEULoz9NTwEAdO1c\nGS6MfrZpIpg5C1AAQxZGYY85UgEAqlM4AG7mcxEq8IcFcLOTwexMdggAoG9PluHC6DeaJgIAurOx\nbKyVUg40TQQdsHUNcDM3VKACOxwAQHUKB8ANDwez8+kpAICuPVaG+xvfbZoIAOhOtDB6sGki6IRF\nKIAbLIxCJXY4AK7zeQgV+QMDuO4rweyZ9BQAQNfOFC+MQjXOJgGui/Y39pdSrmUHgR4pHADXWRiF\niuxwAJRyqHUA6J3CAVDKN4PZL9JTAABde74MF0ZPNE0EnXE+CWB/A6pzpAIAVKdwAEt3tHUAWAKF\nA1i6bwWzH6WnAAC69t8yXBi9r2ki6JClKGDpLIxCAkcqAEB1CgewZB8NZv/MDgEA9O1UGe5vfK9p\nIgCgOxvLxlop5W1NE0GnLEYBS2ZhFJLY4QAAqlM4gKX6YjA7n54CAOjar8pwf+PbTRMBAN2JFkYP\nNE0EHbMcBSyVhVFIZIcDWCKffZDMHx2wRF8LZr9LTwEAdO1sGe5vnGwZCHrnvBJYomh/Y38p5Vp2\nEFgKhQNYIgujkMwOB7A0rr5CAwoHsDRfD2an01MAAF17qgwXRr/QNBEsgDNLYGnsb0ADjlQAgOoU\nDmBJfOZBI/74gCX5ajB7Mj0FANC135bhwmhUQoA9ZlEKWBIvjEIjCgewJG6oQCN2OACA6hQOYCk+\nF8yeSk8BAHTt0TJcGP1O00QAQHc2lo21UsqtTRPBgliWApbCwig0ZIcDAKhO4QCW4Hgw+3d6Clgw\nhQNYgpPB7AfZIQCAvl0qw4XRDzZNBAtjYQpYAguj0JgjFQCgOoUD6J3POZgAf4hA704Es7PpKWDh\nFA6gd9FvqDySngIA6NqVMryhcrRpIlggW9pA79xQgQlwpAIAVKdwAADVKRxAzz4TzJ5OTwEoHEDX\nohsqp9JTAABdi26ovLdpIlgom9pAz9xQgYlwpAIAVKdwAADVKRxArx4KZufTUwClFIUD6JcbKgBA\nda+W4Q2Ve5omggWzrQ30yg0VmBBHKgBAdQoHAFCdwgH06FAwu5qeAnidwgH06OPB7JfZIYAbFA6g\nRx8LZqfTUwAAXTtXhldiP9w0ESycK2JAj1yJhYlxpAIAVKdwAADVKRwAQHUKB9CbdwWzK+kpgJso\nHEBvoiuxP09PAdxE4QB680Awezw9BQDQtefK8A2Oe5smAtxLB7rjDQ6YIEcqAEB1CgcAUJ3CAQBU\np3AAPbk7mL2YngIYUDiAntwXzJ5ITwEMKBxATz4UzM6kpwAGFA6gJwoHAFDda2X46NdtTRMBpRSP\n4QB98egXTJQjFQCgOoUDAKhO4QAAqlM4gF7Y1YAJUziAXrw/mD2bngIIKRxAL94XzJ5OTwGEFA6g\nF1Hh+EN6CiCkcAC9iArHufQUAEDXLpThK6PHmiYCXmerG+hF9MroLZvMgWSOVICeKRswEQoHAFCd\nwgEAVKdwAADVKRwAQHUKBwBQncIB9OBIMHslPQWwKYUD6MF7gtnF9BTAphQOoAd3BbPn0lMAm1I4\ngB74hgMmTuEAeuAbDpg4hQPogW84YOIUDqAHdwSzF9JTAJtSOIAeRNdiX0xPAWzKz9MDPYh+Fdbn\nG0yIbzgAgOoUDgCgOoUDAKhO4QAAqlM4AIDqFA4AoDqFAwCoTuEAAKpTOACA6hQOAKA6hQMAqE7h\nAACqUzgAgOoUDmDuDgWzV9NTAFtSOIC5uz2YvZyeAtiSwgHM3W3B7O/pKYAtKRzA3PmGA2ZA4QDm\nLvqGQ+GAiVE4gLmLvuFwpAITo3AAc+dIBWZA4QDm7i/B7Pn0FMCW9rUOALAH1jb832cbALDn3llK\n+XMp5WIp5XDjLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAs/B//NplwaK5Vx8AAAAASUVO\nRK5CYII=\n",
			"uuid": ""
		}],
		"name": "申请人",
		"audittype": "sign,card",
		"specialworktype": "",
		"value": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAt8SURBVHic7d3Pi15XGQfwk8YocRHbaqJVF7VZVCKlKoYiVNAqtqBCEKy6UKMLBVEQ\n/wj/BxeuFDcN6MIuLJKq2CKaQGkjEUvSRZHS+qNVG02sybgINJO5z8y8M3fOc+499/OBLPKsvpt5\n+fKe55y3FAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nmKIvl1LW1v0DANhzaxv+PdI2DkzPvtYBADoQfavh8xXWuaV1AACgfwoHwHiXgtlH0lPAhCkcAON9\nP5jdn54CJkzhABjvTDD7QHoKmDCFA2C8C8Hs3ekpYMIUDoDx/hrMDqengAlTOADG+1swuz09BUyY\nwgEw3pVg9sb0FDBhCgfAeFeDmcIB63gJD2BveG0UtuAbDoDx3hDMXktPAROmcACM96ZgFu11wGIp\nHADjRfsal9NTwIQpHADjHQxm/0lPAROmcACM95Zg9o/0FDBhCgfAeLcGM4UD1lE4AMZTOGAbCgfA\neNGRyivpKWDCFA6A8aIfans5PQVMmMIBMN6RYPZSegqYMIUDYLy3BzOFA9ZROADG8w0HbEPhABhP\n4YBtKBwA470jmL2YngIA6Nrlcv3n6df/e3PTRDAx+1oHAOjAWjDz+QrrOFIBAKpTOACA6hQOAKA6\nhQMAqE7hAACqUzgAgOoUDgCgOoUDYJzoga/oXQ5YNIUDYJyjweyP6Slg4hQOgHGiwnEhPQVMnMIB\nMM6xYPan9BQwcQoHwDj3BLNz6Slg4hQOgHGiwvFMegoAoGvXyvCn6Q80TQQT5OeTAcbx0/SwAkcq\nAEB1CgcAUJ3CAQBUp3AAANUpHAC7d2cweyk7BMyBwgGwe8eD2e/TU8AMKBwAuxcVjjPpKWAGFA6A\n3fMNBwBQ3aUyfGX0SNNEMFFewwPYPa+MwoocqQAA1SkcAEB1CgcAUJ3CAbA70XLo/9JTwEwoHAC7\nc38w+3V6CpgJhQNgd6LC8UR6CpgJhQNgd6LC8Zv0FABA166V4aNfB5smggnzQA3A7nj0C3bAkQoA\nUJ3CAQBUp3AA7Nz+1gFgbhQOgJ37ZDA7k54CZkThANi5B4LZ6fQUAEDXzpbhldgHmyYCALqzsWys\nFXsdsCV3xgF2zhscsEN2OACA6hQOAKA6hQNgZ+4KZlfSU8DMKBwAOxPdRnk0PQXMjMIBsDPRo1+P\npacAALp2uQyvxN7ZMhDMgWtcADvjSizsgiMVAKA6hQMAqE7hAFjdW1sHgLlSOABW96lg9nh6Cpgh\nhQNgdZ8OZt7gAAD2VHQl9u6miWAmXOUCWJ0rsbBLjlQAgOoUDgCgOoUDYDVHg5lfiYUVKRwAq4mu\nxLqhAitSOABWE12J/Vl6CgCgaxuvw66VUg43TQQz4joXwGpciYURHKkAANUpHABAdQoHwPYeCmbn\n01PAjCkcANs7Ecx+kp4CAOjaC2V4Q+V400QwMzasAbbnhgqM5EgFAKhO4QAAqlM4ALZ2LJj9Kz0F\nzJzCAbC1zwezU+kpAICunS/DGyrRuxzAFmxZA2zNDRXYA45UAIDqFA4AoDqFA2Bz9wazS+kpoAMK\nB8DmHg5mP05PAQB07dkyvKHyiaaJYKZsWgNszg0V2COOVACA6hQOAKA6hQMg9mAwu5ieAjqhcADE\nvhTMfpieAgDo2tUyvKFytGkimDHb1gAxN1RgDzlSAQCqUzgAhu5oHQB6o3AADEULoz9NTwEAdO1c\nGS6MfrZpIpg5C1AAQxZGYY85UgEAqlM4AG7mcxEq8IcFcLOTwexMdggAoG9PluHC6DeaJgIAurOx\nbKyVUg40TQQdsHUNcDM3VKACOxwAQHUKB8ANDwez8+kpAICuPVaG+xvfbZoIAOhOtDB6sGki6IRF\nKIAbLIxCJXY4AK7zeQgV+QMDuO4rweyZ9BQAQNfOFC+MQjXOJgGui/Y39pdSrmUHgR4pHADXWRiF\niuxwAJRyqHUA6J3CAVDKN4PZL9JTAABde74MF0ZPNE0EnXE+CWB/A6pzpAIAVKdwAEt3tHUAWAKF\nA1i6bwWzH6WnAAC69t8yXBi9r2ki6JClKGDpLIxCAkcqAEB1CgewZB8NZv/MDgEA9O1UGe5vfK9p\nIgCgOxvLxlop5W1NE0GnLEYBS2ZhFJLY4QAAqlM4gKX6YjA7n54CAOjar8pwf+PbTRMBAN2JFkYP\nNE0EHbMcBSyVhVFIZIcDWCKffZDMHx2wRF8LZr9LTwEAdO1sGe5vnGwZCHrnvBJYomh/Y38p5Vp2\nEFgKhQNYIgujkMwOB7A0rr5CAwoHsDRfD2an01MAAF17qgwXRr/QNBEsgDNLYGnsb0ADjlQAgOoU\nDmBJfOZBI/74gCX5ajB7Mj0FANC135bhwmhUQoA9ZlEKWBIvjEIjCgewJG6oQCN2OACA6hQOYCk+\nF8yeSk8BAHTt0TJcGP1O00QAQHc2lo21UsqtTRPBgliWApbCwig0ZIcDAKhO4QCW4Hgw+3d6Clgw\nhQNYgpPB7AfZIQCAvl0qw4XRDzZNBAtjYQpYAguj0JgjFQCgOoUD6J3POZgAf4hA704Es7PpKWDh\nFA6gd9FvqDySngIA6NqVMryhcrRpIlggW9pA79xQgQlwpAIAVKdwAADVKRxAzz4TzJ5OTwEoHEDX\nohsqp9JTAABdi26ovLdpIlgom9pAz9xQgYlwpAIAVKdwAADVKRxArx4KZufTUwClFIUD6JcbKgBA\nda+W4Q2Ve5omggWzrQ30yg0VmBBHKgBAdQoHAFCdwgH06FAwu5qeAnidwgH06OPB7JfZIYAbFA6g\nRx8LZqfTUwAAXTtXhldiP9w0ESycK2JAj1yJhYlxpAIAVKdwAADVKRwAQHUKB9CbdwWzK+kpgJso\nHEBvoiuxP09PAdxE4QB680Awezw9BQDQtefK8A2Oe5smAtxLB7rjDQ6YIEcqAEB1CgcAUJ3CAQBU\np3AAPbk7mL2YngIYUDiAntwXzJ5ITwEMKBxATz4UzM6kpwAGFA6gJwoHAFDda2X46NdtTRMBpRSP\n4QB98egXTJQjFQCgOoUDAKhO4QAAqlM4gF7Y1YAJUziAXrw/mD2bngIIKRxAL94XzJ5OTwGEFA6g\nF1Hh+EN6CiCkcAC9iArHufQUAEDXLpThK6PHmiYCXmerG+hF9MroLZvMgWSOVICeKRswEQoHAFCd\nwgEAVKdwAADVKRwAQHUKBwBQncIB9OBIMHslPQWwKYUD6MF7gtnF9BTAphQOoAd3BbPn0lMAm1I4\ngB74hgMmTuEAeuAbDpg4hQPogW84YOIUDqAHdwSzF9JTAJtSOIAeRNdiX0xPAWzKz9MDPYh+Fdbn\nG0yIbzgAgOoUDgCgOoUDAKhO4QAAqlM4AIDqFA4AoDqFAwCoTuEAAKpTOACA6hQOAKA6hQMAqE7h\nAACqUzgAgOoUDmDuDgWzV9NTAFtSOIC5uz2YvZyeAtiSwgHM3W3B7O/pKYAtKRzA3PmGA2ZA4QDm\nLvqGQ+GAiVE4gLmLvuFwpAITo3AAc+dIBWZA4QDm7i/B7Pn0FMCW9rUOALAH1jb832cbALDn3llK\n+XMp5WIp5XDjLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAs/B//NplwaK5Vx8AAAAASUVO\nRK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.338465
	}],
	"mainAttributeVO": {},
	"closeType": "completion"
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']

#作业票关闭批准人

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketAudit.json?actionCode=close&workticketid=%d"%(num3)
data = {
	"reason": "已经完工",
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000005641",
		"latitude": 39.982738,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 1,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "批准人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 3,
		"longitude": 116.338465
	}],
	"mainAttributeVO": {},
	"closeType": "completion"
}
rs = requests.post(url = url,json=data,headers=headers)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)

print(data)
#获取接口返回状态
status= data['status']