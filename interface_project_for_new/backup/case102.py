#手机端主流程 作业任务添加

from backup.case101 import *
from backup.case100 import name
from tools import minsert

case = '手机全流程'
#用例信息变量定义
testsuitm102 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

insert = minsert.get_insert_code1()

name = name
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
caseinfo['id'] = 2001
caseinfo['name'] = '手机端作业任务添加m'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm102.append(caseinfo.copy())
#c
worktaskidxx = worktaskid+1
#worktaskidxx = msql.sql_query_worktaskid(name)
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
caseinfo['id'] = 2002
caseinfo['name'] = '手机端作业任务提交'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm102.append(caseinfo.copy())