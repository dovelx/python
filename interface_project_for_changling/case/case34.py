#手机端主流程全票-作业处理-其他操作

from case.case0 import *

#用例信息变量定义
testsuitm34 = []
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

caseinfo['id'] = 3401
caseinfo['name'] = '作业处理-用火作业-气体复测'
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
testsuitm34.append(caseinfo.copy())