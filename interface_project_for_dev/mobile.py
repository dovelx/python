#手机端主流程 预约，审批。pc安全，手机安全交底签字
import requests
import json
#from globalpkg.global_var import work_appoint_id
# from tools import tool
# from globalpkg.global_var import tsi
from globalpkg.global_var import workticketid
# from globalpkg.global_var import worktaskid
#from case.case1 import *
from tools import tool
from globalpkg.global_var import jsaid
from globalpkg.global_var import safeclarid
#from globalpkg.global_var import sql_query_work_appointid
#from runners.runner2 import inse
from runners import m_login
from case import datas
from runners import pc_login
from tools import mname
from tools import msql
from tools import getdata
from globalpkg.global_var import *
from htmlreporter import HtmlReport
from globalpkg.global_var import executed_history_id
import configparser


#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime

#作业预约名称
name = mname.name
print(name)

case = '手机全流程'

#用例信息变量定义
testsuitm = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

#ps
mheaders = m_login.mlogin(1, 1, 1)
headers = datas.headers
cookies = pc_login.cookies

#cases
caseinfo['id'] = 100
caseinfo['name'] = '获取insertid'
caseinfo['flag'] = 'get'
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardAdd.json'
caseinfo['url'] = url

# 记录测试开始时间
start_time = datetime.datetime.now()# 记录测试开始时间
start_time = datetime.datetime.now()

rs = requests.get(url=caseinfo['url'], headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
# json化
data = json.loads(data)
# 获取接口返回状态
#print("data", data)
sta = data['status']
if sta == 3200:
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#
insert = data['data']['data']['insert__']

print('获取insertid',sta)

#收集用例执行信息
testsuitm.append(caseinfo.copy())

#作业预约

url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardSave.json"
data = {
	"add_attachs": [],
	"del_attachs": [],
	"vo": {
		"equt_name": "",
		"df": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"wf_instance": "",
		"specialenvironment": "ALLNOT",
		"cywlqfyxzz": "1",
		"jsa_code": "",
		"sbzd": "",
		"tableName": "hse_work_appoint",
		"insert__": insert,
		"sourcefunc": "",
		"territorialunitid": 2000000003339,
		"territorialdevicename": "制氢装置",
		"sourcetype": "",
		"territorialunitname": "运行一部",
		"worktypename": "作业许可证,动火作业,受限空间,高处作业,吊装作业,管线/设备打开,挖掘作业,断路作业,临时用电,射线作业,承包商作业,脚手架作业,非计划性维修工作,交叉作业,屏蔽报警、解除连锁和安全应急设备,偏离规则/程序要求的工作,没有安全程序可遵循的工作,其他,清洗作业",
		"equipmentnumber": "",
		"ver": 1,
		"appointstarttime": starttime,
		"task_worktype_name": "储罐浮舱内",
		"dataStatus": 0,
		"standardmaintenance": "",
		"wf_type": "",
		"workunit": 1688712,
		"worklevel_dz": "mcq_dz_workLevel01",
		"workcontent": "不知道",
		"status": "draft",
		"wf_audit_state": "",
		"task_worktype_code": "GCN",
		"territorialdeviceid": 2000000003454,
		"appointendtime": endtime,
		"worktaskid_no": 0,
		"work_position_name": "制氢北区",
		"isreport": "1",
		"wf_current_user": "",
		"wf_audit_time": "",
		"worklevel_dh": "mcq_dh_workLevel01",
		"sourcecode": "",
		"iscontractor": "0",
		"equipmentcode": "",
		"jsaid": "",
		"tenantid": 1,
		"projecttype": "dx",
		"sourceid": "",
		"worklevel_gx": "",
		"created_dt": now,
		"wf_current_nodeid": "",
		"worktype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
		"work_appoint_id": "",
		"worklevel_sx": "mcq_sx_workLevel01",
		"work_position_id": 2000000002019,
		"wf_create_user": "",
		"risksmeasures": "不知道",
		"material_medium": "艾伦",
		"issjtssxzy": "1",
		"isupgradedh": "1",
		"isdzdh": "1",
		"worklevel_gc": "mcq_gc_workLevel01",
		"updated_dt": now,
		"persistent_type": "newoperation",
		"worksite": "作业地点",
		"territorialunitcode": "CS8082020"
	}
}
caseinfo['id'] = 101
caseinfo['name'] = '作业预约'
caseinfo['url'] = url
caseinfo['data'] =data

rs = requests.post(url = caseinfo['url'],json=caseinfo['data'],headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#作业预约送交

work_appoint_idx = getdata.get_work_appoint_id(cookies,name)
print("work_appoint_idx",work_appoint_idx)
#work_appoint_idx = int(work_appoint_idx)
#Url
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfSend.json?dataId=%d&ts='%(work_appoint_idx)
data= {"nodeStr":"2000000009070","opinion":"申请审批","2000000009070":"海顿测试","2000000009070_id":"1000","cCName":"","cC":""}
caseinfo['id'] = 102
caseinfo['name'] = '作业预约送交'
caseinfo['url'] = url
caseinfo['data'] =data
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#作业预约审核
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfFinish.json?dataId=%d&ts='%(work_appoint_idx)

data ={"cC":"1000","nickName":"用户","nodeStr":"","opinion":"同意","cCName":"海顿测试","is_normal_finish":'true'}
caseinfo['id'] = 103
caseinfo['name'] = '作业预约审核'
caseinfo['url'] = url
caseinfo['data'] =data
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#安全分析及交底保存
casename = '安全分析及交底保存'
caseinfo['id'] = 104
caseinfo['name'] = casename
#urlfenxi ='http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK_RISK&0.6529845051499572&contentType=json&ajax=true&tid=1'
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK_RISK&0.9807925598389842&contentType=json&ajax=true&tid=1'
data = {
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
	"projecttype": "dx",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"workname": name,
	"work_appoint_id": work_appoint_idx,
	"workcontent": "不知道",
	"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
	"worktickettype_name": "作业许可证,动火作业,受限空间,高处作业,吊装作业,管线/设备打开,挖掘作业,断路作业,临时用电,射线作业,承包商作业,脚手架作业,非计划性维修工作,交叉作业,屏蔽报警、解除连锁和安全应急设备,偏离规则/程序要求的工作,没有安全程序可遵循的工作,其他,清洗作业",
	"workunitname": "长庆石化分公司",
	"workunit": 1688712,
	"planstarttime": starttime,
	"planendtime": endtime,
	"site": "作业地点",
	"equipmentname": "",
	"work_position_name": "制氢北区",
	"work_position_id": 2000000002019,
	"equipmentnumber": "",
	"equipmentcode": "",
	"constructionscheme": 0,
	"standardmaintenance": ""
}
rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#print(data)
# 获取接口返回状态
sta = data['status']

if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#安全分析步骤添加接口用例信息
#jsaidxx = jsaid+1
jsaidxx = getdata.get_safe_task_id(cookies,name)
print ("安全分析步骤添加使用ID:",jsaidxx)

casename = '安全分析步骤添加'
caseinfo['id'] = 105
caseinfo['name'] = casename
url ='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_STEP_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&0.8939960513657317&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {
	"tableName": "hse_safety_analysis_step",
	"qualify_level": "no_qualify",
	"duty_name": "",
	"jsaid": jsaidxx,
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
rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#安全分析步保存加接口用例信息
casename = '安全分析保存'
caseinfo['id'] = 106
caseinfo['name'] = casename
url='http://192.168.6.27:6030/hse/HSE_SAFETY_ANALYSIS_RISK/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.09494809285755568&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx,jsaidxx)
data = {
	"tableName": "hse_safety_analysis",

	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"jsaid": jsaidxx,
	"jsa_templete_name": "",
	"jsa_templete_id": "",
	"temp_type": "newWorkTask",
	"jsa_monitor_userid": 1000,
	"jsa_monitor_name": "测试用户",
	"jsa_menber_userids": "1000",
	"jsa_menber_username": "测试用户",
	"analyze_time": now,
	"worktickettype": "",
	"equip_stuff": "",
	"worktaskid": jsaidxx,
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
rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#安全交底，环境影响大
casename = '安全交底'
caseinfo['id'] = 107
caseinfo['name'] = casename
#safeclaridxx = safeclarid+1
safeclaridxx = jsaidxx
print ("送交ID:",safeclaridxx)
url='http://192.168.6.27:6030/hse/HSE_SAFETY_DISCLOSURE/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK_RISK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.7447101068947941&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx,safeclaridxx)

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
	"safeclarid": safeclaridxx,
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
	"worktaskid": jsaidxx,
	"work_position_id": 2000000002019
}
rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#安全送交接口用例信息

casename = '安全送交'
caseinfo['id'] = 108
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.9498759321537273&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {}
rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#手机安全交底模块

#安全送交审批-现场作业人员签字
casename = '安全送交审批-现场作业人员签字'
caseinfo['id'] = 109
caseinfo['name'] = casename
#url = 'http://192.168.6.27:6030/m/hse_m/HSE_SAFETY_DISCLOSURE_M/jsasignAudit.json?safe_name=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&safe_content=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&confirm_content=1%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E4%BD%9C%E4%B8%9A%E5%8C%BA%E5%9F%9F%E5%8F%8A%E5%91%A8%E8%BE%B9%E7%94%9F%E4%BA%A7%E4%BD%9C%E4%B8%9A%E6%83%85%E5%86%B5%0D%0A2%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%EF%BC%88JSA%EF%BC%89%0D%0A3%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%85%B7%E4%BD%93%E5%AE%89%E5%85%A8%E8%A6%81%E6%B1%82%EF%BC%88%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E4%B8%AD%E7%9A%84%E6%8E%A7%E5%88%B6%E6%8E%AA%E6%96%BD%EF%BC%89%0D%0A4%E3%80%81%E5%B7%B2%E5%AF%B9%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%8E%B0%E5%9C%BA%E5%AE%89%E5%85%A8%E6%8E%AA%E6%96%BD%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%A3%80%E6%9F%A5%E7%A1%AE%E8%AE%A4%0D%0A5%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%B6%89%E5%8F%8A%E7%9A%84%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E7%9A%84%E6%9C%89%E9%99%90%E6%9C%9F%E9%99%90%20%0D%0A6%E3%80%81%E5%B7%B2%E6%8E%8C%E6%8F%A1%E4%B8%AA%E4%BA%BA%E9%98%B2%E6%8A%A4%E7%94%A8%E5%85%B7%E6%AD%A3%E7%A1%AE%E4%BD%A9%E6%88%B4%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%0D%0A7%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E7%AA%81%E5%8F%91%E6%83%85%E5%86%B5%E4%B8%8B%E7%9A%84%E5%BA%94%E6%80%A5%E9%81%BF%E9%99%A9%E6%96%B9%E6%B3%95&additional_content=&workTicketid=2000000002028&worktaskid=2000000002028&workType=aqjd&actionCode=clarsign'
url = 'http://192.168.6.27:6030/m/hse_m/HSE_SAFETY_DISCLOSURE_M/jsasignAudit.json?safe_name=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&safe_content=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&confirm_content=1%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E4%BD%9C%E4%B8%9A%E5%8C%BA%E5%9F%9F%E5%8F%8A%E5%91%A8%E8%BE%B9%E7%94%9F%E4%BA%A7%E4%BD%9C%E4%B8%9A%E6%83%85%E5%86%B5%0D%0A2%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%EF%BC%88JSA%EF%BC%89%0D%0A3%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%85%B7%E4%BD%93%E5%AE%89%E5%85%A8%E8%A6%81%E6%B1%82%EF%BC%88%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E4%B8%AD%E7%9A%84%E6%8E%A7%E5%88%B6%E6%8E%AA%E6%96%BD%EF%BC%89%0D%0A4%E3%80%81%E5%B7%B2%E5%AF%B9%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%8E%B0%E5%9C%BA%E5%AE%89%E5%85%A8%E6%8E%AA%E6%96%BD%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%A3%80%E6%9F%A5%E7%A1%AE%E8%AE%A4%0D%0A5%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%B6%89%E5%8F%8A%E7%9A%84%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E7%9A%84%E6%9C%89%E9%99%90%E6%9C%9F%E9%99%90%20%0D%0A6%E3%80%81%E5%B7%B2%E6%8E%8C%E6%8F%A1%E4%B8%AA%E4%BA%BA%E9%98%B2%E6%8A%A4%E7%94%A8%E5%85%B7%E6%AD%A3%E7%A1%AE%E4%BD%A9%E6%88%B4%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%0D%0A7%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E7%AA%81%E5%8F%91%E6%83%85%E5%86%B5%E4%B8%8B%E7%9A%84%E5%BA%94%E6%80%A5%E9%81%BF%E9%99%A9%E6%96%B9%E6%B3%95&additional_content=&workTicketid='+str(jsaidxx)+'&worktaskid='+str(jsaidxx)+'&workType=aqjd&actionCode=clarsign'
data = {
	"mainAttributeVO": {
		"additional_content": ""
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006735",
		"latitude": 39.98272,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nQmCC\n",
			"uuid": ""
		}],
		"name": "现场作业人员",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nQmCC\n",
		"isbrushposition": 0,
		"disporder": 1,
		"longitude": 116.338469
	}]
}
#rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#print(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#安全送交审批-现场负责人签字
casename = '安全送交审批-现场负责人签字'
caseinfo['id'] = 110
caseinfo['name'] = casename

url = 'http://192.168.6.27:6030/m/hse_m/HSE_SAFETY_DISCLOSURE_M/jsasignAudit.json?safe_name=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&safe_content=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&confirm_content=1%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E4%BD%9C%E4%B8%9A%E5%8C%BA%E5%9F%9F%E5%8F%8A%E5%91%A8%E8%BE%B9%E7%94%9F%E4%BA%A7%E4%BD%9C%E4%B8%9A%E6%83%85%E5%86%B5%0D%0A2%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%EF%BC%88JSA%EF%BC%89%0D%0A3%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%85%B7%E4%BD%93%E5%AE%89%E5%85%A8%E8%A6%81%E6%B1%82%EF%BC%88%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E4%B8%AD%E7%9A%84%E6%8E%A7%E5%88%B6%E6%8E%AA%E6%96%BD%EF%BC%89%0D%0A4%E3%80%81%E5%B7%B2%E5%AF%B9%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%8E%B0%E5%9C%BA%E5%AE%89%E5%85%A8%E6%8E%AA%E6%96%BD%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%A3%80%E6%9F%A5%E7%A1%AE%E8%AE%A4%0D%0A5%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%B6%89%E5%8F%8A%E7%9A%84%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E7%9A%84%E6%9C%89%E9%99%90%E6%9C%9F%E9%99%90%20%0D%0A6%E3%80%81%E5%B7%B2%E6%8E%8C%E6%8F%A1%E4%B8%AA%E4%BA%BA%E9%98%B2%E6%8A%A4%E7%94%A8%E5%85%B7%E6%AD%A3%E7%A1%AE%E4%BD%A9%E6%88%B4%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%0D%0A7%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E7%AA%81%E5%8F%91%E6%83%85%E5%86%B5%E4%B8%8B%E7%9A%84%E5%BA%94%E6%80%A5%E9%81%BF%E9%99%A9%E6%96%B9%E6%B3%95&additional_content=&workTicketid='+str(jsaidxx)+'&worktaskid='+str(jsaidxx)+'&workType=aqjd&actionCode=clarsign'
data = {
	"mainAttributeVO": {
		"additional_content": ""
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006734",
		"latitude": 39.982727,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nS6W0wwAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "现场负责人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\nS6W0wwAAAABJRU5ErkJggg==\n",
		"isbrushposition": 0,
		"disporder": 2,
		"longitude": 116.338467
	}]
}
#rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#print(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#安全送交审批-作业教育人（项目负责人）签字
casename = '安全送交审批-作业教育人（项目负责人）签字'
caseinfo['id'] = 111
caseinfo['name'] = casename
#http://192.168.6.27:6030/m/hse_m/HSE_SAFETY_DISCLOSURE_M/jsasignAudit.json?safe_name=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&safe_content=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&confirm_content=1%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E4%BD%9C%E4%B8%9A%E5%8C%BA%E5%9F%9F%E5%8F%8A%E5%91%A8%E8%BE%B9%E7%94%9F%E4%BA%A7%E4%BD%9C%E4%B8%9A%E6%83%85%E5%86%B5%0D%0A2%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%EF%BC%88JSA%EF%BC%89%0D%0A3%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%85%B7%E4%BD%93%E5%AE%89%E5%85%A8%E8%A6%81%E6%B1%82%EF%BC%88%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E4%B8%AD%E7%9A%84%E6%8E%A7%E5%88%B6%E6%8E%AA%E6%96%BD%EF%BC%89%0D%0A4%E3%80%81%E5%B7%B2%E5%AF%B9%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%8E%B0%E5%9C%BA%E5%AE%89%E5%85%A8%E6%8E%AA%E6%96%BD%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%A3%80%E6%9F%A5%E7%A1%AE%E8%AE%A4%0D%0A5%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%B6%89%E5%8F%8A%E7%9A%84%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E7%9A%84%E6%9C%89%E9%99%90%E6%9C%9F%E9%99%90%20%0D%0A6%E3%80%81%E5%B7%B2%E6%8E%8C%E6%8F%A1%E4%B8%AA%E4%BA%BA%E9%98%B2%E6%8A%A4%E7%94%A8%E5%85%B7%E6%AD%A3%E7%A1%AE%E4%BD%A9%E6%88%B4%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%0D%0A7%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E7%AA%81%E5%8F%91%E6%83%85%E5%86%B5%E4%B8%8B%E7%9A%84%E5%BA%94%E6%80%A5%E9%81%BF%E9%99%A9%E6%96%B9%E6%B3%95&additional_content=&workTicketid=2000000002028&worktaskid=2000000002028&workType=aqjd&actionCode=clarsign'
#http://192.168.6.27:6030/m/hse_m/HSE_SAFETY_DISCLOSURE_M/jsasignAudit.json?safe_name=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&safe_content=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&confirm_content=1%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E4%BD%9C%E4%B8%9A%E5%8C%BA%E5%9F%9F%E5%8F%8A%E5%91%A8%E8%BE%B9%E7%94%9F%E4%BA%A7%E4%BD%9C%E4%B8%9A%E6%83%85%E5%86%B5%0D%0A2%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%EF%BC%88JSA%EF%BC%89%0D%0A3%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%85%B7%E4%BD%93%E5%AE%89%E5%85%A8%E8%A6%81%E6%B1%82%EF%BC%88%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E4%B8%AD%E7%9A%84%E6%8E%A7%E5%88%B6%E6%8E%AA%E6%96%BD%EF%BC%89%0D%0A4%E3%80%81%E5%B7%B2%E5%AF%B9%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%8E%B0%E5%9C%BA%E5%AE%89%E5%85%A8%E6%8E%AA%E6%96%BD%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%A3%80%E6%9F%A5%E7%A1%AE%E8%AE%A4%0D%0A5%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%B6%89%E5%8F%8A%E7%9A%84%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E7%9A%84%E6%9C%89%E9%99%90%E6%9C%9F%E9%99%90%20%0D%0A6%E3%80%81%E5%B7%B2%E6%8E%8C%E6%8F%A1%E4%B8%AA%E4%BA%BA%E9%98%B2%E6%8A%A4%E7%94%A8%E5%85%B7%E6%AD%A3%E7%A1%AE%E4%BD%A9%E6%88%B4%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%0D%0A7%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E7%AA%81%E5%8F%91%E6%83%85%E5%86%B5%E4%B8%8B%E7%9A%84%E5%BA%94%E6%80%A5%E9%81%BF%E9%99%A9%E6%96%B9%E6%B3%95&additional_content=&workTicketid=2000000002028&worktaskid=2000000002028&workType=aqjd&actionCode=clarsign
url = 'http://192.168.6.27:6030/m/hse_m/HSE_SAFETY_DISCLOSURE_M/jsasignAudit.json?safe_name=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&safe_content=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&confirm_content=1%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E4%BD%9C%E4%B8%9A%E5%8C%BA%E5%9F%9F%E5%8F%8A%E5%91%A8%E8%BE%B9%E7%94%9F%E4%BA%A7%E4%BD%9C%E4%B8%9A%E6%83%85%E5%86%B5%0D%0A2%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%EF%BC%88JSA%EF%BC%89%0D%0A3%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%85%B7%E4%BD%93%E5%AE%89%E5%85%A8%E8%A6%81%E6%B1%82%EF%BC%88%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E4%B8%AD%E7%9A%84%E6%8E%A7%E5%88%B6%E6%8E%AA%E6%96%BD%EF%BC%89%0D%0A4%E3%80%81%E5%B7%B2%E5%AF%B9%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%8E%B0%E5%9C%BA%E5%AE%89%E5%85%A8%E6%8E%AA%E6%96%BD%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%A3%80%E6%9F%A5%E7%A1%AE%E8%AE%A4%0D%0A5%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%B6%89%E5%8F%8A%E7%9A%84%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E7%9A%84%E6%9C%89%E9%99%90%E6%9C%9F%E9%99%90%20%0D%0A6%E3%80%81%E5%B7%B2%E6%8E%8C%E6%8F%A1%E4%B8%AA%E4%BA%BA%E9%98%B2%E6%8A%A4%E7%94%A8%E5%85%B7%E6%AD%A3%E7%A1%AE%E4%BD%A9%E6%88%B4%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%0D%0A7%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E7%AA%81%E5%8F%91%E6%83%85%E5%86%B5%E4%B8%8B%E7%9A%84%E5%BA%94%E6%80%A5%E9%81%BF%E9%99%A9%E6%96%B9%E6%B3%95&additional_content=&workTicketid='+str(jsaidxx)+'&worktaskid='+str(jsaidxx)+'&workType=aqjd&actionCode=clarsign'
data = {"mainAttributeVO":{"additional_content":""},"auditPlainLineList":[{"actiontype":"sign","isexmaineable":1,"groupType":"4","code":"2000000005785","latitude":39.982727,"idnumber":"","dataStatus":0,"ismustaudit":1,"force_photo":0,"isEnd":1,"ismulti":0,"isShow":1,"auditorder":3,"isinputidnumber":0,"electronicSignature":[{"imgStr":"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\n","uuid":""}],"name":"作业教育人（项目负责人）","audittype":"sign,face,card","specialworktype":"","value":"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\n","isbrushposition":0,"disporder":3,"longitude":116.338467}]}
#rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#print(data)
# 获取接口返回状态
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#作业任务添加m预制任务
casename = '作业任务添加m预制任务'
caseinfo['id'] = 112
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKAPPLY_MCQ_M/cardAdd.json'
rs = requests.get(url=url, headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
# json化
data = json.loads(data)
# 获取接口返回状态
#print("data", data)
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())
insert = data['data']['data']['insert__']

print("作业任务添加m预制任务",sta)

#作业任务添加m
casename = '作业任务添加m'
caseinfo['id'] = 113
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKAPPLY_MCQ_M/cardSave.json'
data = {
	"vo": {
		"df": 0,
		"workname": name,
		"woid": "",
		"territorialdeviceid": 2000000003454,
		"workunitname": "长庆石化分公司",
		"work_position_name": "制氢北区",
		"jsa_code": name,
		"worktickettype_query": "",
		"created_by_name": "",
		"tableName": "hse_work_task",
		"iscontractor": 0,
		"updated_by_name": "",
		"insert__": insert,
		"equipmentcode": "",
		"territorialunitid": "2000000003339",
		"jsaid": jsaidxx,
		"territorialdevicename": "制氢装置",
		"tenantid": 1,
		"projecttype": "rcjx",
		"territorialunitname": "运行一部",
		"workstatus": "draft",
		"equipmentnumber": "",
		"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
		"ver": 1,
		"created_dt": now,
		"planendtime": endtime,
		"reminder": "",
		"work_appoint_name": name,
		"reminderid": "",
		"worktickettype_name": "作业许可证",
		"applyunitname": "运行一部",
		"equipmentname": "",
		"dataStatus": 0,
		"work_appoint_id": 2000000001775,
		"wo_code": "",
		"standardmaintenance": "",
		"created_by": "",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"workunit": 1688712,
		"updated_dt": now,
		"contractorname": "",
		"updated_by": "",
		"planstarttime": starttime,
		"territorialunitcode": "CS8082020",
		"applyunitid": "2000000003339",
		"workcontent": "作业内容123",
		"worktaskid": ""
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())
#作业任务提交
casename = '作业任务提交'
caseinfo['id'] = 114
caseinfo['name'] = casename
worktaskidxx = getdata.get_work_task_id(cookies,name)

print("worktaskidxx",worktaskidxx)
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKAPPLY_MCQ_M/submit.json?dataId=%d&ts='%(worktaskidxx)
data = {
	"vo": {
		"df": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": 0,
		"jsa_code": name,
		"created_by_name": "测试用户",
		"beendelaynum": 0,
		"tableName": "hse_work_task",
		"territorialunitid": 2000000003339,
		"territorialdevicename": "制氢装置",
		"territorialunitname": "运行一部",
		"equipmentnumber": "",
		"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
		"ver": 1,
		"planendtime": endtime,
		"work_appoint_name": "Created_by_Python_CEI3Vy",
		"constructionscheme": 0,
		"applyunitname": "运行一部",
		"equipmentname": "",
		"iswfnotreport": 0,
		"dataStatus": 0,
		"wo_code": "",
		"standardmaintenance": "",
		"created_by": 1000,
		"pause": 0,
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"workcontent": "作业内容123",
		"wf_audit_state": "0",
		"constructionscheme_attachshowlist": [],
		"plan_type": 3,
		"woid": "",
		"territorialdeviceid": 2000000003454,
		"work_position_name": "制氢北区",
		"worktickettype_query": "",
		"iscontractor": 0,
		"updated_by_name": "测试用户",
		"equipmentcode": "",
		"jsaid": 2000000001875,
		"tenantid": 1,
		"projecttype": "rcjx",
		"workstatus": "draft",
		"created_dt": now,
		"reminder": "",
		"reminderid": "",
		"worktickettype_name": "",
		"work_appoint_id": work_appoint_idx,
		"work_position_id": 2000000002019,
		"wf_create_user": 1000,
		"site": "作业地点123",
		"updated_dt": now,
		"contractorname": "",
		"territorialunitcode": "CS8082020",
		"applyunitid": 2000000003339,
		"worktaskid": worktaskidxx
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#print(name)

#作业许可证保存
casename = '作业许可证保存'
caseinfo['id'] = 115
caseinfo['name'] = casename

workticketidx = workticketid + 7
ts = tsi + 7

url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/cardSave.json?level=1'

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
				"worktaskharmid": 2000000033156,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033157,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033158,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033159,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033160,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033161,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033162,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033163,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033164,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033165,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033166,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033167,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033168,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033169,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033170,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033171,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033172,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033173,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033174,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033175,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033176,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033177,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033178,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033179,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskharmid": 2000000033180,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktaskequipmentid": 2000000016450,
				"equipmentcode": "aqyj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016451,
				"equipmentcode": "qfbyz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016452,
				"equipmentcode": "hjhmj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016453,
				"equipmentcode": "aqm",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016454,
				"equipmentcode": "fjdfz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016455,
				"equipmentcode": "he",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016456,
				"equipmentcode": "aqx",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016457,
				"equipmentcode": "fdmz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016458,
				"equipmentcode": "zyshxq",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016459,
				"equipmentcode": "fhf",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016460,
				"equipmentcode": "st",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016461,
				"equipmentcode": "jyfz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016462,
				"equipmentcode": "fhmj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016463,
				"equipmentcode": "aqd",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016464,
				"equipmentcode": "aqs",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016465,
				"equipmentcode": "tsss",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016466,
				"equipmentcode": "rypx",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskequipmentid": 2000000016467,
				"equipmentcode": "qtfh",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079606,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079607,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079608,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079609,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079610,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079611,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079612,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079613,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079614,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079615,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079616,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079617,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079618,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079619,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079620,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079621,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079622,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079623,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079624,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079625,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079626,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktaskmeasureid": 2000000079627,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"hse_work_task_harm_mcq_m": 25,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"otherunit": "",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"othercontent": "",
		"hse_work_task_equipment_m": 18,
		"worktype_name": "作业许可证",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "1",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"worker": "不知道",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 22,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
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
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"gas_aging": "4",
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": worktaskidxx,
		"ts": 1592531114768
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#作业许可证
casename = '作业许可证提交'
caseinfo['id'] = 116
caseinfo['name'] = casename

workticketidx = workticketid + 7
ts = tsi + 7

#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/submit.json?dataId=workticketidx&ts=ts
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/submit.json?dataId=%d&ts=ts'%(workticketidx)
data = {
	"vo": {
		"hse_work_task_harm_mcq_m": 25,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"otherunit": "",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"othercontent": "",
		"hse_work_task_equipment_m": 18,
		"worktype_name": "作业许可证",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "1",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"worker": "不知道",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 22,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
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
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"gas_aging": "4",
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": worktaskidxx,
		"ts": ts
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#动火作业
casename = '动火作业保存'
caseinfo['id'] = 117
caseinfo['name'] = casename

workticketidx = workticketid + 4
ts = tsi + 4

url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DH_MCQ_M/cardSave.json?level=1'
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
				"worktype": "dh",
				"harmid": 2000000008667,
				"harmcode": "dhzy001",
				"harmname": "爆炸",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033141,
				"workway": "mcq_dhfs01",
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008668,
				"harmcode": "dhzy002",
				"harmname": "火灾",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033142,
				"workway": "mcq_dhfs01",
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008669,
				"harmcode": "dhzy003",
				"harmname": "灼伤",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033143,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008670,
				"harmcode": "dhzy004",
				"harmname": "烫伤",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033144,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008671,
				"harmcode": "dhzy005",
				"harmname": "机械伤害",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033145,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008672,
				"harmcode": "dhzy006",
				"harmname": "中毒",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033146,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008673,
				"harmcode": "dhzy007",
				"harmname": "辐射",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033147,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008674,
				"harmcode": "dhzy008",
				"harmname": "触电",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033148,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008675,
				"harmcode": "dhzy009",
				"harmname": "泄漏",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033149,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008676,
				"harmcode": "dhzy010",
				"harmname": "窒息",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033150,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008677,
				"harmcode": "dhzy011",
				"harmname": "坠落",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033151,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008678,
				"harmcode": "dhzy012",
				"harmname": "落物",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033152,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008679,
				"harmcode": "dhzy013",
				"harmname": "掩埋",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033153,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008680,
				"harmcode": "dhzy014",
				"harmname": "噪声",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033154,
				"workway": "mcq_dhfs03,mcq_dhfs06",
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008681,
				"harmcode": "dhzy015",
				"harmname": "其他：（）",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033155,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "1.动火处与管线连接处用盲板隔断（）处",
				"riskrepositoryid": 2000000005013,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079485,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "2.管道容器内可燃介质用蒸汽、氮气或水处理干净",
				"riskrepositoryid": 2000000005014,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079486,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "3.清除动火点周围的可燃介质和可燃物",
				"riskrepositoryid": 2000000005015,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079487,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "4.作业时50米内不准有放空或脱水操作",
				"riskrepositoryid": 2000000005016,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079488,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "5.动火现场配备消防蒸汽带（）根",
				"riskrepositoryid": 2000000005017,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079489,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "6.必须分析检验合格",
				"riskrepositoryid": 2000000005018,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079490,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "7.动火点半径15米内污水井、地漏封死盖严",
				"riskrepositoryid": 2000000005019,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079491,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "8.动火现场配备8公斤干粉灭火器（）台，配备轮载干粉灭火机（）台",
				"riskrepositoryid": 2000000005020,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079492,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "9.附近的固定消防设施齐全完好",
				"riskrepositoryid": 2000000005021,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079493,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "10.动火时需要消防车监护",
				"riskrepositoryid": 2000000005022,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079494,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "11.补充安全措施：（）",
				"riskrepositoryid": 2000000005023,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079495,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "1.在动火点处设置隔离设施",
				"riskrepositoryid": 2000000005024,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079496,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "2.清除动火点上方坠落物或转移动火地点",
				"riskrepositoryid": 2000000005025,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079497,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "3.动火点搭设临时作业平台",
				"riskrepositoryid": 2000000005026,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079498,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "4.人员作业穿戴合适防护用品",
				"riskrepositoryid": 2000000005027,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079499,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "5.施工机具符合要求",
				"riskrepositoryid": 2000000005028,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079500,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "6.人员培训合格",
				"riskrepositoryid": 2000000005029,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079501,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "7.特种作业人员持有效作业证",
				"riskrepositoryid": 2000000005030,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079502,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "8.动火现场发生意外泄漏，立即停止动火，消除火源",
				"riskrepositoryid": 2000000005031,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079503,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "9.补充安全措施：（）",
				"riskrepositoryid": 2000000005032,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079504,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "rd06",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "动火作业",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "",
		"hassafetyplan": "",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"tasktype": "dh10",
		"worklevel": "mcq_dh_workLevel01",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 20,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"medium": "大雁",
		"updated_by_name": "卢健",
		"workway": "mcq_dhfs14",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "dh",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isupgradedh": "",
		"isdzdh": "",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"gas_aging": "4",
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": worktaskidxx,
		"ts": 1592531768729
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#动火作业
casename = '动火作业提交'
caseinfo['id'] = 118
caseinfo['name'] = casename

workticketidx = workticketid + 4
ts = tsi + 4
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DH_MCQ_M/submit.json?dataId=2000000007399&ts=1592532272767
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DH_MCQ_M/submit.json?dataId=%d&ts=1592532272767'%(workticketidx)
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
				"worktype": "dh",
				"harmid": 2000000008667,
				"harmcode": "dhzy001",
				"harmname": "爆炸",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033141,
				"workway": "mcq_dhfs01",
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008668,
				"harmcode": "dhzy002",
				"harmname": "火灾",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033142,
				"workway": "mcq_dhfs01",
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008669,
				"harmcode": "dhzy003",
				"harmname": "灼伤",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033143,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008670,
				"harmcode": "dhzy004",
				"harmname": "烫伤",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033144,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008671,
				"harmcode": "dhzy005",
				"harmname": "机械伤害",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033145,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008672,
				"harmcode": "dhzy006",
				"harmname": "中毒",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033146,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008673,
				"harmcode": "dhzy007",
				"harmname": "辐射",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033147,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008674,
				"harmcode": "dhzy008",
				"harmname": "触电",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033148,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008675,
				"harmcode": "dhzy009",
				"harmname": "泄漏",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033149,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008676,
				"harmcode": "dhzy010",
				"harmname": "窒息",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033150,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008677,
				"harmcode": "dhzy011",
				"harmname": "坠落",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033151,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008678,
				"harmcode": "dhzy012",
				"harmname": "落物",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033152,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008679,
				"harmcode": "dhzy013",
				"harmname": "掩埋",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033153,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008680,
				"harmcode": "dhzy014",
				"harmname": "噪声",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033154,
				"workway": "mcq_dhfs03,mcq_dhfs06",
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dh",
				"harmid": 2000000008681,
				"harmcode": "dhzy015",
				"harmname": "其他：（）",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033155,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "1.动火处与管线连接处用盲板隔断（）处",
				"riskrepositoryid": 2000000005013,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079485,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "2.管道容器内可燃介质用蒸汽、氮气或水处理干净",
				"riskrepositoryid": 2000000005014,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079486,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "3.清除动火点周围的可燃介质和可燃物",
				"riskrepositoryid": 2000000005015,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079487,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "4.作业时50米内不准有放空或脱水操作",
				"riskrepositoryid": 2000000005016,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079488,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "5.动火现场配备消防蒸汽带（）根",
				"riskrepositoryid": 2000000005017,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079489,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "6.必须分析检验合格",
				"riskrepositoryid": 2000000005018,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079490,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "7.动火点半径15米内污水井、地漏封死盖严",
				"riskrepositoryid": 2000000005019,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079491,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "8.动火现场配备8公斤干粉灭火器（）台，配备轮载干粉灭火机（）台",
				"riskrepositoryid": 2000000005020,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079492,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "9.附近的固定消防设施齐全完好",
				"riskrepositoryid": 2000000005021,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079493,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "10.动火时需要消防车监护",
				"riskrepositoryid": 2000000005022,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079494,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "11.补充安全措施：（）",
				"riskrepositoryid": 2000000005023,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079495,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "1.在动火点处设置隔离设施",
				"riskrepositoryid": 2000000005024,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079496,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "2.清除动火点上方坠落物或转移动火地点",
				"riskrepositoryid": 2000000005025,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079497,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "3.动火点搭设临时作业平台",
				"riskrepositoryid": 2000000005026,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079498,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "4.人员作业穿戴合适防护用品",
				"riskrepositoryid": 2000000005027,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079499,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "5.施工机具符合要求",
				"riskrepositoryid": 2000000005028,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079500,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "6.人员培训合格",
				"riskrepositoryid": 2000000005029,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079501,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "7.特种作业人员持有效作业证",
				"riskrepositoryid": 2000000005030,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079502,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "8.动火现场发生意外泄漏，立即停止动火，消除火源",
				"riskrepositoryid": 2000000005031,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079503,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "9.补充安全措施：（）",
				"riskrepositoryid": 2000000005032,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dhzy20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dh",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "zyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079504,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "rd06",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "动火作业",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "",
		"hassafetyplan": "",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"tasktype": "dh10",
		"worklevel": "mcq_dh_workLevel01",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 20,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"medium": "大雁",
		"updated_by_name": "卢健",
		"workway": "mcq_dhfs14",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "dh",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isupgradedh": "",
		"isdzdh": "",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"gas_aging": "4",
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": worktaskidxx,
		"ts": 1592531768729
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#受限作业
casename = '受限作业保存'
caseinfo['id'] = 119
caseinfo['name'] = casename

workticketidx = workticketid + 5
ts = tsi + 5

url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_SX_MCQ_M/cardSave.json?level=1'
data = {
	"children": {
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "管道容器可燃气体窜入",
				"riskrepositoryid": 2000000005108,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079506,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "塔 容器内有可燃介质",
				"riskrepositoryid": 2000000005109,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079507,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "通风不良",
				"riskrepositoryid": 2000000005110,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079508,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "受限空间内残存可燃气体和有毒有害气体",
				"riskrepositoryid": 2000000005111,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079509,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "人员出入口处有障碍物",
				"riskrepositoryid": 2000000005112,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079510,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "人员应急救援设备不全",
				"riskrepositoryid": 2000000005113,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079511,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "监护人不在现场",
				"riskrepositoryid": 2000000005114,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079512,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "受限空间作业点周围警示不明显",
				"riskrepositoryid": 2000000005115,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079513,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "现场急救器材不够",
				"riskrepositoryid": 2000000005116,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079514,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业人员着装不规范",
				"riskrepositoryid": 2000000005117,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079515,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业工具使用时易产生火花",
				"riskrepositoryid": 2000000005118,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079516,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业人员未按要求佩戴防护器具",
				"riskrepositoryid": 2000000005119,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079517,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业人员对防护器具使用不熟练",
				"riskrepositoryid": 2000000005120,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079518,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业过程中有时有可燃气体逸出",
				"riskrepositoryid": 2000000005121,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079519,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业时间过长",
				"riskrepositoryid": 2000000005122,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079520,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "人员作业时触电",
				"riskrepositoryid": 2000000005123,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079521,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "工具、材料进入前后数量不清",
				"riskrepositoryid": 2000000005124,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079522,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "补充措施：（）",
				"riskrepositoryid": 2000000005125,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079523,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "将受限空间与管线连接处用（）块盲板隔离",
				"riskrepositoryid": 2000000005126,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079524,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "用蒸汽、氮气或水彻底处理干净",
				"riskrepositoryid": 2000000005127,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079525,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "打开所有通风孔和人孔，进行自然通风2小时以上",
				"riskrepositoryid": 2000000005128,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj21",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079526,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "采取机械强制通风",
				"riskrepositoryid": 2000000005129,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj22",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079527,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "对受限空间内的气体进行采样分析，成绩合格",
				"riskrepositoryid": 2000000005130,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj23",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079528,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "每（）小时采样一次",
				"riskrepositoryid": 2000000005131,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj24",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079529,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "清理人员出入口处的障碍物，并悬挂标识",
				"riskrepositoryid": 2000000005132,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj25",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079530,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "监护人备好应急救援设备并且能够熟练使用",
				"riskrepositoryid": 2000000005133,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj26",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079531,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "外部设专人监护，内外人员规定联络信号和方法",
				"riskrepositoryid": 2000000005134,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj27",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079532,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业点周围警戒线拉好，出入口处设警示牌",
				"riskrepositoryid": 2000000005135,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj28",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079533,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "现场配备灭火器（ ）台",
				"riskrepositoryid": 2000000005136,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj29",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079534,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "现场已配备急救器材",
				"riskrepositoryid": 2000000005137,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj30",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079535,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "现场配备气防抢险车和人员",
				"riskrepositoryid": 2000000005138,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj31",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "sgzyfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079536,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "穿着防静电工作服和鞋",
				"riskrepositoryid": 2000000005139,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj32",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079537,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "使用不产生火花（如有色金属制作）的工具",
				"riskrepositoryid": 2000000005140,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj33",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079538,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "按规定佩戴防护器具",
				"riskrepositoryid": 2000000005141,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj34",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079539,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业前队作业人员进行器具使用的培训和演练",
				"riskrepositoryid": 2000000005142,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj35",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079540,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业人员佩戴可燃气体报警器。乙炔带不能有接口",
				"riskrepositoryid": 2000000005143,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj36",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079541,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "受限空间内不得超过( )人,每人作业时间不得超过( )分钟",
				"riskrepositoryid": 2000000005144,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj37",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079542,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "符合临时用电规定，电源应装漏电保护器，照明电压≤24伏，特别潮湿或金属受限空间内照明电压≤12伏",
				"riskrepositoryid": 2000000005145,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj38",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079543,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "对人员、材料、工具进行登记和清点",
				"riskrepositoryid": 2000000005146,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "sxkj39",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "sx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gysbhjfxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079544,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"hasemergencyplan": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "受限空间",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "1",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "mcq_sx_workLevel01",
		"tasktype": "comone08",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 39,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"hasrescueplan": "1",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"haschecklist": "",
		"updated_by_name": "卢健",
		"workway": "mcq_sxfs16",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "sx",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"gas_aging": "4",
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592531768733
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#受限作业
casename = '受限作业提交'
caseinfo['id'] = 120
caseinfo['name'] = casename

workticketidx = workticketid + 5
ts = tsi + 5
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DH_MCQ_M/submit.json?dataId=2000000007399&ts=1592532272767
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_SX_MCQ_M/submit.json?dataId=%d&ts=1592532384543'%(workticketidx)
data = {
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"hasemergencyplan": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "受限空间",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "1",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "mcq_sx_workLevel01",
		"tasktype": "comone08",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 39,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"hasrescueplan": "1",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"haschecklist": "",
		"updated_by_name": "卢健",
		"workway": "mcq_sxfs16",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "sx",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"gas_aging": "4",
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": ts
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#高处作业
casename = '高处作业保存'
caseinfo['id'] = 121
caseinfo['name'] = casename

workticketidx = workticketid + 9
ts = tsi + 9

url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GC_MCQ_M/cardSave.json?level=1'
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
				"worktype": "gc",
				"harmid": 2000000008687,
				"harmcode": "gczy001",
				"harmname": "人员坠落",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033186,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008688,
				"harmcode": "gczy002",
				"harmname": "物体打击",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033187,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008689,
				"harmcode": "gczy003",
				"harmname": "机械伤害",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033188,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008690,
				"harmcode": "gczy004",
				"harmname": "湿滑跌倒",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033189,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008691,
				"harmcode": "gczy005",
				"harmname": "脚手架坍塌",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033190,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008692,
				"harmcode": "gczy006",
				"harmname": "中毒窒息",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033191,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008693,
				"harmcode": "gczy007",
				"harmname": "辐射",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033192,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008694,
				"harmcode": "gczy008",
				"harmname": "泄漏",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033193,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008695,
				"harmcode": "gczy009",
				"harmname": "灼烫伤",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033194,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008696,
				"harmcode": "gczy010",
				"harmname": "临边、孔洞",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033195,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008697,
				"harmcode": "gczy011",
				"harmname": "防护不当",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033196,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008698,
				"harmcode": "gczy012",
				"harmname": "个人防护装备缺陷",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033197,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gc",
				"harmid": 2000000008699,
				"harmcode": "gczy013",
				"harmname": "其他：（）",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033198,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "身体条件符合要求",
				"riskrepositoryid": 2000000005047,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079633,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "着装符合工作要求",
				"riskrepositoryid": 2000000005048,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079634,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "佩戴安全带",
				"riskrepositoryid": 2000000005049,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079635,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "30米以上作业配备通讯工具",
				"riskrepositoryid": 2000000005050,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079636,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "有坠落防护设施",
				"riskrepositoryid": 2000000005051,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079637,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "携带工具袋",
				"riskrepositoryid": 2000000005052,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079638,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业点照明充足",
				"riskrepositoryid": 2000000005053,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079639,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "设置围栏、警戒线、夜间警示灯",
				"riskrepositoryid": 2000000005054,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079640,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业前培训其他措施",
				"riskrepositoryid": 2000000005055,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079641,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "垂直分层作业中间有隔离",
				"riskrepositoryid": 2000000005056,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079642,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "梯子符合安全要求",
				"riskrepositoryid": 2000000005057,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079643,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "在非承重物上作业时搭设承重板",
				"riskrepositoryid": 2000000005058,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079644,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "员工清楚坠落风险",
				"riskrepositoryid": 2000000005059,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079645,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其它：（）",
				"riskrepositoryid": 2000000005060,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gczy14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gc",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "fxxjcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079646,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"hse_work_task_harm_mcq_m": 13,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "高处作业",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "1",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "mcq_gc_workLevel01",
		"tasktype": "comtwo06",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 14,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"hasrescueplan": "1",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "gc",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592531114768
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#高处作业
casename = '高处作业提交'
caseinfo['id'] = 122
caseinfo['name'] = casename

workticketidx = workticketid + 9
ts = tsi + 9
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GC_MCQ_M/submit.json?dataId=2000000007404&ts=1592532540145
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GC_MCQ_M/submit.json?dataId=%d&ts=1592532540145'%(workticketidx)
data = {
	"vo": {
		"hse_work_task_harm_mcq_m": 13,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "高处作业",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "1",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "mcq_gc_workLevel01",
		"tasktype": "comtwo06",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 14,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"hasrescueplan": "1",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "gc",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": ts
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#吊装作业
casename = '吊装作业保存'
caseinfo['id'] = 123
caseinfo['name'] = casename

workticketidx = workticketid + 6
ts = tsi + 6

url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DZ_MCQ_M/cardSave.json?level=1'
data = {
	"children": {
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "1.吊装准备",
				"riskrepositoryid": 2000000004968,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079556,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "核实物件重量",
				"riskrepositoryid": 2000000004969,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079557,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "考虑吊装附件引起重量增加",
				"riskrepositoryid": 2000000004970,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079558,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "吊装角度适合（考虑最差角度）",
				"riskrepositoryid": 2000000004971,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079559,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "符合起重机额定载荷",
				"riskrepositoryid": 2000000004972,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079560,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "检查作业人员经过培训",
				"riskrepositoryid": 2000000004973,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079561,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "对起重机进行了检查和维护",
				"riskrepositoryid": 2000000004974,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079562,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "吊索具及附件满足能力需要",
				"riskrepositoryid": 2000000004975,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079563,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已检查吊索具及其附件无缺陷",
				"riskrepositoryid": 2000000004976,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079564,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已清楚物件的规格尺寸及重心",
				"riskrepositoryid": 2000000004977,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079565,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已明确物件的捆绑和固定方式",
				"riskrepositoryid": 2000000004978,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079566,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已制定吊挂货物的方法",
				"riskrepositoryid": 2000000004979,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079567,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "货物支撑物是否合适",
				"riskrepositoryid": 2000000004980,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079568,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "明确货物件吊运路线",
				"riskrepositoryid": 2000000004981,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079569,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "明确如何运输物件",
				"riskrepositoryid": 2000000004982,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079570,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "明确物件放置地点",
				"riskrepositoryid": 2000000004983,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079571,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "考虑物件吊装的平衡方法",
				"riskrepositoryid": 2000000004984,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079572,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "是否需要溜绳（或拉钩）",
				"riskrepositoryid": 2000000004985,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079573,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "是否需要物件缓冲防震保护",
				"riskrepositoryid": 2000000004986,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079574,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "是否考虑强风下物件稳定措施",
				"riskrepositoryid": 2000000004987,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079575,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "是否是带有突出物的物件",
				"riskrepositoryid": 2000000004988,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy21",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079576,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "支腿支撑加固措施落实",
				"riskrepositoryid": 2000000004989,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy22",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079577,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "天气情况是否适合吊装",
				"riskrepositoryid": 2000000004990,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy23",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079578,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "确认已落实应急措施",
				"riskrepositoryid": 2000000004991,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy24",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079579,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "2.吊装区域",
				"riskrepositoryid": 2000000004992,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy25",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079580,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "是否需要梯子或脚手架",
				"riskrepositoryid": 2000000004993,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy26",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079581,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "是否已考虑辅助工具和设备",
				"riskrepositoryid": 2000000004994,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy27",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079582,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "吊装、移动过程中是否有障碍",
				"riskrepositoryid": 2000000004995,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy28",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079583,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*是否设置路障或警示标志",
				"riskrepositoryid": 2000000004996,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy29",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079584,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*警示区域是否涵盖作业半径",
				"riskrepositoryid": 2000000004997,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy30",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079585,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*地下设施已确认",
				"riskrepositoryid": 2000000004998,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy31",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079586,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*防火帽是否安装合格",
				"riskrepositoryid": 2000000004999,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy32",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079587,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "3.起重机及人员",
				"riskrepositoryid": 2000000005000,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy33",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079588,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已确定作业组中每一个人的任务",
				"riskrepositoryid": 2000000005001,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy34",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079589,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "司机的身体和心理状况良好",
				"riskrepositoryid": 2000000005002,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy35",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079590,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "操作室中能否清楚看到指挥信号",
				"riskrepositoryid": 2000000005003,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy36",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079591,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "司机是否有克服吊装盲点的措施",
				"riskrepositoryid": 2000000005004,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy37",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079592,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已明确指挥信号",
				"riskrepositoryid": 2000000005005,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy38",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079593,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*已确定吊装负责人",
				"riskrepositoryid": 2000000005006,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy39",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079594,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*已明确唯一的吊装指挥",
				"riskrepositoryid": 2000000005007,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy40",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079595,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*起重司机、指挥、司索是否持证上岗",
				"riskrepositoryid": 2000000005008,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy41",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079596,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*是否需要无线电通讯工具",
				"riskrepositoryid": 2000000005009,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy42",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079597,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*已进行吊装计划交底培训",
				"riskrepositoryid": 2000000005010,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy43",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079598,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "*支腿处的地面平整、坚实",
				"riskrepositoryid": 2000000005011,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy44",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079599,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "4.其他（）",
				"riskrepositoryid": 2000000005012,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dzzy45",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dz",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "qdqjc",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079600,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"loadhigh": "10",
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"loadradius": "8",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"objectmass": "",
		"worktype_name": "吊装作业",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "mcq_dz_workLevel01",
		"tasktype": "comone08",
		"lock_status": 0,
		"planendtime": endtime,
		"hashookcheck": "",
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 45,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"hasrescueplan": "",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"loadrate": "20",
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"loadmass": "8",
		"tenantid": 1,
		"objectnorm": "3*3*3",
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"hasdrivermedical": "",
		"hasfacadecheck": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "dz",
		"loadgoodsname": "大雁",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"ticketdealphoto": 0,
		"applyunitid": 2000000003339,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"loaddegree": "",
		"ts": 1592531114768
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#吊装作业
casename = '吊装作业提交'
caseinfo['id'] = 124
caseinfo['name'] = casename

workticketidx = workticketid + 6
ts = tsi + 6
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GC_MCQ_M/submit.json?dataId=2000000007404&ts=1592532540145
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DZ_MCQ_M/submit.json?dataId=%d&ts=1592532696292'%(workticketidx)
data = {
	"vo": {
		"loadhigh": "10",
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"drawshow": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"loadradius": "8",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"objectmass": "",
		"worktype_name": "吊装作业",
		"territorialunitid": 2000000003339,
		"hasdrawpaper": "",
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "mcq_dz_workLevel01",
		"tasktype": "comone08",
		"lock_status": 0,
		"planendtime": endtime,
		"hashookcheck": "",
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 45,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"hasrescueplan": "",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"loadrate": "20",
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"loadmass": "8",
		"tenantid": 1,
		"objectnorm": "3*3*3",
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"hasdrivermedical": "",
		"hasfacadecheck": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "dz",
		"loadgoodsname": "大雁",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"ticketdealphoto": 0,
		"applyunitid": 2000000003339,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"loaddegree": "",
		"ts": 1592532696292
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#临时用电
casename = '临时用电保存'
caseinfo['id'] = 125
caseinfo['name'] = casename

workticketidx = workticketid + 1
ts = tsi + 1

url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_LSYD_MCQ_M/cardSave.json?level=1'
data = {
	"children": {
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "1.安装临时线路人员持有电工作业操作证",
				"riskrepositoryid": 2000000005090,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079406,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "2.在防爆场所使用的临时电源、元器件和线路达到相应的防爆等级要求",
				"riskrepositoryid": 2000000005091,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079407,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "3.临时用电设施装有漏电保护器,移动工具、手持工具“一机一闸一保护”",
				"riskrepositoryid": 2000000005092,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079408,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "4.临时用电的单项和混用线路采用五线制",
				"riskrepositoryid": 2000000005093,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079409,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "5.临时用电架空线路在装置内不低于2.5m,道路不低于5m",
				"riskrepositoryid": 2000000005094,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079410,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "6.临时用电线路架空进线未采用裸线,未在树或脚手架上架设",
				"riskrepositoryid": 2000000005095,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079411,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "7.暗管埋设及地下电缆线路设有“走向标志”和“安全标志”,电缆埋深大于0.7m",
				"riskrepositoryid": 2000000005096,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079412,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "8.现场临时用配电盘、箱有防雨措施",
				"riskrepositoryid": 2000000005097,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079413,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "9.临时用电设置接地保护，接地电阻值满足规范要求，接地线和接零线分开设置",
				"riskrepositoryid": 2000000005098,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079414,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "10.用电设备、线路容量、负荷符合要求",
				"riskrepositoryid": 2000000005099,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079415,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "11.现场临时配电箱、盘上标有电压标识和危险标识，并设有安全锁具",
				"riskrepositoryid": 2000000005100,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079416,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "12.临时下路穿越道路时设有防护套管，防护套管内径不应小于电缆外径的1.5倍。",
				"riskrepositoryid": 2000000005101,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079417,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "13.水下或潮湿环境中使用电气设备或电动工具，带电零件与壳体之间，基本绝缘不得小于2M伲忧烤挡坏眯∮?7M?",
				"riskrepositoryid": 2000000005102,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079418,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "14.手持电动工具外观完好，标牌清晰，各种保护罩（板）齐全",
				"riskrepositoryid": 2000000005103,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079419,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "15.临时施工、作业场所使用安全插座、插头",
				"riskrepositoryid": 2000000005104,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079420,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "16.临时用电线路及设备有良好的绝缘，所有的临时用电线路必须采用额定电压等级不低于500V的绝缘导线",
				"riskrepositoryid": 2000000005105,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079421,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "17.临时用电线路经过有高温、振动、腐蚀、积水、防爆区域及机械损伤等区域时，没有接头",
				"riskrepositoryid": 2000000005106,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079422,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "18.其他安全措施：（）",
				"riskrepositoryid": 2000000005107,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "lsyd18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "lsyd",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079423,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "临时用电",
		"territorialunitid": 2000000003339,
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "202006lsyd157",
		"workunit": 1688712,
		"updated_by": 1000,
		"poweraccesspoint": "北京",
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 18,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"workvoltage": "220",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "lsyd",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"ticketdealphoto": 0,
		"applyunitid": 2000000003339,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592531114767
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#临时用电
casename = '临时用电提交'
caseinfo['id'] = 126
caseinfo['name'] = casename

workticketidx = workticketid + 1
ts = tsi + 1
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GC_MCQ_M/submit.json?dataId=2000000007404&ts=1592532540145
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_LSYD_MCQ_M/submit.json?dataId=%d&ts=1592532903456'%(workticketidx)
data = {
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"worktype_name": "临时用电",
		"territorialunitid": 2000000003339,
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "202006lsyd157",
		"workunit": 1688712,
		"updated_by": 1000,
		"poweraccesspoint": "北京",
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 18,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"workvoltage": "220",
		"isupgrade": 0,
		"invalidreason": "",
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "lsyd",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"ticketdealphoto": 0,
		"applyunitid": 2000000003339,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592532903456
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#挖掘作业
casename = '挖掘作业保存'
caseinfo['id'] = 127
caseinfo['name'] = casename
workticketidx = workticketid + 2
ts = tsi + 2
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DT_MCQ_M/cardSave.json?level=1'
data = {
	"children": {
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "挖掘方案已审查通过",
				"riskrepositoryid": 2000000005147,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079424,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已落实现场安全监督",
				"riskrepositoryid": 2000000005148,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079425,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已确认土质类型",
				"riskrepositoryid": 2000000005149,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079426,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已办理断路申请",
				"riskrepositoryid": 2000000005150,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079427,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已考虑挖出物存放位置",
				"riskrepositoryid": 2000000005151,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079428,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已确定机具设备进入方式",
				"riskrepositoryid": 2000000005152,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079429,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "禁止使用铁棒、铁镐或抓斗等机具",
				"riskrepositoryid": 2000000005153,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079430,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已审查附图",
				"riskrepositoryid": 2000000005154,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079431,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已完成危险评估",
				"riskrepositoryid": 2000000005155,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079432,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已制定塌方保护措施",
				"riskrepositoryid": 2000000005156,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079433,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已设置围栏或路障",
				"riskrepositoryid": 2000000005157,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079434,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已考虑排水方式",
				"riskrepositoryid": 2000000005158,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079435,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "人工挖掘",
				"riskrepositoryid": 2000000005159,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079436,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "挖掘机具活动范围足够大",
				"riskrepositoryid": 2000000005160,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079437,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已对所有作业人员进行安全教育、交底",
				"riskrepositoryid": 2000000005161,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079438,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已制定紧急状态下的安全措施",
				"riskrepositoryid": 2000000005162,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079439,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已考虑对邻近结构物的影响",
				"riskrepositoryid": 2000000005163,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079440,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已落实逃离进出方式和设施",
				"riskrepositoryid": 2000000005164,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079441,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "需要的支护设施已就位",
				"riskrepositoryid": 2000000005165,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079442,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已落实警示标识",
				"riskrepositoryid": 2000000005166,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079443,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已准备跨越坑沟的设施",
				"riskrepositoryid": 2000000005167,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy21",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079444,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已制定挖掘作业安全检查表",
				"riskrepositoryid": 2000000005168,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy22",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079445,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其它：（）",
				"riskrepositoryid": 2000000005170,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy24",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "kzcsjqr",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079446,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "水管线，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005207,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy25",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079447,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "工艺管线，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005208,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy26",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079448,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "电气线路，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005209,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy27",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079449,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "仪表线路，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005210,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy28",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079450,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "消防管线，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005211,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy29",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079451,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "下水道，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005212,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy30",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079452,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "压缩气体，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005213,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy31",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079453,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他隐蔽设施，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005214,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy32",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079454,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他，管径、走向、深度、位置（），隔离阀/开关的位置（），参考图号（）",
				"riskrepositoryid": 2000000005215,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "wjzy33",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dt",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ybssqk",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079455,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"dig_size_l": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"dig_size_h": "",
		"tableName": "hse_work_ticket",
		"worktype_name": "挖掘作业",
		"territorialunitid": 2000000003339,
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"dig_size_w": "",
		"ver": 1,
		"tasktype": "",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"attaches_attachshowlist": [],
		"created_by": 1000,
		"attaches": 0,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 32,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"workside": "",
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"workway": "",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "dt",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"excavation_eqp": "",
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592531114767
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#挖掘作业
casename = '挖掘作业提交'
caseinfo['id'] = 128
caseinfo['name'] = casename

workticketidx = workticketid + 2
ts = tsi + 2
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GC_MCQ_M/submit.json?dataId=2000000007404&ts=1592532540145
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DT_MCQ_M/submit.json?dataId=%d&ts=1592532979916'%(workticketidx)
data = {
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"dig_size_l": "",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"dig_size_h": "",
		"tableName": "hse_work_ticket",
		"worktype_name": "挖掘作业",
		"territorialunitid": 2000000003339,
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"dig_size_w": "",
		"ver": 1,
		"tasktype": "",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"attaches_attachshowlist": [],
		"created_by": 1000,
		"attaches": 0,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 32,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"workside": "",
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"workway": "",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "dt",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"excavation_eqp": "",
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592532979916
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#断路作业
casename = '断路作业保存'
caseinfo['id'] = 129
caseinfo['name'] = casename
workticketidx = workticketid + 8
ts = tsi + 8
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DL_MCQ_M/cardSave.json?level=1'
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
				"worktype": "dl",
				"harmid": 2000000008682,
				"harmcode": "dlzy001",
				"harmname": "阻碍消防车通行",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033181,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dl",
				"harmid": 2000000008683,
				"harmcode": "dlzy002",
				"harmname": "妨碍人员及车辆在紧急情况下及时撤离",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033182,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dl",
				"harmid": 2000000008684,
				"harmcode": "dlzy003",
				"harmname": "路面受损坏",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033183,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dl",
				"harmid": 2000000008685,
				"harmcode": "dlzy004",
				"harmname": "断路作业的地下工艺管线、地下电力和通讯电缆受损",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033184,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "dl",
				"harmid": 2000000008686,
				"harmcode": "dlzy005",
				"harmname": "其他：（）",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033185,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
				"ismustconfirm": 0,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "作业前，制定交通组织方案（附后），并已通知相关部门或单位",
				"riskrepositoryid": 2000000005033,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dlzy01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dl",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079628,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业前，在断路的路口和相关道路上设置交通警示标志，在作业区附近设置路栏、道路作业警示灯、导向标等交通警示设施",
				"riskrepositoryid": 2000000005034,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dlzy02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dl",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079629,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "作业现场设置警戒线、围栏、警示牌",
				"riskrepositoryid": 2000000005035,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dlzy03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dl",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079630,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "夜间作业设置警示红灯",
				"riskrepositoryid": 2000000005036,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dlzy04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dl",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079631,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他补充的安全措施：（）",
				"riskrepositoryid": 2000000005037,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "dlzy05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "dl",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "aqcs",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079632,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"explain": 0,
		"hse_work_task_harm_mcq_m": 5,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workreason": "母鸡啊",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"otherunit": "",
		"level_upgrade": 0,
		"relevantdoc": "rd04",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"othercontent": "",
		"worktype_name": "断路作业",
		"territorialunitid": 2000000003339,
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"attaches_attachshowlist": [],
		"created_by": 1000,
		"attaches": 0,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 5,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"explain_attachshowlist": [],
		"worktype": "dl",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592531114768
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#断路作业
casename = '断路作业提交'
caseinfo['id'] = 130
caseinfo['name'] = casename
workticketidx = workticketid + 8
ts = tsi + 8
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_DL_MCQ_M/submit.json?dataId=%d&ts=1592533078484'%(workticketidx)
data = {
	"vo": {
		"explain": 0,
		"hse_work_task_harm_mcq_m": 5,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workreason": "母鸡啊",
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"otherunit": "",
		"level_upgrade": 0,
		"relevantdoc": "rd04",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"othercontent": "",
		"worktype_name": "断路作业",
		"territorialunitid": 2000000003339,
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"worklevel": "",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"attaches_attachshowlist": [],
		"created_by": 1000,
		"attaches": 0,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 5,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"explain_attachshowlist": [],
		"worktype": "dl",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592533078484
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#管线作业
casename = '管线作业保存'
caseinfo['id'] = 131
caseinfo['name'] = casename
workticketidx = workticketid + 3
ts = tsi + 3
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GX_MCQ_M/cardSave.json?level=1'
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
				"worktype": "gx",
				"harmid": 2000000008700,
				"harmcode": "gxzy001",
				"harmname": "压力",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033131,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008701,
				"harmcode": "gxzy002",
				"harmname": "可燃性",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033132,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008702,
				"harmcode": "gxzy003",
				"harmname": "毒性",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033133,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008703,
				"harmcode": "gxzy004",
				"harmname": "腐蚀性",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033134,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008704,
				"harmcode": "gxzy005",
				"harmname": "液体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033135,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008705,
				"harmcode": "gxzy006",
				"harmname": "辐射性",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033136,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008706,
				"harmcode": "gxzy007",
				"harmname": "气体",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033137,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008707,
				"harmcode": "gxzy008",
				"harmname": "温度",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033138,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008708,
				"harmcode": "gxzy009",
				"harmname": "第二能源",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033139,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"harmid": 2000000008709,
				"harmcode": "gxzy010",
				"harmname": "其他请注明：（）",
				"created_by": 1000,
				"tableName": "hse_work_task_harm",
				"worktaskharmid": 2000000033140,
				"updated_dt": now,
				"tenantid": 1,
				"updated_by": 1000,
				"worktaskid": worktaskidxx,
				"workticketid": workticketidx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000118,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016431,
				"equipmentcode": "aqyj",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000119,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016432,
				"equipmentcode": "qfbyz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000120,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016433,
				"equipmentcode": "aqm",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "耳罩",
				"dataStatus": 0,
				"worktype": "gx",
				"personequipmentid": 2000000000121,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016434,
				"equipmentcode": "ez",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000122,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016435,
				"equipmentcode": "fjdfz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000123,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016436,
				"equipmentcode": "aqx",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000124,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016437,
				"equipmentcode": "aqd",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000125,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016438,
				"equipmentcode": "fdmz",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000126,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016439,
				"equipmentcode": "zyshxq",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "化学防化服",
				"dataStatus": 0,
				"worktype": "gx",
				"personequipmentid": 2000000000127,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016440,
				"equipmentcode": "hxfhf",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000128,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016441,
				"equipmentcode": "st",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"isconfirm": 0
			}
		}, {
			"vo": {
				"isselect": 0,
				"ver": 1,
				"df": 0,
				"created_dt": now,
				"ismust": 1,
				"equipmentname": "防火隔热服",
				"dataStatus": 0,
				"worktype": "gx",
				"personequipmentid": 2000000000129,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016442,
				"equipmentcode": "fhgef",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
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
				"worktype": "gx",
				"personequipmentid": 2000000000130,
				"created_by": 1000,
				"tableName": "hse_work_task_equipment",
				"worktaskequipmentid": 2000000016443,
				"equipmentcode": "qtfh",
				"updated_dt": now,
				"updated_by": 1000,
				"tenantid": 1,
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"isconfirm": 0
			}
		}],
		"HSE_WORK_TASK_MEASURE_MCQ_M": [{
			"vo": {
				"measuredesc": "氮气置换",
				"riskrepositoryid": 2000000005061,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy01",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079456,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "蒸煮",
				"riskrepositoryid": 2000000005062,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy02",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079457,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "空气吹扫",
				"riskrepositoryid": 2000000005063,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy03",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079458,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "排气",
				"riskrepositoryid": 2000000005064,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy04",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079459,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "化学清洗",
				"riskrepositoryid": 2000000005065,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy05",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079460,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "水洗",
				"riskrepositoryid": 2000000005066,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy06",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079461,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "泄压",
				"riskrepositoryid": 2000000005067,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy07",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079462,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "排液",
				"riskrepositoryid": 2000000005068,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy08",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079463,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "气体检测合格",
				"riskrepositoryid": 2000000005069,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy09",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079464,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他请注明：（）",
				"riskrepositoryid": 2000000005070,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy10",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "ql",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079465,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "双重隔离",
				"riskrepositoryid": 2000000005071,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy11",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gl",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079466,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "双截止阀",
				"riskrepositoryid": 2000000005072,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy12",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gl",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079467,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "单截止阀",
				"riskrepositoryid": 2000000005073,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy13",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gl",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079468,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "凝固（固化）工艺",
				"riskrepositoryid": 2000000005074,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy14",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gl",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079469,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "已上锁挂牌",
				"riskrepositoryid": 2000000005075,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy15",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gl",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079470,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他请注明：（）",
				"riskrepositoryid": 2000000005076,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy16",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "gl",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079471,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "抽吸系统",
				"riskrepositoryid": 2000000005077,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy17",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079472,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "通风系统",
				"riskrepositoryid": 2000000005078,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy18",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079473,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "水管",
				"riskrepositoryid": 2000000005079,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy19",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079474,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "安全冲淋",
				"riskrepositoryid": 2000000005080,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy20",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079475,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "消防车",
				"riskrepositoryid": 2000000005081,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy21",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079476,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "泄漏收集桶",
				"riskrepositoryid": 2000000005082,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy22",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079477,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "砂袋",
				"riskrepositoryid": 2000000005083,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy23",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079478,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "吸油物品",
				"riskrepositoryid": 2000000005084,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy24",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079479,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "连接火炬",
				"riskrepositoryid": 2000000005085,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy25",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079480,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "救援",
				"riskrepositoryid": 2000000005086,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy26",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079481,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "路障/警戒线",
				"riskrepositoryid": 2000000005087,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy27",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079482,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "应急预案",
				"riskrepositoryid": 2000000005088,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy28",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079483,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}, {
			"vo": {
				"measuredesc": "其他请注明：（）",
				"riskrepositoryid": 2000000005089,
				"isselect": 0,
				"df": 0,
				"ver": 1,
				"created_dt": now,
				"measurecode": "gxzy29",
				"mesuresource": "qy",
				"ismust": 1,
				"dataStatus": 0,
				"worktype": "gx",
				"prepareperson": "1000",
				"created_by": 1000,
				"ismustphoto": 0,
				"measuretype": "yqxldkzsb",
				"tableName": "hse_work_task_measure",
				"updated_dt": now,
				"worktaskmeasureid": 2000000079484,
				"tenantid": 1,
				"updated_by": 1000,
				"preparepersonname": "测试用户",
				"workticketid": workticketidx,
				"worktaskid": worktaskidxx,
				"ismustconfirm": 0
			}
		}]
	},
	"vo": {
		"hse_work_task_harm_mcq_m": 10,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "rd03",
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"othercontent": "",
		"hse_work_task_equipment_m": 13,
		"worktype_name": "管线/设备打开",
		"haslineopensitemap": "1",
		"territorialunitid": 2000000003339,
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"tasktype": "comone08",
		"worklevel": "",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 1,
		"hse_work_task_measure_mcq_m": 29,
		"workcontent": "作业内容123",
		"pipeline_level": "",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"medium": "",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "gx",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"gas_aging": "",
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": worktaskidxx,
		"ts": 1592531114844
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#管线作业
casename = '管线作业提交'
caseinfo['id'] = 132
caseinfo['name'] = casename
workticketidx = workticketid + 3
ts = tsi + 3
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_GX_MCQ_M/submit.json?dataId=%d&ts=1592533162481'%(workticketidx)
data = {
	"vo": {
		"hse_work_task_harm_mcq_m": 10,
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "rd03",
		"beendelaynum": 0,
		"created_by_name": "卢健",
		"tableName": "hse_work_ticket",
		"aecolcode": 0,
		"othercontent": "",
		"hse_work_task_equipment_m": 13,
		"worktype_name": "管线/设备打开",
		"haslineopensitemap": "1",
		"territorialunitid": 2000000003339,
		"hassafetyplan": "1",
		"aecolcode_attachshowlist": [],
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"tasktype": "comone08",
		"worklevel": "",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"created_by": 1000,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"hse_work_task_measure_mcq_m": 29,
		"workcontent": "作业内容123",
		"pipeline_level": "",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"work_position_name": "制氢北区",
		"medium": "",
		"updated_by_name": "卢健",
		"tenantid": 1,
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"closereason": "",
		"worktype": "gx",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"gas_aging": "",
		"territorialunitcode": "CS8082020",
		"hashseplan": "",
		"worktaskid": worktaskidxx,
		"ts": 1592533162481
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#射线作业
casename = '射线作业保存'
caseinfo['id'] = 133
caseinfo['name'] = casename
workticketidx = workticketid + 10
ts = tsi + 10
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_SHEX_FY_M/cardSave.json?editId=%d&level=1'%(workticketidx)
data = {
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "rd03",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"othercontent": "",
		"worktype_name": "射线作业",
		"territorialunitid": 2000000003339,
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"tasktype": "comtwo05",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"attaches_attachshowlist": [],
		"created_by": 1000,
		"attaches": 0,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"controlrange": "",
		"radiosourcenum": "2",
		"work_position_name": "制氢北区",
		"sourcecode": "",
		"updated_by_name": "卢健",
		"radiosourcetype": "1",
		"tenantid": 1,
		"suprange": "",
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "shex",
		"safedistance": "10",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"sourcestrength": "",
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592531114769
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#射线作业
casename = '射线作业提交'
caseinfo['id'] = 134
caseinfo['name'] = casename
workticketidx = workticketid + 10
ts = tsi + 10
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_SHEX_FY_M/submit.json?dataId=%d&ts=1592533268164'%(workticketidx)
data = {
	"vo": {
		"df": 0,
		"sent_overdueclose_message": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": "0",
		"level_upgrade": 0,
		"relevantdoc": "rd03",
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_ticket",
		"othercontent": "",
		"worktype_name": "射线作业",
		"territorialunitid": 2000000003339,
		"territorialunitname": "运行一部",
		"is_pause": 0,
		"ver": 1,
		"tasktype": "comtwo05",
		"lock_status": 0,
		"planendtime": endtime,
		"applyunitname": "运行一部",
		"dataStatus": 0,
		"worktask_name": name,
		"isfireday": 0,
		"attaches_attachshowlist": [],
		"created_by": 1000,
		"attaches": 0,
		"worknumber": "",
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"isgas_detection": 0,
		"workcontent": "作业内容123",
		"workticketid": workticketidx,
		"close_type": "",
		"isupgrade": 0,
		"ticketdealphoto_attachshowlist": [],
		"controlrange": "",
		"radiosourcenum": "2",
		"work_position_name": "制氢北区",
		"sourcecode": "",
		"updated_by_name": "卢健",
		"radiosourcetype": "1",
		"tenantid": 1,
		"suprange": "",
		"workstatus": "draft",
		"istaskpause": 0,
		"actualstarttime": "",
		"actualendtime": "",
		"created_dt": now,
		"worktype": "shex",
		"safedistance": "10",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"isdue": 0,
		"updated_dt": now,
		"sourcestrength": "",
		"applyunitid": 2000000003339,
		"ticketdealphoto": 0,
		"territorialunitcode": "CS8082020",
		"worktaskid": worktaskidxx,
		"ts": 1592533268164
	}
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批-吊装和断路
casename = '合并审批-危害'
caseinfo['id'] = 135
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/harmHebinAudit.json?worktaskid=worktaskidxx&workType=zyrw&workTicketids=workticketidx1,workticketidx2&tabtype=harm&actionCode=harm
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/harmHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=harm&actionCode=harm'%(worktaskidxx,workticketidx1,workticketidx2)
data = {
	"mainAttributeVO": {},
	"voList": [{
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": now,
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"harmid": 2000000008682,
		"harmcode": "dlzy001",
		"harmname": "阻碍消防车通行",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000033181,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": worktaskidxx,
		"workticketid": workticketidx2,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}, {
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": now,
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"harmid": 2000000008683,
		"harmcode": "dlzy002",
		"harmname": "妨碍人员及车辆在紧急情况下及时撤离",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000033182,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": worktaskidxx,
		"workticketid": workticketidx2,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}, {
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": now,
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"harmid": 2000000008684,
		"harmcode": "dlzy003",
		"harmname": "路面受损坏",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000033183,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": worktaskidxx,
		"workticketid": workticketidx2,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}, {
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": now,
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"harmid": 2000000008685,
		"harmcode": "dlzy004",
		"harmname": "断路作业的地下工艺管线、地下电力和通讯电缆受损",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000033184,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": worktaskidxx,
		"workticketid": workticketidx2,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}, {
		"isselect": 0,
		"df": 0,
		"ver": 1,
		"created_dt": now,
		"ismust": 1,
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"harmid": 2000000008686,
		"harmcode": "dlzy005",
		"harmname": "其他：（好）",
		"created_by": 1000,
		"tableName": "hse_work_task_harm",
		"worktaskharmid": 2000000033185,
		"updated_dt": now,
		"tenantid": 1,
		"updated_by": 1000,
		"audittype": "",
		"worktaskid": worktaskidxx,
		"workticketid": workticketidx2,
		"ismustconfirm": 0,
		"isconfirm": 1,
		"signSrc": ""
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批
casename = '合并审批-安全措施'
caseinfo['id'] = 136
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/harmHebinAudit.json?worktaskid=worktaskidxx&workType=zyrw&workTicketids=workticketidx1,workticketidx2&tabtype=harm&actionCode=harm
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/measureHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=measure&businesstype=aqcs&actionCode=measure'%(worktaskidxx,workticketidx1,workticketidx2)
data = {
	"mainAttributeVO": {},
	"voList": [{
		"measuredesc": "作业前，制定交通组织方案（附后），并已通知相关部门或单位",
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
		"riskrepositoryid": 2000000005033,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dlzy01",
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "aqcs",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079628,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx2,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业前，在断路的路口和相关道路上设置交通警示标志，在作业区附近设置路栏、道路作业警示灯、导向标等交通警示设施",
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
		"riskrepositoryid": 2000000005034,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dlzy02",
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "aqcs",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079629,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx2,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业现场设置警戒线、围栏、警示牌",
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
		"riskrepositoryid": 2000000005035,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dlzy03",
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "aqcs",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079630,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx2,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "夜间作业设置警示红灯",
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
		"riskrepositoryid": 2000000005036,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dlzy04",
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "aqcs",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079631,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx2,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "其他补充的安全措施：（好咧）",
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
		"riskrepositoryid": 2000000005037,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dlzy05",
		"dataStatus": 0,
		"worktype": "dl",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "aqcs",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079632,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx2,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批
casename = '合并审批-起吊前检查-签字1'
caseinfo['id'] = 137
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/harmHebinAudit.json?worktaskid=worktaskidxx&workType=zyrw&workTicketids=workticketidx1,workticketidx2&tabtype=harm&actionCode=harm
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/measureHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=measure&businesstype=qdqjc&actionCode=measure'%(worktaskidxx,workticketidx1,workticketidx2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000006992",
		"latitude": 39.982739,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "作业单位措施确认及安全教育人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 2,
		"longitude": 116.338462
	}],
	"voList": [{
		"measuredesc": "1.吊装准备",
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
		"riskrepositoryid": 2000000004968,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy01",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079556,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "核实物件重量",
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
		"riskrepositoryid": 2000000004969,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy02",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079557,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "考虑吊装附件引起重量增加",
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
		"riskrepositoryid": 2000000004970,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy03",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079558,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "吊装角度适合（考虑最差角度）",
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
		"riskrepositoryid": 2000000004971,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy04",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079559,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "符合起重机额定载荷",
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
		"riskrepositoryid": 2000000004972,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy05",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079560,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "检查作业人员经过培训",
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
		"riskrepositoryid": 2000000004973,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy06",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079561,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "对起重机进行了检查和维护",
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
		"riskrepositoryid": 2000000004974,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy07",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079562,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "吊索具及附件满足能力需要",
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
		"riskrepositoryid": 2000000004975,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy08",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079563,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已检查吊索具及其附件无缺陷",
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
		"riskrepositoryid": 2000000004976,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy09",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079564,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已清楚物件的规格尺寸及重心",
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
		"riskrepositoryid": 2000000004977,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy10",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079565,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已明确物件的捆绑和固定方式",
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
		"riskrepositoryid": 2000000004978,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy11",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079566,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已制定吊挂货物的方法",
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
		"riskrepositoryid": 2000000004979,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy12",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079567,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "货物支撑物是否合适",
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
		"riskrepositoryid": 2000000004980,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy13",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079568,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "明确货物件吊运路线",
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
		"riskrepositoryid": 2000000004981,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy14",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079569,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "明确如何运输物件",
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
		"riskrepositoryid": 2000000004982,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy15",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079570,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "明确物件放置地点",
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
		"riskrepositoryid": 2000000004983,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy16",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079571,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "考虑物件吊装的平衡方法",
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
		"riskrepositoryid": 2000000004984,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy17",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079572,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否需要溜绳（或拉钩）",
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
		"riskrepositoryid": 2000000004985,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy18",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079573,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否需要物件缓冲防震保护",
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
		"riskrepositoryid": 2000000004986,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy19",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079574,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否考虑强风下物件稳定措施",
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
		"riskrepositoryid": 2000000004987,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy20",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079575,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否是带有突出物的物件",
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
		"riskrepositoryid": 2000000004988,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy21",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079576,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "支腿支撑加固措施落实",
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
		"riskrepositoryid": 2000000004989,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy22",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079577,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "天气情况是否适合吊装",
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
		"riskrepositoryid": 2000000004990,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy23",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079578,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "确认已落实应急措施",
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
		"riskrepositoryid": 2000000004991,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy24",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079579,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否需要梯子或脚手架",
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
		"riskrepositoryid": 2000000004993,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy26",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079581,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否已考虑辅助工具和设备",
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
		"riskrepositoryid": 2000000004994,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy27",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079582,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "吊装、移动过程中是否有障碍",
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
		"riskrepositoryid": 2000000004995,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy28",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079583,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*是否设置路障或警示标志",
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
		"riskrepositoryid": 2000000004996,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy29",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079584,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*警示区域是否涵盖作业半径",
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
		"riskrepositoryid": 2000000004997,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy30",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079585,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*地下设施已确认",
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
		"riskrepositoryid": 2000000004998,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy31",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079586,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*防火帽是否安装合格",
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
		"riskrepositoryid": 2000000004999,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy32",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079587,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "3.起重机及人员",
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
		"riskrepositoryid": 2000000005000,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy33",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079588,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已确定作业组中每一个人的任务",
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
		"riskrepositoryid": 2000000005001,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy34",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079589,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "司机的身体和心理状况良好",
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
		"riskrepositoryid": 2000000005002,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy35",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079590,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "操作室中能否清楚看到指挥信号",
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
		"riskrepositoryid": 2000000005003,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy36",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079591,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "司机是否有克服吊装盲点的措施",
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
		"riskrepositoryid": 2000000005004,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy37",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079592,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已明确指挥信号",
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
		"riskrepositoryid": 2000000005005,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy38",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079593,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*已确定吊装负责人",
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
		"riskrepositoryid": 2000000005006,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy39",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079594,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*已明确唯一的吊装指挥",
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
		"riskrepositoryid": 2000000005007,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy40",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079595,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*起重司机、指挥、司索是否持证上岗",
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
		"riskrepositoryid": 2000000005008,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy41",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079596,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*是否需要无线电通讯工具",
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
		"riskrepositoryid": 2000000005009,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy42",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079597,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*已进行吊装计划交底培训",
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
		"riskrepositoryid": 2000000005010,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy43",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079598,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*支腿处的地面平整、坚实",
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
		"riskrepositoryid": 2000000005011,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy44",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079599,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "4.其他（好多啊）",
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
		"riskrepositoryid": 2000000005012,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy45",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079600,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批
casename = '合并审批-起吊前检查-签字2'
caseinfo['id'] = 138
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/harmHebinAudit.json?worktaskid=worktaskidxx&workType=zyrw&workTicketids=workticketidx1,workticketidx2&tabtype=harm&actionCode=harm
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/measureHebinAudit.json?worktaskid=%d&workType=zyrw&workTicketids=%d,%d&tabtype=measure&businesstype=qdqjc&actionCode=measure'%(worktaskidxx,workticketidx1,workticketidx2)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000006991",
		"latitude": 39.982739,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "属地措施确认及安全教育人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.338462
	}],
	"voList": [{
		"measuredesc": "1.吊装准备",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004968,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy01",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079556,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "核实物件重量",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004969,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy02",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079557,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "考虑吊装附件引起重量增加",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAlbSURBVHic7d1Nq15nFQbgp5U4UPAD+gNKFarVIqRasB9qJmoGogWFWtAKrVBBnDp3\n6lgsBRGFUERQEQtOdGAcaEVB1KgEwYkIgqYRbSGhOQ6E0py9TnLS8671fLzXBZms0T3py83Z995t\nDQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAABO6GOttRdaa7/uHQQAWNOZ1trBq/5d6xsHAFjRpXZ94TjoGwd4tdt6\nBwDYkahg+I2DQdzeOwAAsD6FAwBIp3AAAOkUDgAgncIBAKRTOACAdAoHAJBO4QAA0ikcAEA6hQMA\nSKdwAADpFA5gBa8Pbv7nbTAQhQNYwT3B7c/lKYAjKRzACt4R3C6WpwCOpHAAK4j+wvHH8hTAkRQO\nYAVR4bhQngI4ksIBrODdwe0P5SkAgKUdBP9OdU0EXOe23gEAdiB6BdbvGwzEIxUAIJ3CAQCkUzgA\ngHQKBwCQTuEAZvfO4Pa38hTADSkcwOxOB7fflKcAbkjhAGZ3X3BTOGAwCgcwu/uD2/PlKQCApV1t\n26+M3tE1EbDhS3zA7HxlFCbgkQoAkE7hAADSKRwAQDqFA5jZncHtcnUI4OYUDmBmDwe38+UpgJtS\nOICZPRTcfl6eAgBY2oW2/QbHA10TASHvqgMzi77BcfsRd6Ajj1SA1SgbMCCFAwBIp3AAAOkUDmBW\np4Pb38tTAMeicACz+mhw+3F5CuBYFA5gVh8JbgoHALBTh7+/cdBae1PXRMCRfIcDmFX0+qvfNBiU\nRyoAQDqFAwBIp3AAM3owuP21OgRwfAoHMKNHgtsPylMAAEv7S9u+ofKBromAG7LoBmbkDRWYjEcq\nAEA6hQMASKdwALO5K7hdK08B3BKFA5hN9IbK98tTAABL+2XbvqHyWNdEwE1ZdQOzid5QeV3zWAWG\npnAAs/FKLEzIhgMASKdwADO5J7hdLU8B3DKFA5jJo8Ht2fIUAMDSLrbtGypnuyYCjsXQCpiJwShM\nyiMVACCdwgEApFM4gFk8FNz+UZ4CeE0UDmAWjwe3c+UpAIClXWnbN1Te0zURcGzW3cAsvKECE/NI\nBQBIp3AAM3hL7wDAySgcwAw+H9yeK08BACzt9207GP1U10TALTG4AmZgMAqT80gFAEincAAA6RQO\nYHSfCG4Xy1MAAEv7UdsORr/cNREAsJzDZeOgtfbmromAW2blDYzOGyqwABsOACCdwgGM7Exwu1ye\nAjgxhQMY2RPB7evlKQCApb3ctoPRt3dNBLwmhlfAyAxGYREeqQAA6RQOYFSng9vV8hTATigcwKii\nweg3ylMAAEu70raD0eivHsAEjK+AURmMwkI8UgEA0ikcwIjuC24GozAxhQMY0VPB7ZnyFADA0qIv\njN7bNRFwIgZYwIgMRmExHqkAAOkUDmA0DwS3l8pTADulcACjiQajT5enAACWdngsetBau7trIuDE\njLCA0RiMwoI8UgEA0ikcwEjOBrd/l6cAAJb2XNvuN77SNREAsJxoMHpH10TAThhiASMxGIVF2XAA\no/B7BAvzHzgwiieC24XyFADA0n7btvuNL3RNBAAsJxqMnuqaCNgZYyxgFAajsDAbDmAEXn2FxSkc\nwAi+FNx+Up4CAFja5bbdbzzSNRGwU56PAiOw34DFeaQCAKRTOIDe7uodAMincAC9PRXcflieAgBY\n2ottOxg92zURsHNGWUBvBqOwBzxSAQDSKRxAT+/qHQCooXAAPUWD0e+UpwAAlnalbQejH+oZCMhh\nmAX0ZDAKe8IjFQAgncIB9PLe4HatPAVQQuEAeokGo98qTwEALO3lth2M3t81EZDGOAvoxWAU9ohH\nKgBAOoUD6OHh4Ha1PAUAsLRzbbvf+FrXRADAcg6XjYPW2r1dEwGpDLSAHgxGYc/YcAAA6RQOoNqH\ng9tL5SkAgKV9r233G1/tmggAWE40GH1b10RAOiMtoJrBKOwhGw4AIJ3CAVQ6Hdx8YRT2gMIBVPps\ncDtXngIAWNqlth2MnumaCChhqAVUMhiFPeWRCgCQTuEAqpzqHQDoR+EAqjwe3H5VngIAWNrP2nYw\n+sWuiQCA5USfNH9D10RAGetwoIo3VGCP2XAAAOkUDqDC+4Pbi+UpgG4UDqDCZ4Lbt8tTAABL+2/b\nDkajv3oAizLYAioYjMKe80gFAEincADZfGsDUDiAdJ8LbuerQwAAa/tF2w5Gn+yaCABYTvRJc//n\nWNgzVuJANm+oADYcAEA+hQPI9MHg9kJ5CqA7hQPI9Fhw+2Z5CgBgaf9p28Ho+7omArow3AIyGYwC\nrTWPVACAAgoHkMXvC/AKPwhAlk8Gt9+VpwCGoHAAWR4Nbs+WpwAAlhZ90vzOnoGAfqzFgSzeUAFe\n4ZEKAJBO4QAyvLV3AGAsCgeQIfqk+U/LUwAASzvftoPRJ7smAgCWE72h8sauiYCuLMaBDN5QAa5j\nwwEApFM4gF27O7hdK08BDEXhAHYt+qT5d8tTAABL+1PbDkY/3jUR0J0RF7BrBqPAhkcqAEA6hQMA\nSKdwALv0YHC7VJ4CGI7CAezSp4PbufIUAMDS/tW2b6hEf/UA9ozlOLBL3lABQh6pAADpFA5glw4P\nRP/ZJQUAsLzn2/8frSgbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAABP5HycBPATyLX2uAAAAAElFTkSuQmCC\n",
		"riskrepositoryid": 2000000004970,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy03",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079558,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "吊装角度适合（考虑最差角度）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004971,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy04",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079559,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "符合起重机额定载荷",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAlbSURBVHic7d1Nq15nFQbgp5U4UPAD+gNKFarVIqRasB9qJmoGogWFWtAKrVBBnDp3\n6lgsBRGFUERQEQtOdGAcaEVB1KgEwYkIgqYRbSGhOQ6E0py9TnLS8671fLzXBZms0T3py83Z995t\nDQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAABO6GOttRdaa7/uHQQAWNOZ1trBq/5d6xsHAFjRpXZ94TjoGwd4tdt6\nBwDYkahg+I2DQdzeOwAAsD6FAwBIp3AAAOkUDgAgncIBAKRTOACAdAoHAJBO4QAA0ikcAEA6hQMA\nSKdwAADpFA5gBa8Pbv7nbTAQhQNYwT3B7c/lKYAjKRzACt4R3C6WpwCOpHAAK4j+wvHH8hTAkRQO\nYAVR4bhQngI4ksIBrODdwe0P5SkAgKUdBP9OdU0EXOe23gEAdiB6BdbvGwzEIxUAIJ3CAQCkUzgA\ngHQKBwCQTuEAZvfO4Pa38hTADSkcwOxOB7fflKcAbkjhAGZ3X3BTOGAwCgcwu/uD2/PlKQCApV1t\n26+M3tE1EbDhS3zA7HxlFCbgkQoAkE7hAADSKRwAQDqFA5jZncHtcnUI4OYUDmBmDwe38+UpgJtS\nOICZPRTcfl6eAgBY2oW2/QbHA10TASHvqgMzi77BcfsRd6Ajj1SA1SgbMCCFAwBIp3AAAOkUDmBW\np4Pb38tTAMeicACz+mhw+3F5CuBYFA5gVh8JbgoHALBTh7+/cdBae1PXRMCRfIcDmFX0+qvfNBiU\nRyoAQDqFAwBIp3AAM3owuP21OgRwfAoHMKNHgtsPylMAAEv7S9u+ofKBromAG7LoBmbkDRWYjEcq\nAEA6hQMASKdwALO5K7hdK08B3BKFA5hN9IbK98tTAABL+2XbvqHyWNdEwE1ZdQOzid5QeV3zWAWG\npnAAs/FKLEzIhgMASKdwADO5J7hdLU8B3DKFA5jJo8Ht2fIUAMDSLrbtGypnuyYCjsXQCpiJwShM\nyiMVACCdwgEApFM4gFk8FNz+UZ4CeE0UDmAWjwe3c+UpAIClXWnbN1Te0zURcGzW3cAsvKECE/NI\nBQBIp3AAM3hL7wDAySgcwAw+H9yeK08BACzt9207GP1U10TALTG4AmZgMAqT80gFAEincAAA6RQO\nYHSfCG4Xy1MAAEv7UdsORr/cNREAsJzDZeOgtfbmromAW2blDYzOGyqwABsOACCdwgGM7Exwu1ye\nAjgxhQMY2RPB7evlKQCApb3ctoPRt3dNBLwmhlfAyAxGYREeqQAA6RQOYFSng9vV8hTATigcwKii\nweg3ylMAAEu70raD0eivHsAEjK+AURmMwkI8UgEA0ikcwIjuC24GozAxhQMY0VPB7ZnyFADA0qIv\njN7bNRFwIgZYwIgMRmExHqkAAOkUDmA0DwS3l8pTADulcACjiQajT5enAACWdngsetBau7trIuDE\njLCA0RiMwoI8UgEA0ikcwEjOBrd/l6cAAJb2XNvuN77SNREAsJxoMHpH10TAThhiASMxGIVF2XAA\no/B7BAvzHzgwiieC24XyFADA0n7btvuNL3RNBAAsJxqMnuqaCNgZYyxgFAajsDAbDmAEXn2FxSkc\nwAi+FNx+Up4CAFja5bbdbzzSNRGwU56PAiOw34DFeaQCAKRTOIDe7uodAMincAC9PRXcflieAgBY\n2ottOxg92zURsHNGWUBvBqOwBzxSAQDSKRxAT+/qHQCooXAAPUWD0e+UpwAAlnalbQejH+oZCMhh\nmAX0ZDAKe8IjFQAgncIB9PLe4HatPAVQQuEAeokGo98qTwEALO3lth2M3t81EZDGOAvoxWAU9ohH\nKgBAOoUD6OHh4Ha1PAUAsLRzbbvf+FrXRADAcg6XjYPW2r1dEwGpDLSAHgxGYc/YcAAA6RQOoNqH\ng9tL5SkAgKV9r233G1/tmggAWE40GH1b10RAOiMtoJrBKOwhGw4AIJ3CAVQ6Hdx8YRT2gMIBVPps\ncDtXngIAWNqlth2MnumaCChhqAVUMhiFPeWRCgCQTuEAqpzqHQDoR+EAqjwe3H5VngIAWNrP2nYw\n+sWuiQCA5USfNH9D10RAGetwoIo3VGCP2XAAAOkUDqDC+4Pbi+UpgG4UDqDCZ4Lbt8tTAABL+2/b\nDkajv3oAizLYAioYjMKe80gFAEincADZfGsDUDiAdJ8LbuerQwAAa/tF2w5Gn+yaCABYTvRJc//n\nWNgzVuJANm+oADYcAEA+hQPI9MHg9kJ5CqA7hQPI9Fhw+2Z5CgBgaf9p28Ho+7omArow3AIyGYwC\nrTWPVACAAgoHkMXvC/AKPwhAlk8Gt9+VpwCGoHAAWR4Nbs+WpwAAlhZ90vzOnoGAfqzFgSzeUAFe\n4ZEKAJBO4QAyvLV3AGAsCgeQIfqk+U/LUwAASzvftoPRJ7smAgCWE72h8sauiYCuLMaBDN5QAa5j\nwwEApFM4gF27O7hdK08BDEXhAHYt+qT5d8tTAABL+1PbDkY/3jUR0J0RF7BrBqPAhkcqAEA6hQMA\nSKdwALv0YHC7VJ4CGI7CAezSp4PbufIUAMDS/tW2b6hEf/UA9ozlOLBL3lABQh6pAADpFA5glw4P\nRP/ZJQUAsLzn2/8frSgbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAABP5HycBPATyLX2uAAAAAElFTkSuQmCC\n",
		"riskrepositoryid": 2000000004972,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy05",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079560,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "检查作业人员经过培训",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004973,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy06",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079561,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "对起重机进行了检查和维护",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004974,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy07",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079562,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "吊索具及附件满足能力需要",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004975,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy08",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079563,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已检查吊索具及其附件无缺陷",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004976,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy09",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079564,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已清楚物件的规格尺寸及重心",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004977,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy10",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079565,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已明确物件的捆绑和固定方式",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004978,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy11",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079566,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已制定吊挂货物的方法",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004979,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy12",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079567,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "货物支撑物是否合适",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004980,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy13",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079568,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "明确货物件吊运路线",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004981,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy14",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079569,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "明确如何运输物件",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004982,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy15",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079570,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "明确物件放置地点",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004983,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy16",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079571,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "考虑物件吊装的平衡方法",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004984,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy17",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079572,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否需要溜绳（或拉钩）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004985,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy18",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079573,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否需要物件缓冲防震保护",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004986,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy19",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079574,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否考虑强风下物件稳定措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004987,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy20",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079575,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否是带有突出物的物件",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004988,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy21",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079576,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "支腿支撑加固措施落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004989,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy22",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079577,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "天气情况是否适合吊装",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004990,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy23",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079578,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "确认已落实应急措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004991,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy24",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079579,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否需要梯子或脚手架",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAlbSURBVHic7d1Nq15nFQbgp5U4UPAD+gNKFarVIqRasB9qJmoGogWFWtAKrVBBnDp3\n6lgsBRGFUERQEQtOdGAcaEVB1KgEwYkIgqYRbSGhOQ6E0py9TnLS8671fLzXBZms0T3py83Z995t\nDQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAABO6GOttRdaa7/uHQQAWNOZ1trBq/5d6xsHAFjRpXZ94TjoGwd4tdt6\nBwDYkahg+I2DQdzeOwAAsD6FAwBIp3AAAOkUDgAgncIBAKRTOACAdAoHAJBO4QAA0ikcAEA6hQMA\nSKdwAADpFA5gBa8Pbv7nbTAQhQNYwT3B7c/lKYAjKRzACt4R3C6WpwCOpHAAK4j+wvHH8hTAkRQO\nYAVR4bhQngI4ksIBrODdwe0P5SkAgKUdBP9OdU0EXOe23gEAdiB6BdbvGwzEIxUAIJ3CAQCkUzgA\ngHQKBwCQTuEAZvfO4Pa38hTADSkcwOxOB7fflKcAbkjhAGZ3X3BTOGAwCgcwu/uD2/PlKQCApV1t\n26+M3tE1EbDhS3zA7HxlFCbgkQoAkE7hAADSKRwAQDqFA5jZncHtcnUI4OYUDmBmDwe38+UpgJtS\nOICZPRTcfl6eAgBY2oW2/QbHA10TASHvqgMzi77BcfsRd6Ajj1SA1SgbMCCFAwBIp3AAAOkUDmBW\np4Pb38tTAMeicACz+mhw+3F5CuBYFA5gVh8JbgoHALBTh7+/cdBae1PXRMCRfIcDmFX0+qvfNBiU\nRyoAQDqFAwBIp3AAM3owuP21OgRwfAoHMKNHgtsPylMAAEv7S9u+ofKBromAG7LoBmbkDRWYjEcq\nAEA6hQMASKdwALO5K7hdK08B3BKFA5hN9IbK98tTAABL+2XbvqHyWNdEwE1ZdQOzid5QeV3zWAWG\npnAAs/FKLEzIhgMASKdwADO5J7hdLU8B3DKFA5jJo8Ht2fIUAMDSLrbtGypnuyYCjsXQCpiJwShM\nyiMVACCdwgEApFM4gFk8FNz+UZ4CeE0UDmAWjwe3c+UpAIClXWnbN1Te0zURcGzW3cAsvKECE/NI\nBQBIp3AAM3hL7wDAySgcwAw+H9yeK08BACzt9207GP1U10TALTG4AmZgMAqT80gFAEincAAA6RQO\nYHSfCG4Xy1MAAEv7UdsORr/cNREAsJzDZeOgtfbmromAW2blDYzOGyqwABsOACCdwgGM7Exwu1ye\nAjgxhQMY2RPB7evlKQCApb3ctoPRt3dNBLwmhlfAyAxGYREeqQAA6RQOYFSng9vV8hTATigcwKii\nweg3ylMAAEu70raD0eivHsAEjK+AURmMwkI8UgEA0ikcwIjuC24GozAxhQMY0VPB7ZnyFADA0qIv\njN7bNRFwIgZYwIgMRmExHqkAAOkUDmA0DwS3l8pTADulcACjiQajT5enAACWdngsetBau7trIuDE\njLCA0RiMwoI8UgEA0ikcwEjOBrd/l6cAAJb2XNvuN77SNREAsJxoMHpH10TAThhiASMxGIVF2XAA\no/B7BAvzHzgwiieC24XyFADA0n7btvuNL3RNBAAsJxqMnuqaCNgZYyxgFAajsDAbDmAEXn2FxSkc\nwAi+FNx+Up4CAFja5bbdbzzSNRGwU56PAiOw34DFeaQCAKRTOIDe7uodAMincAC9PRXcflieAgBY\n2ottOxg92zURsHNGWUBvBqOwBzxSAQDSKRxAT+/qHQCooXAAPUWD0e+UpwAAlnalbQejH+oZCMhh\nmAX0ZDAKe8IjFQAgncIB9PLe4HatPAVQQuEAeokGo98qTwEALO3lth2M3t81EZDGOAvoxWAU9ohH\nKgBAOoUD6OHh4Ha1PAUAsLRzbbvf+FrXRADAcg6XjYPW2r1dEwGpDLSAHgxGYc/YcAAA6RQOoNqH\ng9tL5SkAgKV9r233G1/tmggAWE40GH1b10RAOiMtoJrBKOwhGw4AIJ3CAVQ6Hdx8YRT2gMIBVPps\ncDtXngIAWNqlth2MnumaCChhqAVUMhiFPeWRCgCQTuEAqpzqHQDoR+EAqjwe3H5VngIAWNrP2nYw\n+sWuiQCA5USfNH9D10RAGetwoIo3VGCP2XAAAOkUDqDC+4Pbi+UpgG4UDqDCZ4Lbt8tTAABL+2/b\nDkajv3oAizLYAioYjMKe80gFAEincADZfGsDUDiAdJ8LbuerQwAAa/tF2w5Gn+yaCABYTvRJc//n\nWNgzVuJANm+oADYcAEA+hQPI9MHg9kJ5CqA7hQPI9Fhw+2Z5CgBgaf9p28Ho+7omArow3AIyGYwC\nrTWPVACAAgoHkMXvC/AKPwhAlk8Gt9+VpwCGoHAAWR4Nbs+WpwAAlhZ90vzOnoGAfqzFgSzeUAFe\n4ZEKAJBO4QAyvLV3AGAsCgeQIfqk+U/LUwAASzvftoPRJ7smAgCWE72h8sauiYCuLMaBDN5QAa5j\nwwEApFM4gF27O7hdK08BDEXhAHYt+qT5d8tTAABL+1PbDkY/3jUR0J0RF7BrBqPAhkcqAEA6hQMA\nSKdwALv0YHC7VJ4CGI7CAezSp4PbufIUAMDS/tW2b6hEf/UA9ozlOLBL3lABQh6pAADpFA5glw4P\nRP/ZJQUAsLzn2/8frSgbAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAABP5HycBPATyLX2uAAAAAElFTkSuQmCC\n",
		"riskrepositoryid": 2000000004993,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy26",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079581,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "是否已考虑辅助工具和设备",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004994,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy27",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079582,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "吊装、移动过程中是否有障碍",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004995,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy28",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079583,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*是否设置路障或警示标志",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004996,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy29",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079584,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*警示区域是否涵盖作业半径",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004997,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy30",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079585,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*地下设施已确认",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004998,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy31",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079586,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*防火帽是否安装合格",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000004999,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy32",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079587,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "3.起重机及人员",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005000,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy33",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079588,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已确定作业组中每一个人的任务",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005001,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy34",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079589,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "司机的身体和心理状况良好",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005002,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy35",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079590,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "操作室中能否清楚看到指挥信号",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005003,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy36",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079591,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "司机是否有克服吊装盲点的措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005004,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy37",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079592,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已明确指挥信号",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005005,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy38",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079593,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*已确定吊装负责人",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005006,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy39",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079594,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*已明确唯一的吊装指挥",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005007,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy40",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079595,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*起重司机、指挥、司索是否持证上岗",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005008,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy41",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079596,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*是否需要无线电通讯工具",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005009,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy42",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079597,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*已进行吊装计划交底培训",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005010,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy43",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079598,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "*支腿处的地面平整、坚实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005011,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy44",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079599,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}, {
		"measuredesc": "4.其他（好多啊）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": 0,
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 1,
		"audittype": "sign",
		"ismustconfirm": 0,
		"signSrc": "data:image/png;base64,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\n",
		"riskrepositoryid": 2000000005012,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dzzy45",
		"dataStatus": 0,
		"worktype": "dz",
		"person_name": "",
		"prepareperson": "1000",
		"created_by": 1000,
		"measuretype": "qdqjc",
		"updated_dt": now,
		"worktaskmeasureid": 2000000079600,
		"updated_by": 1000,
		"preparepersonname": "测试用户",
		"workticketid": workticketidx1,
		"worktaskid": worktaskidxx,
		"isconfirm": "1"
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批-会签
casename = '合并审批-申请人-签字'
caseinfo['id'] = 139
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid'%(workticketidx1,workticketidx2,worktaskidxx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006894",
		"latitude": 39.982713,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "申请人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.338462
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批-会签
casename = '合并审批-作业人-签字'
caseinfo['id'] = 140
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid'%(workticketidx1,workticketidx2,worktaskidxx)
data = {
	"mainAttributeVO": {
		"cardnum": "911CDA4D",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"latitude": 39.982725,
		"idnumber": "",
		"busdata": {
			"cardnum": "911CDA4D",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000009956,
			"person_name": "海顿测试"
		},
		"person_name": "海顿测试",
		"personid": 2000000009956,
		"specialworktype": "",
		"uuid": "1592534044330",
		"longitude": 116.338471
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006895",
		"personList": [{
			"cardnum": "911CDA4D",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"latitude": 39.982725,
			"idnumber": "",
			"busdata": {
				"cardnum": "911CDA4D",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000009956,
				"person_name": "海顿测试"
			},
			"person_name": "海顿测试",
			"personid": 2000000009956,
			"specialworktype": "",
			"uuid": "1592534044330",
			"longitude": 116.338471
		}],
		"latitude": 39.982725,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"name": "作业人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 2,
		"longitude": 116.338471
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批-会签
casename = '合并审批-属地监护人-签字'
caseinfo['id'] = 141
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid'%(workticketidx1,workticketidx2,worktaskidxx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006896",
		"latitude": 39.982872,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "属地监护人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 3,
		"longitude": 116.337939
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批-会签
casename = '合并审批-调度中心-签字'
caseinfo['id'] = 142
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid'%(workticketidx1,workticketidx2,worktaskidxx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007084",
		"latitude": 39.982664,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 15,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "调度中心",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 15,
		"longitude": 116.338416
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#合并审批-会签
casename = '合并审批-作业单位负责人-签字'
caseinfo['id'] = 143
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid'%(workticketidx1,workticketidx2,worktaskidxx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006999",
		"latitude": 39.982663,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 20,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "作业单位负责人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 20,
		"longitude": 116.33832
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#合并审批-会签
casename = '合并审批-属地单位批准人-签字'
caseinfo['id'] = 144
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid'%(workticketidx1,workticketidx2,worktaskidxx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007000",
		"latitude": 39.982691,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 21,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAArdSURBVHic7d1NyFxXGQfwJ5q2tpAUE5su/MIPJDtbFReN0FRM/UAUrBhLVy1KqBVx\nY6uLYvxA0a1QSqUoIgjWj9aNWBoRWiOSNFWhEAQXjVBITYoBG6WxeV0Epc6ce+fOzD3n3Hvn94NZ\nvM/inf+dxZt/7jn3TAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAwTpdHxO0RcSQithpef4qIm2oFBADGZ29E/CCay8Wi17mI2F86NAAwfIci4oVYvWQ0\nvQ4XvAYAYIDuj/4LRtPrLYWuCQAYgDujXMmYfT1W4PoAgEr2RMRzsV5Z+FlE3Nrw+/dFxH1L/C4A\nYEI+GKsXjAciYtcK73lFRDze4fe/fcVrAgAG4quxfMH4R1x69LVPpxa85x09vx8AUMA9sXzR+HDm\nTAcWvP+Dmd8fAOjJwViuZNxbIeOLLXkeqpAHAOjoXdG9ZJyMSyeG1nQ8mvM9UjEXANDgdHQrGg/X\nCtjgh9Gc9ZcVcwEAL/Pp6FY0vlsrYAdfj+bcj1bMBQAb7xXR7ejxJ2oFXNIXo/kavlkxFwBsrLti\ncdF4Ji6VkjFpKx37KuYCgI1zJhaXjVdXS7e+z0fzde2smAsANsL1sbho3F8tXb++HM3XCABk8pto\nLxovRcSVtcJlcjTS1/rvmqEAYIq2xaV/YNvKxn3V0uV3LtLXfLBmKACYknfH4iWU3dXSlWNpBQAy\neSTai8aJetGK2xbjO1cEAAavaRnhv68b60Wr5qFwlwMAerE92ovGxRjfuRp9mtrjvwBQ3N5oLxu/\nrxdtMH4V85/LsaqJAGBEbov2svGxetEGZVdYVgGAlTwY7WXjmnrRBknhAIAlHYvmonGhYq4hOx3z\nn9UNVRMBwICdjOaycbJirqG7N+Y/r59XTQQAA9VWNn5cMdcYXB2WVQBgobay8YWKucZE4QCAFr+O\n5rLx/oq5xkbhAIAG347msrG/XqxRUjgAIGF/KBt9uhjzn+NVVRMBwAA0lY1ba4YasaMx/1neVDUR\nUM0mf98DvFzT7f6vRMSPSgaZkFOJ2Z7iKYBBUDgg4hsN88ci4nDBHFNzNjF7TfEUwCAoHBDxpYb5\ngaIppudMYrareApgEBQONt23GubbiqaYJnc4gP9RONh0dydm3ymeYpr+lpjtLp4CGASFg012S8P8\nc0VTTNfOxOyF4imAQVA42GQPJGa/KJ5iulJPpDxXPAUwCAoHm+zJxOyjxVNM17WJ2eniKYBBUDjY\nZDfP/PzJKimmK3WHQ+GADbW9dgCozNMo+aTucKQ2kgIArOx8zB9t/saqiYBq/O8OyCV1XLy/ObCh\n7OEAALJTOACA7BQOACA7hQPIIXWeyTPFUwCDoXAAORxKzL5fOgQAMG2zj8NuhW+KhY3mETUgB4/E\nAv/HkgoAkJ3CAfTttsTsz8VTAACT9nTM79+4q2oioDprqkDf7N8A5lhSAQCyUziAPr0vMftX8RQA\nwKQdifn9G1+rmggAmJzUgV87qiYCBsFGLqBPNowCSfZwAH3ZXTsAMFwKB9CXexKzh4unAAAm7ULM\n79/YVzURMBjWVoG+2L8BNLKkAgBkp3AAffhIYnameAoAYNJSB37dXTURADA5qQO/rqyaCBgUG7qA\nPtgwCrSyhwNYlzsZwEIKB7CuzyRmR4qnAAAm7S8xv3/jlqqJgMGxxgqsy/4NYCFLKgBAdgoHsI7X\n1g4AjIPCAazjzsTsp8VTAACT9mzMbxg9UDURMEg2dgHrsGEU6MSSCgCQncIBrMoJo0BnCgewqjsS\ns8eLpwAAJu14zG8Yvb1qIgBgclJfSX9Z1UTAYNlNDqzKEypAZ/ZwAADZKRzAKt6amF0sngIYDYUD\nWMXHE7OfFE8BAEzasZjfMPqJqokAgMlJPaFyedVEwKDZUQ6swhMqwFLs4QAAslM4AIDsFA5gWe9N\nzJ4ungIYFYUDWNbNidmjxVMAAJN2IuafUPlA1UQAwOSkHol9ZdVEwOB5jA1YlkdigaXZwwEAZKdw\nAADZKRzAMrbXDgCMk8IBLOPGxOyp4imA0VE4gGXckJgdLZ4CGB2FA1jGvsTsd8VTAACTdj7mz+B4\nc9VEwCh4dh5YhjM4gJVYUgEAslM4AIDsFA4AIDuFAwDITuEAunpbYnameApglBQOoKt3JmZPFk8B\njJLCAXT1jsTsePEUwCgpHEBX1ydmJ4qnAAAm7fmYP2X0TVUTAaPhhECgK6eMAiuzpAIAZKdwAADZ\nKRwAQHYKBwCQncIBdHFNYnaheApgtBQOoIvrErM/FE8BjJbCAXShcABrUTiALhQOYC0KB9BF6lhz\nhQMA6NXskeZbEXFZ1UTAqDiWGOjCsebAWiypAADZKRwAQHYKBwCQncIBAGSncACL7KgdABg/hQNY\nZG9i9sfiKYBRUziARVKF42TxFMCoKRzAIgoHsDaFA1hE4QDWpnAAiygcAEB2F8P3qABr8l0IwCK+\nRwVYmyUVACA7hQMAyE7hAACyUzgAgOwUDgAgO4UDAMhO4QDavC4xe7Z4CmD0FA6gzRsSs1PFUwCj\np3AAbVKF46/FUwCjp3AAbRQOoBcKB9DGkgrQC4UDaPP6xMwdDmBpCgfQxpIKAJDd2Zj/avprqyYC\nRslXTANtfDU90AtLKgBAdgoHAJCdwgEAZKdwAADZKRwAQHYKBwCQncIBAGSncAAA2SkcAEB2CgcA\nkJ3CAQBkp3AAANkpHECTVyVmLxZPAUyCwgE02ZmYnSueApgEhQNocnVipnAAK1E4gCYKB9AbhQNo\nonAAvVE4gCYKB9AbhQNokiocfy+eApgEhQNo4g4H0BuFA2iyIzFzhwNYicIBNNmdmLnDAaxE4QCa\n7ErMni+eApgEhQNoonAAvVE4gCapJZWzxVMAk6BwAE3c4QAAsvtnRGzNvK6qmggYrW21AwCDtZWY\n+ZsBrMSSCgCQncIBAGSncAAA2SkcAEB2CgcAkJ3CAaTsTcxOFU8BTIbCAaR8KDH7bfEUAMCkPRHz\nh34drJoIAJic2bKxFRFXVE0EjJpTA4EUp4wCvbKHAwDITuEAZr0nMTtfPAUwKQoHMOtTidn3iqcA\nACbtpZjfMHpd1UTA6NkEBsyyYRTonSUVACA7hQOYdWjm589WSQEATN6eiDgc9m4AAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACMwH8Ax0QN\ngLB9Z/IAAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "属地单位批准人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\ngLB9Z/IAAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 21,
		"longitude": 116.338282
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#现场确认-合并审批-会签
casename = '合并审批-批准人-签字'
caseinfo['id'] = 145
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
#http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=2000000007401,2000000007403&worktaskid=2000000004560&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/signHebinAudit.json?workTicketids=%d,%d&worktaskid=%d&workType=zyrw&datatype=sign&actionCode=sign&hdBusKeyCode=worktaskid'%(workticketidx1,workticketidx2,worktaskidxx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006908",
		"latitude": 39.982666,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 24,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nAAAAwKT8fw6zi6f5Ylw2AAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "批准人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAABWXSURBVHic7d170G13XR7w5+Sc3E5zIyFcYqgmJXJJQWg7mlqngYo6mkCT2JZKEDo1\niBRabbEtYKUlBlsp0DQgtVOVUlt1WoJYFNtahqsZLoJTRIGABUyaQLjkSm7n8vaPlwPJeddv7f2+\n797ru9ben8/Mmszsk7P3s9c65/0+Z10TAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYU3uqAwAr45Qk\nD3/A8ogkD01yZ5I7HrB8JsknizICACP25CRXJfnjJBtLWH4/yfOSHDvUFwIA6hyT5O8m+XCWUyy2\ns/xKkscs9+sCAEM4I8m/S325mGf5+WwWIgBgAv5GkgOpLxC7WV618LUCLJWTRmE9nJnkg0m+Zcmf\nc0OSm5N8/gH/Pe1ry6lfW/781/IsykVJ3r7A9wMAtunyLG6vwruSvCCbpWHRLkhydTavYtlpvjcv\nIRfz+6tJ3pZvbI8P1cYBYAgvzM4H921JXp3k/MFTP9hPZ2f5b0nysIK86+YZSa5P/7a4qiwdAEv1\n3dn+gP5INg9LjNmFSf5vtve97k9yTkXYFfbibG8b3FMTE4BlOT6bP9znHQRX1sRciPOSfCXzf9dD\ncXntblyQzfK2k71Nv1iQF4Al+bHM98P/xiz2ZM0xeGPmH353J9lfE3OSrszOD8ttJPnS8JEBWJY/\nyewf/L9Zlm44z8z2DiHR9trsvGS8Lsu/EgqAgc364X9tXbQyj8z8w/GFRRnH6qpsv2C8siQpAIOZ\ndehgX120UTg9811iezAOszwr2ysZihrAmugbBlcX5hqjUzPfCY+vrQpY6LGZv2S8O24UCbBW+obC\n2YW5xm6ey4XvT7K3KuCA9mX+q3x+uSgjAIX6hoTHus/nVzJ7yP5YWbrl+9XMVzR+oSogALX6Hhfv\nCarbszfJnekfuLeWpVuOJ2W+ovG2qoAA1PtHaQ+IdTgEsCzPz+wB/G1l6RZnnkunP1mWDoBROCvt\nIXFKYa5VsTezTyr9n2XpducJmV00DmTzih4A1lxrUDyhMtQKenX6B/OhTGtv0rsyu2xcUhUOgHFp\nPRvln1aGWmEnZfaQHvtD7pLNvRZ93+HdddEAGJtfSPew+HRlqDXx3vQP7I/WRZtpVmE6qy4aAGPz\nTWkPDIZxQfoH9+GM7xDLF9PO6/kxAGzRGhonVIZaU7NOKP3OumgPcnnaGZ9RmAuAkfpyuofG8ytD\nrbm3pL90vLUu2tfZIwbA3F6a7qHxmcpQJEmenP7ScW9dtPxkI5M9YgBscUL8K3UKDqa/eJxWkKkr\nx28W5ABgAloD7IzKUHT6vfSXjosHzHJaIwMAbPHf0z00frYyFL0uSX/p+I2BcnRdmXLzQJ8NwIQ8\nOt0D657KUMzllPSXjs8t+fO/r/G5j1/y58KO7KkOAGuutfvb383puDvJiT2/vqxt6c8Ok+Kx1lDn\nnY3XnzVoCnZrf5Lren798BI+81Dj9VV4ui0AC/SQdO8Ov6kyFLvyo+k/xLIo/6nx/v91gZ8BwIpw\nCexqemLa2/aOBbz/I3reHwAe5EnpHhg/VBmKhTkj7VLwH3b53soGAHPrGhiVd6pk8fpu5HbSDt/z\nU433u2i3YQFYPY9L99B4WGUoluLMLG6PxAsa7/OFhSQFYOXcHvfcWCdXZPeF4+GN93AoBYCmrqFx\nemkilu2W7Lwo7O34vUeWxy02JgCr4pr4V+q6uiff2N7P2Mbva5WN/7bogACsjq7B8YLSRIzZEPf0\ngMG4BS4MY0+67zjp7yBdDqf9Z8OfGSZpX3UAWBOv63jt1sFTMAV9ezCUDQB6de0Wf2ppIsbm/PQf\nRjm5LhoAU+E4PH1em/6ycVZdNACm4jFROGj7cvrLxml10QCYkjdl6xB5Y2kixuBR6S8aG3HOBgDb\ncH+2DpJHlyai2i+lv2jcUhcNgKlyOIUjjklyIP1l45qydABMmsJBklyW2YdQzilLB8DkKRx8Ov1F\n47a6aACsgkdm63Bxw6/10fek1yPLlWXpAFgZ35+tA+adpYkYyuszu2ycUpYOBubW5rBc53W89snB\nUzC0u5Oc2PPr70jytIGywCgoHLBcx3W8du/gKRjKNyf57Iz/57FROllDx1QHgBWncKyPn0x/2fhS\nNm/kpWywlhQOWK5jO167Z/AULNsfJvnXPb/+4iRnDpQFRskhFViuP+147dzBU7BMh9L/j7c/k81z\nOmCt2cMBy/XxjtceO3gKlmFvNq80af0cvTGbh1CUDQCW7tRsvRTyvtJELMKZcXtyAEbGnUZXy19K\nf9n4trpoAKwzhWN1fFf6y8b+umgArLtD2TqYLipNxE58R9pF43BhLgBIkvybbB1Qt5cmYrv+Qtpl\n447CXADwIA6rTFdf2fhsXSwA2KprWL27NBHz6CsbnyjMBQCdXpTuofXwylD06isbHyvMBQC9WsOL\n8Xli2tvrw4W5AGCmH4wrHKbge6NsADBxN6Z7kB2sDMXXPS/KBgArou/GUdR5Xdrb5aOFuQBgR/an\nv3Q8tC7a2vofaW+PDxTmAoBdOSn9pePlddHWzufT3g7XFuYCgIWYVTpuq4u2NrpuO39k+bnCXACw\ncIfTXzwur4u2smYd1npuXTQAWJ6vpH8A3pfkhLJ0q+X70r+un1gXDQCW7xXpH4QbSd5Zlm41vC39\n6/ekumgAMJyHZHbp2EjywaqAE3ZX2uvzUGEuACjTd5nmA5frk5xWlHEqTkn/OryhLhoA1Nuf5EDm\nKx4bSf5OScpxuzj96+zVddEAYFwuzfylYyPJ+5KcXpJ0XGbtJTq/LhoAjNczs73isZHk15IcWxG2\nWN/5GhtJjqmLBgDT8MPZfvHYSHJNRdgCfevgc4W5AGCSzs3s+3e0lvck+dbhIy/Vuen/zv+qLhoA\nrIY3ZWfFYyPJl5P8zeEjL9TfjvM1AGAwZyX5SHZePjaSXJVkz9DBd+E/xvkaAFDmgiRfyO7KxzuS\nfMfQwbfhfWln/0phLgBYS09N8unsrnwcuerlnIGzt3wm7ZzvL8wFAGTzHh3XZvflYyPJ1UlOHjZ+\nkuSOnkxXFuQBAGZ4eZLD2X35uCfJy5LsXXLegz0ZnrrkzwYAFuCvZ/fnfRxZ7kjykiT7Fpivrxg9\neoGfAwAM5Kzs7nLbrj0gr0hy/A7z9L33GTt8TwBgZJ6c5O1ZXAG5K8k/znyXrfa9zzreuh0A1sb3\nJvn9LK6A3JTk8o7P6fs9U7pfCACwAM9KcmMWV0DeMePXAQDy7CTXZ3EFxJ4NAGCmv5XkU1lM4Xhf\nkicMGx8AmKIrktyc3ZeP27N5OAcAYKaXZjF7P142dHAAYDqWca7Hiwf9BgDAqM26GuWSJJ+d8f/1\nLYeT/NAg3wQAGKWdXPr62hm/r2/542w+wA4AWAN70l8M5n0I3BVJ7p7xXq3losV8FQBgrHayZ2OW\nv5bk1hnv3bW8ehefCQCM0L70D/9F3dTr6UnunPFZRy+vWdBnAwCFjs8wZeNo/2LG5x69vGRJOQCA\nJTslyzmMsh2nZnvPezl/oFwAwAI8LPVl42hvnZHpyPLlonwAwDack/GVjQe6OvMVjyuqAgIA/R6f\n9gA/VJiry89ndum4M55UCwCjckHag/v+wlyzfDyzi8eFZekAgK/7nrSH9V2FueZ1epKD6S8d76oK\nBwBs3r2zNaS/VJhrJ342/aXjvrpoALC+Lk17OH+uMNduHJfZezuOK0sHAGvm2WkP5E8U5lqUt6e/\ndPzZumgAsB6ek/Yg/lRhrkX7i+kvHU+siwYAq+15aQ/gzxTmWpYT0l86vrsuGgCspkvSHrw3FOYa\nQl/puLgwFwCslKelPXBvLsw1pHvTXgffWZgLAFZC37kM61I2jrgh7XXh4W8AsEOPS3vA3lKYq9J1\naa+ThxbmAoBJelTag3Xdn6r6qbTXDQAwp/1pD9TbCnONyV1ROgBgx/ZE2ZhXaz19sTIUAExBa4je\nWRlqxFrr65WVoQBgzA6le3geqAw1ciemXToeUZgLAEbptjgnYafOjXUHADP9SdoDc29hrim5Jt3r\n74OVoQBgLN6cdtl4eGGuKboj3evx5MpQAFDtWWmXje8qzDVlXevyYGkiACh0Xtpl4yWFuabu76d7\nnT69MhQAVDg27bLxO4W5VsXhOIEUAJpl43OVoVbIyelev3+lMhQADKlVNu6pDLWCvhh7OQBYUx+I\n+0UMpbWX4+zKUACwbM9Nu2wcU5hrld2drev6j0oTAcASnZl22TijMNeqOyf2JgGwRlpl42mVodaE\nS2QBWAv3pnvo/VZlqDXyi9m67u8tTQQAC/bedJcNj5oflsMqAKysZ8YVKWPRtQ1OK00EAAtwetpl\n46TCXOvqC9m6HX68NBEALECrbFxUGWqN/XS2bot3liYCgF3quvfDRpLfrQy15k7N1u1xW2kiANiF\n/53usvHVylAkcS4NACvikjhJdMxsFwAm77i0y8aphbn4BoUDgMlrlY3LKkPxIAoHAJPWOm/j3ZWh\neJCzs3X7HChNBADb8KR0l43DlaHY4kezdRu9vzQRLJHHT8Pq+YPG68cNmoJZfqDjtesGTwEAO/DV\ndO/duLQyFJ26HqB3QWkiAJjD1ekuG9dXhqLJCaMATM4j4n4bU2NbATA5rbLh6aPj9A/jChUAJuaG\ndJeNl1eGolfX+Rs/U5oIAHr8SLrLxq2VoZipa5vtKU0EAA19ty5nvP5cbDMAJqRVNs6rDMVMXZcu\n/3ZpIgBo+LfpLhtvqQzFXLq22/GliQCgQ+tQiqscxu+X43AKABNxME46nKqu7XZ5aSIA6PCKdA+t\nl1WGYi5Pib0bAEzA3jiUMmVd2+53SxMBQIf70j209lWGYi4/kO5t54ndAIzKZekeWK+qDMXcurbd\n50sTAUCHroF1uDQR82rdDXZvZSgAONob0z2w9leGYm5d2+4TpYkAoEPXwPqD0kTM6+fiyhQAJuCm\nGFhTtSfd2+69laEA4GiPTPfA+meVoZjbnVEWAZiAwzGwpuop6d52VxVmAoAtHp/ugfX4ylDMrWvb\nKYsAjE7X3o07ShMxr+vSXTbOqAwFAEdr7d04qTIUczkj3dvuuspQANCla+/GraWJmJdDKQBMgr0b\n0/WH6d52TynMBACduvZu3FmaiHk8Ld1l4+bKUADQ5fR0D63TKkMxF4dSAJiMP429G1N0X7rLxjmV\noQCgpWtonV2aiFnekO7t9luVoQCg5ZrYJT8156Z7mx2uDAUAfboG1z8oTUSf1oPZNpLsK8wFAE0X\nxt6NqWk95+Y5laEAoE/X4PpfpYnoc326t9n/qQwFALN0Da9jShPR8s/Tvb0OVYYCgFl+Kg6nTMVj\n4n4bAExU1/D64dJEdOk7SfRRhbkAYC7+tTwNrbLxE5WhAGAer487i07B3ekuGx+pDAUA8+oaYt9T\nmoijfTzd2+lgZSgAmFfrnADG49fjJFEAJu5l2TrEbihNxAM9N+2ycVxhLgDYloPZOsguKk3EEU9I\nu2x8c2EuANg2u+nH6fS0y8alhbkAYNvOjMIxRiekXTb+fWEuANiRX83Wgfbm0kQck3bZ+GhhLgDY\nsa6hdnZpIlpl4/bKULBK9lQHgDXUdfjE38U6rcNZB5McO2QQWGWeSAnDMsDGpfWU143YVrBQCgcM\nq+vBbO8fPAVJck/aPwP9bARg0n4vW88TuKI00Xq6M+4iCsAK6xpwdt0P6960y8bewlwAsDD+RV3r\n/rTLxv7CXACwUApHnQNpl42HFuYCgIX6pmwddDeWJlofXc+uObI8pDAXrI191QFgjfzljtc+OHiK\n9XM47fucnJrkjgGzwNpSOGA4F3S89oHBU6yXvkNWp2TzahVgAAoHDKdrD8eHBk+xPvrKxslJ7hoq\nCAAM6XBcGTGEPWmfr7GR5MS6aACwfK5QWb7j0182jq+LBgDDUDiW65T0lw03WANgLSgcy/Ow9JcN\nT+MFYG0oHMtxXvrLBgCsFcNw8b497aJxuDAXAJRROBbr4rTLxr2FuQCglMKxOM9Lu2zcXpgLAMop\nHIvxurTLxv8rzAUAo6Bw7N61aZeNPyrMBQCjoXDszvvSLhvvKcwFAKOicOzcx9MuG28tzAUAo3NT\ntg7LR5YmmoYvpF023lCYCwBG6R3ZOjCfXppo/O5Ou2z8RGEuABitv5etQ/M3ShON26G0y8ZlhbkA\nYNT2x3kc8+q7Vfm3F+YCgElQOPrtS3/Z+JayZAAwIQpH28npLxtn1EUDgGm5NVsH6YtKE43Do9Jf\nNo6viwYA0/NPsnWYrvtTTZ+c/rKxpy4aAEyXwyrf0PfE13UvYgCwK13D9TmliWr8VNpl46uFuQBg\nJXQN2gOliYb31rTLxg2FuQBgpazziZGfSLtsfKgwFwCsnAPZOmzX4fHqt6VdNv5zYS4AWEmtKzNW\n2eG0y8YLCnMBwErrGryvL020HCek/7LXC+uiAcDqe2lWfy/Ht6a/bJxdFw0A1kfXEH5VaaLFeU76\ny8YJddEAYL38l6zmXo5r44ZeADAqq7aX46a0y8ZXCnMBwFr7tazGXo5j0n8I5b110QCApHtAf6Q0\n0fY8Jv1l48q6aADAEa9J96DeXxlqTv8y/WXjgrpoAMDRpniC5S3pLxsn1kUDALpcmO6h/YrKUA2n\np79o3FUXDQCY5e50D/C9laGO8sr0l4331EUDAOaxN91DfCyPr78n/WXj++uiAQDb0dqD8JbCTJc1\nMjlfAwAmrDXUzx84x74kX+3Js5Hk5oEzAQALsi/tAX/sQBne1JPhyPLjA2UBAJbk0rQH/TK9qOdz\njyyHMlzxAQCW7GMZ7v4cL2x81tHLLy3hswGAYofSHv77FvD+v97z/g9c7kty/AI+DwAYqb4i8Owd\nvN/FM97z6OVHdhcfAJiKWaXgt2f8/kuT3DrH+zxwefuivwQAMG7HZntlYTfLhwf6TgDASC2zaLxh\nwO8BAIzcW7LYonH5sPEBgCn5ney8ZLymIC8AMGE/mOT96S8YH0vy/KqAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAwKT8fw6zi6f5Ylw2AAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 24,
		"longitude": 116.338469
	}]
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#作业处理-关闭合并-会签
casename = '作业处理-关闭合并-申请人-签字'
caseinfo['id'] = 146
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketHebinAudit.json?worktaskid=2000000004663&hdBusKeyCode=worktaskid&actionCode=close&workTicketids=2000000007735,2000000007737
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketHebinAudit.json?worktaskid=%d&hdBusKeyCode=worktaskid&actionCode=close&workTicketids=%d,%d'%(worktaskidxx,workticketidx1,workticketidx2)
data = {
	"reason": "完工",
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006909",
		"latitude": 39.98268,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nnYEDAOju/8NwLChWUc0DAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "申请人",
		"audittype": "sign,card",
		"specialworktype": "",
		"value": "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\nnYEDAOju/8NwLChWUc0DAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 1,
		"longitude": 116.338197
	}],
	"mainAttributeVO": {},
	"closeType": "completion"
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())


#作业处理-关闭合并-会签
casename = '作业处理-关闭合并-批准人-签字'
caseinfo['id'] = 146
caseinfo['name'] = casename
workticketidx1 = workticketid + 6
workticketidx2 = workticketid + 8
#ts = tsi + 10
#http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketHebinAudit.json?worktaskid=2000000004663&hdBusKeyCode=worktaskid&actionCode=close&workTicketids=2000000007735,2000000007737
#http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketHebinAudit.json?worktaskid=2000000004663&hdBusKeyCode=worktaskid&actionCode=close&workTicketids=2000000007735,2000000007737
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketHebinAudit.json?worktaskid=%d&hdBusKeyCode=worktaskid&actionCode=close&workTicketids=%d,%d'%(worktaskidxx,workticketidx1,workticketidx2)
data = {
	"reason": "完工",
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000006914",
		"latitude": 39.98268,
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 4,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\ntpTyvVzUenpxH4cNsrz1AQANKm3ZfVv4fIxrF55YAMDZ6GKaWYvtNF8HAJgjBQMAqG6s2QtviQAA\nRQ+hXAAAE9jH62LxHIdlkazzUwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgmH8B3R8G13wz2pwAAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "批准人",
		"audittype": "sign,card,face",
		"specialworktype": "",
		"value": "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\ntpTyvVzUenpxH4cNsrz1AQANKm3ZfVv4fIxrF55YAMDZ6GKaWYvtNF8HAJgjBQMAqG6s2QtviQAA\nRQ+hXAAAE9jH62LxHIdlkazzUwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgmH8B3R8G13wz2pwAAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 4,
		"longitude": 116.338197
	}],
	"mainAttributeVO": {},
	"closeType": "completion"
}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
if sta == 3200:
    #print("作业预约成功", sta)
    caseinfo['result'] = "pass"
else:
    caseinfo['result'] = "Fail"
    logger.info("%s错误结果%s", caseinfo['name'], data)
#收集用例执行信息
testsuitm.append(caseinfo.copy())

#
# logger.info('正在初始化数据库[名称：TESTDB]对象')
# testdb = MyDB('./config/dbconfig.conf', 'TESTDB')
# #用例执行
# for i in range(len(testsuitm)):
#     # 构造测试步骤对象
#     step_id = 1
#     step_number = 1
#     step_action = ''
#     testcase_name = testsuitm[i]['name']
#     testcase_steps = 1
#     testcase_isactive = 1
#     testsuite_id = 1
#     testsuite_name = "作业许可"
#     testplan = "plan1"
#     project_name = "changqing"
#     testcase_id = testsuitm[i]['id']
#     testproject = 'changqing'
#     preconditions = ''
#     host = "192.168.6.27"
#     port = "6030"
#     #case_executed_history_id = "20200602083321"
#     case_executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())
#     expected_results = ""
#     tc_external_id = 1
#     sql_insert = 'INSERT INTO ' + case_step_report_tb + '(executed_history_id, testcase_id, testcase_name, testplan, project, step_id, step_num, protocol_method, protocol, host, port, ' \
# 														'step_action, expected_results, runresult, reason, runtime)' \
# 														' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
#
#     data = (case_executed_history_id, testcase_id, testcase_name, testplan, testproject, step_id,
# 				step_number, '无', 'http', host, port,
# 				step_action, expected_results, 'Unexecuted', '', '0000-00-00 00:00:00')
#     logger.info('记录测试步骤到测试步骤报告表')
#     testdb.execute_insert(sql_insert, data)
#
#
#     fail_or_error_reason = ''
#     protocol_method = "Post"
#     #run_time =""
#     run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 记录运行时间
#     #logger.info("===================运行时间===========================")
#     #print(run_time)
#     action_of_step=""
#     if testsuitm[i]['result'] == "pass":
#         result_of_step ="pass"
#     else:
#         result_of_step = "Fail"
#     sql_update = 'UPDATE ' + case_step_report_tb + ' SET runresult=\"%s\",reason=\"%s\", protocol_method=\"%s\", runtime=\"%s\",' \
# 														   'step_action=\"%s\", expected_results=\"%s\"' \
# 														   ' WHERE executed_history_id = %s AND testcase_id = %s AND step_id = %s' \
# 														   ' AND project=\'%s\' AND testplan=\'%s\'  AND runtime=\'%s\''
#     data = ("pass", fail_or_error_reason, protocol_method, run_time, action_of_step, result_of_step,
# 					str(case_executed_history_id), testcase_id, step_id,
# 					testproject, testplan, '0000-00-00 00:00:00')
#     logger.info('正在更新步骤执行结果')
#     testdb.execute_update(sql_update, data)
#
#     logger.info('测试用例[id=%s, name=%s]执行成功' % (testcase_id, testcase_name))
# #结果处理
# for i in range(len(testsuitm)):
#     #print(testsuit[i])
#     # 构造测试用例对象
#     testcase_name = testsuitm[i]['name']
#     testcase_steps = 1
#     testcase_isactive = 1
#     testsuite_id = 1
#     testsuite_name= "作业许可"
#     testplan =  "plan1"
#     project_name = "changqing"
#     testcase_id = testsuitm[i]['id']
#     preconditions =''
#     tc_external_id = 1
#     #executed_history_id = "20200602083913"
#     #executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())
# 	#testcase_obj = TestCase(testcase_id, testcase_name, testcase_steps, testcase_isactive, project_name, testsuite_id, tc_external_id, preconditions)
#     try:
#         sql_insert = 'INSERT INTO ' + testcase_report_tb + '(executed_history_id, testcase_id, testcase_name, testsuit, testplan, project, runresult, runtime, tc_external_id)' \
# 														   ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
#         data = (executed_history_id, testcase_id, testcase_name, testsuite_name, testplan, project_name, 'Unexecuted',
# 				'0000-00-00 00:00:00', tc_external_id)
#         logger.info('记录测试用例到测试用例报表')
#         testdb.execute_insert(sql_insert, data)
#
#         #logger.info('开始执行测试用例[id=%s，name=%s]' % (testcase_id, testcase_name))
#         run_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 记录运行时间
#         case_executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 流水记录编号
#         if testsuitm[i]['result'] == "pass":
#             testcase_run_result = "pass"
#         else:
#             testcase_run_result = "Fail"
#         #testcase_run_result = testsuit[i]['result']
#
#         logger.info('正在更新用例执行结果')
#         sql_update = 'UPDATE ' + testcase_report_tb + ' SET runresult=\"%s\", runtime=\"%s\",' \
#                                              ' case_exec_history_id=\"%s\"' \
#                                              ' WHERE executed_history_id = %s and testcase_id = %s' \
#                                               ' AND project=\'%s\' AND testplan=\'%s\''
#         data = (testcase_run_result, run_time, str(case_executed_history_id), executed_history_id, testcase_id, project_name,
#         testplan)
#         testdb.execute_update(sql_update, data)
#     except Exception as e:
#         logger.error('运行用例出错 %s' % e)
#
# logger.info('接口测试已执行完成，正在关闭数据库连接')
# testdb.close()
# # 记录测试结束时间
# end_time = datetime.datetime.now()
# # 构造测试报告
# html_report = HtmlReport('test report', 'ushayden_interface_autotest_report')
# html_report.set_time_took(str(end_time - start_time))  # 计算测试消耗时间
#
# # 读取测试报告路径及文件名
# config = configparser.ConfigParser()
# config.read('./config/report.conf', encoding='utf-8')
# dir_of_report = config['REPORT']['dir_of_report']
# report_name = config['REPORT']['report_name']
#
# # 设置报告生成路
# html_report.mkdir_of_report(dir_of_report)
#
# # 生成测试报告
# html_report.generate_html(report_name)
#
# logger.info('生成测试报告成功')

for i in range(len(testsuitm)):
    #print(testsuitm(i)['id'],testsuitm(i)['name'],testsuitm(i)['result'])
    print("",testsuitm[i]['id'],testsuitm[i]['name'],testsuitm[i]['result'])

print(name)