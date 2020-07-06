#a安全分析增删改查
import json
import requests
from globalpkg.global_var import *
from tools.tool import *

#临时cookies
cookies={'JSESSIONID': '719FF49AB0E6CB255165409E8ACB4C9Fqoevbc'}
print(cookies)
name = ran_name_with_str()
print("作业预约名称",name)


#开始作业预约
#拼写预约URL
work_appoint_id_l = sql_query_work_appointid+1
print("作业预约NEW ID:",work_appoint_id_l)
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.3707947936681053&contentType=json&ajax=true&tid=1'%(work_appoint_id_l,work_appoint_id_l)
#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': 'bd95a01c276341b89715228e81d0ca3f',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }
#作业许可大票数据
data = {
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
	"specialenvironment": "ALLNOT",
	"task_worktype_code": "QT",
	"task_worktype_name": "其他",
	"cywlqfyxzz": "0",
	"isdzdh": "0",
	"projecttype": "rcjx",
	"isupgradedh": "0",
	"persistent_type": "newoperation",
	"issjtssxzy": "0",
	"worklevel_dh": "",
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
	"worktypename": "作业许可证",
	"worktype": "xkz",
	"appointstarttime": starttime,
	"appointendtime": endtime,
	"material_medium": "物料介质123",
	"risksmeasures": "重点防控的风险123"
}
#请求作业预约保存接口
rs=requests.post(url2, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
#获取接口返回状态
sta= data['status']
if sta == 3200:
    print("作业预约成功", sta)
else:
    print("rulst",data)

    ####

#送交用例信息
casename = '作业预约送交'
#送交接口地址
url3='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(work_appoint_id_l,work_appoint_id_l)
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

    print("作业预约送交", status)
    #caseinfo['result'] = 1
#else:
    #caseinfo['result'] = 0
#收集用例执行信息
#testsuit.append(caseinfo.copy())
#作业预约审批用例信息

casename = '作业预约审批'
# count =count+1
# caseid = count
# caseinfo['id'] = caseid
# caseinfo['name'] = casename
#审批接口地址
url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(work_appoint_id_l)
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

    print("作业预约审批", status)
    #caseinfo['result'] = 1

#print(cc)
#安全分析第一个保存用例信息
#caseid = 5
casename = '安全分析及交底保存'


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

	"work_appoint_id": work_appoint_id_l,
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


#获取安全分析接口用例信息
#caseid = 6
casename = '获取安全分析列表'


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


#print (b)
jsaid_l = jsaid+1
print ("安全分析列表使用ID jsaid_l:",jsaid_l)

#安全分析步骤添加
#安全分析步骤添加接口用例信息
#caseid = 7
casename = '安全分析步骤添加'

#url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.5426692795870303&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid_l)
url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.8939960513657317&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid_l)
data = {
	"tableName": "hse_safety_analysis_step",
	"qualify_level": "no_qualify",
	"duty_name": "",
	"jsaid": jsaid_l,
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

    print("安全分析步骤添加", status)

#time.sleep(5)
#安全分析保存
#安全分析步保存加接口用例信息

casename = '安全分析保存'

#jsaid_l = jsaid_l
print("jsaid_l:",jsaid_l)
#url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.2955948527813328&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid_l,jsaid_l)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.09494809285755568&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid_l,jsaid_l)
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
	"jsaid": jsaid_l,
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
	"worktaskid": jsaid_l,
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

    print("安全分析保存", status)

#安全分析删除


casename = '安全分析删除'

#jsaid_l = jsaid_l
#print("jsaid_l:",jsaid_l)
#url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.2955948527813328&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid_l,jsaid_l)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.09494809285755568&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid_l,jsaid_l)
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.2463658272702205&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid_l)
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.2964446119500741&contentType=json&ajax=true&tid=1'%(jsaid_l,jsaid)
data = [jsaid_l]
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

    print("安全分析删除", status)