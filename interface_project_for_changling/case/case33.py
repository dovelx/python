#手机端主流程全票-全票-现场确认会签完毕

from case.case0 import *

#用例信息变量定义
testsuitm33 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

#作业预约

caseinfo['id'] = 3301
caseinfo['name'] = '作业预约-新增'
#http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardSave.json
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardSave.json'

data = {
	"add_attachs": [],
	"del_attachs": [],
	"vo": {
		"equt_name": "",
		"df": 0,
		"code": "",
		"workname": "作业任务名称",
		"territorialdeviceid": 2000000005070,
		"workunitname": "炼油一部",
		"appointendtime": endtime,
		"wf_instance": "",
		"iscontainfireday": "",
		"worktaskid_no": 0,
		"work_position_name": "脱硫区",
		"wf_current_user": "",
		"plantype": "",
		"wf_audit_time": "",
		"tableName": "hse_work_appoint",
		"iscontractor": "0",
		"insert__": "37c2f7d31a534c17b0ef26901d0f9e3a",
		"territorialunitid": 2000000005066,
		"territorialdevicename": "脱硫装置",
		"tenantid": 2000000001003,
		"territorialunitname": "炼油一部",
		"equipmentnumber": "",
		"ver": 1,
		"created_dt": now,
		"appointstarttime": starttime,
		"wf_current_nodeid": "",
		"worktype": "dh,sx,mbcd,gc,dz,lsyd,dt",
		"dataStatus": 0,
		"work_appoint_id": "",
		"standardmaintenance": "",
		"wf_type": "",
		"work_position_id": 2000000001499,
		"wf_create_user": "",
		"territorialdevicecode": "0000000103000008",
		"workunit": 2000000005066,
		"updated_dt": now,
		"worksite": "北京",
		"territorialunitcode": "000000010300",
		"workcontent": "",
		"status": "draft",
		"wf_audit_state": ""
	}
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm33.append(caseinfo.copy())

#作业预约
work_appoint_idx = sql_query_work_appointid+1
caseinfo['id'] = 3302
caseinfo['name'] = '作业预约-送交'
#http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardSave.json
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfSend.json?dataId=%d&ts='%(work_appoint_idx)

data = {
	"nodeStr": "2000000013477",
	"opinion": "申请审批",
	"2000000013477": "长岭石化管理员",
	"2000000013477_id": "2000000012062",
	"cCName": "",
	"cC": ""
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm33.append(caseinfo.copy())

#作业预约

caseinfo['id'] = 3303
caseinfo['name'] = '作业预约-审核'
#http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfFinish.json?dataId=2000000000473&ts=
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfFinish.json?dataId=%d&ts='%(work_appoint_idx)

data = {
	"cC": "2000000012062",
	"nickName": "cl",
	"nodeStr": "",
	"opinion": "同意",
	"cCName": "长岭石化管理员",
	"is_normal_finish": "true"
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm33.append(caseinfo.copy())

