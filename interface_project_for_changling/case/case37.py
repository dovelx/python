#手机端主流程 作业任务添加

from case.case36 import *

from tools import getmdata
from tools import msql
case = '手机全流程'
#用例信息变量定义
testsuitm37 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

insert = getmdata.get_insert_code()

name = name
#作业任务添加m
url = 'http://192.168.6.156/m/hse_m/HSE_WORKAPPLY_GB_M/cardSave.json'

data = {
	"vo": {
		"df": 0,
		"workname": name,
		"workunitname": "中石化长岭分公司",
		"jsa_code": name,
		"created_by_name": "",
		"tableName": "hse_work_task",
		"insert__": insert,
		"territorialunitid": "2000000004016",
		"territorialdevicename": "炼油一部",
		"territorialunitname": "中石化长岭分公司",
		"gas_standard_type": "",
		"equipmentnumber": "",
		"worktickettype": "dh,sx,mbcd,gc,dz,lsyd,dt",
		"ver": 1,
		"planendtime": endtime,
		"work_appoint_name": name,
		"applyunitname": "中石化长岭分公司",
		"equipmentname": "",
		"dataStatus": 0,
		"wo_code": "",
		"created_by": "",
		"workunit": 2000000004016,
		"updated_by": "",
		"planstarttime": starttime,
		"isgas_detection": "",
		"workcontent": "内容",
		"territorialdeviceid": 2000000005066,
		"woid": "",
		"work_position_name": "炼油北区",
		"worktickettype_query": "",
		"worktools": "",
		"iscontractor": 0,
		"updated_by_name": "",
		"jsaid": jsaidx,
		"tenantid": 2000000001003,
		"projecttype": "rcjx",
		"workstatus": "draft",
		"created_dt": now,
		"work_property": "plan",
		"work_appoint_id": 2000000000547,
		"work_position_id": 2000000001891,
		"territorialdevicecode": "000000010300",
		"site": "北京",
		"updated_dt": now,
		"contractorname": "",
		"territorialunitcode": "00000001",
		"applyunitid": "2000000004016",
		"gas_aging": "",
		"worktaskid": ""
	}
}

caseinfo['id'] = 2001
caseinfo['name'] = '手机端作业任务添加m'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm37.append(caseinfo.copy())
#手机端作业任务提交
worktaskidxx = worktaskid+1
#worktaskidxx = msql.sql_query_worktaskid(name)
print("worktaskidxx",worktaskidxx)
url = 'http://192.168.6.156/m/hse_m/HSE_WORKAPPLY_GB_M/submit.json?dataId=%d&ts='%(worktaskidxx)

data = {
	"vo": {
		"df": 0,
		"workname": name,
		"workunitname": "中石化长岭分公司",
		"delaynum": 0,
		"jsa_code": name,
		"created_by_name": "长岭石化管理员",
		"beendelaynum": 0,
		"tableName": "hse_work_task",
		"territorialunitid": 2000000004016,
		"territorialdevicename": "炼油一部",
		"territorialunitname": "中石化长岭分公司",
		"gas_standard_type": "",
		"equipmentnumber": "",
		"worktickettype": "dh,sx,mbcd,gc,dz,lsyd,dt",
		"ver": 1,
		"planendtime": endtime,
		"work_appoint_name": name,
		"applyunitname": "中石化长岭分公司",
		"equipmentname": "",
		"iswfnotreport": 0,
		"dataStatus": 0,
		"wo_code": "",
		"created_by": 2000000012062,
		"pause": 0,
		"workunit": 2000000004016,
		"updated_by": 2000000012062,
		"planstarttime": starttime,
		"isgas_detection": "",
		"workcontent": "内容",
		"wf_audit_state": "0",
		"plan_type": 3,
		"territorialdeviceid": 2000000005066,
		"woid": "",
		"work_position_name": "炼油北区",
		"worktickettype_query": "",
		"worktools": "",
		"iscontractor": 0,
		"updated_by_name": "长岭石化管理员",
		"jsaid": jsaidx,
		"tenantid": 2000000001003,
		"projecttype": "rcjx",
		"workstatus": "draft",
		"created_dt": now,
		"work_property": "plan",
		"work_appoint_id": 2000000000547,
		"work_position_id": 2000000001891,
		"wf_create_user": 2000000012062,
		"territorialdevicecode": "000000010300",
		"site": "北京",
		"updated_dt": now,
		"contractorname": "",
		"territorialunitcode": "00000001",
		"applyunitid": 2000000004016,
		"gas_aging": "",
		"worktaskid": worktaskidxx
	}
}
caseinfo['id'] = 2002
caseinfo['name'] = '手机端作业任务提交'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm37.append(caseinfo.copy())