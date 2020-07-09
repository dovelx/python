#手机端主流程全票-全票-作业预约-审核

from globalpkg.global_var import sql_query_jsa_step_harm_id
from tools import tool
from globalpkg.global_var import tsi
from globalpkg.global_var import workticketid
from globalpkg.global_var import worktaskid
from globalpkg.global_var import worktaskid1
from globalpkg.global_var import jsaid
from globalpkg.global_var import safeclarid
from globalpkg.global_var import sql_query_work_appointid
from globalpkg.global_var import sql_query_jsastepid
from globalpkg.global_var import sql_query_jsa_step_measure_id
from tools.getmdata import getinsert

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


case = '长岭项目作业许可'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)
#作业预约

caseinfo['id'] = 3301
caseinfo['name'] = '作业预约-新增'
#http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardSave.json
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/cardSave.json'
insert = getinsert()
data = {
	"add_attachs": [],
	"del_attachs": [],
	"vo": {
		"equt_name": "",
		"df": 0,
		"code": "",
		"workname": name,
		"territorialdeviceid": 2000000005066,
		"workunitname": "中石化长岭分公司",
		"appointendtime": endtime,
		"wf_instance": "",
		"iscontainfireday": "",
		"worktaskid_no": 0,
		"work_position_name": "炼油北区",
		"wf_current_user": "",
		"plantype": "",
		"wf_audit_time": "",
		"tableName": "hse_work_appoint",
		"iscontractor": "0",
		"insert__": insert,
		"territorialunitid": 2000000004016,
		"territorialdevicename": "炼油一部",
		"tenantid": 2000000001003,
		"territorialunitname": "中石化长岭分公司",
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
		"work_position_id": 2000000001891,
		"wf_create_user": "",
		"territorialdevicecode": "000000010300",
		"workunit": 2000000004016,
		"updated_dt": now,
		"worksite": "北京",
		"territorialunitcode": "",
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

