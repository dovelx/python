#手机端主流程 预约，审批。pc安全，
import requests
import json
#from globalpkg.global_var import work_appoint_id
from tools import tool
from globalpkg.global_var import tsi
from globalpkg.global_var import workticketid
from globalpkg.global_var import worktaskid
#from case.case1 import *
from tools import tool
from globalpkg.global_var import jsaid
from globalpkg.global_var import safeclarid
from globalpkg.global_var import sql_query_work_appointid
#from runners.runner2 import inse
from runners import m_login
from case import datas
from runners import pc_login
#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime
#作业预约名称
name = tool.ran_name_with_str()
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



caseinfo['id'] = 100
caseinfo['name'] = '获取insertid'
caseinfo['flag'] = 'get'
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardAdd.json'

caseinfo['url'] = url
#caseinfo['data'] =data
mheaders = m_login.mlogin(1, 1, 1)
headers = datas.headers
cookies = pc_login.cookies
#testsuitm.append(caseinfo.copy())
rs = requests.get(url=caseinfo['url'], headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
# json化
data = json.loads(data)
# 获取接口返回状态
print("data", data)
sta = data['status']
# if caseinfo['id'] == 100:
insert = data['data']['data']['insert__']

print(sta)
#workticketidxxx = workticketid +1

#作业预约
work_appoint_idx = sql_query_work_appointid+1
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
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm.append(caseinfo.copy())
rs = requests.post(url = caseinfo['url'],json=caseinfo['data'],headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
print(sta)

#作业预约送交
#Url
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfSend.json?dataId=%d&ts='%(work_appoint_idx)
data= {"nodeStr":"2000000009070","opinion":"申请审批","2000000009070":"测试用户","2000000009070_id":"1000","cCName":"","cC":""}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
print(sta)

#作业预约审核
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfFinish.json?dataId=%d&ts='%(work_appoint_idx)

data ={"cC":"1000","nickName":"用户","nodeStr":"","opinion":"同意","cCName":"测试用户","is_normal_finish":'true'}
rs = requests.post(url = url,json=data,headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
print(sta)

#work_appoint_idx = work_appoint_idx-1
#安全分析及交底保存
casename = '安全分析及交底保存'
caseinfo['id'] = 4
caseinfo['name'] = casename
urlfenxi ='http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK_RISK&0.6529845051499572&contentType=json&ajax=true&tid=1'
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
print(data)
# 获取接口返回状态
#sta = data['status']

#if sta != 3200:
#    print(sta)
    #print(data)

#安全分析步骤添加接口用例信息
jsaidxx = jsaid+1
print ("安全分析步骤添加使用ID:",jsaidxx)

casename = '安全分析步骤添加'
caseinfo['id'] = 5
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
print(sta)

#安全分析步保存加接口用例信息
casename = '安全分析保存'
caseinfo['id'] = 6
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
print(sta)
#安全交底，环境影响大
casename = '安全交底'
caseinfo['id'] = 7
caseinfo['name'] = casename
safeclaridxx = safeclarid+1
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
	"worktaskid": jsaid,
	"work_position_id": 2000000002019
}
rs = requests.post(url=url, json=data, headers=headers, cookies=cookies)
# 返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
# 获取接口返回状态
sta = data['status']
print(sta)

#安全送交接口用例信息

casename = '安全送交'
caseinfo['id'] = 8
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
print(sta)
#作业任务添加m预制任务
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKAPPLY_MCQ_M/cardAdd.json'
rs = requests.get(url=url, headers=mheaders)
# 返回值转码
data = rs.content.decode('utf-8')
# json化
data = json.loads(data)
# 获取接口返回状态
print("data", data)
sta = data['status']
# if caseinfo['id'] == 100:
insert = data['data']['data']['insert__']

print(sta)
#作业任务添加m
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
		"jsaid": 2000000001875,
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
print(data)
print(sta)
#作业任务提交
worktaskidxx = worktaskid+1
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
print(data)
print(sta)