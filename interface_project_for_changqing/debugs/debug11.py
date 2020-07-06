#用例信息变量定义
testsuit = [100]
caseinfo = {}
caseinfo['id'] = 1
caseinfo['""'] = ''
caseinfo['result'] = 0
caseinfo['url'] = ''
caseinfo['data'] = ''

#用例信息
count = 1
caseinfo['id'] = 1
caseinfo['""'] = '作业预约'



url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=111&topFuncCode=HSE_WORK_APPOINT&dataId=111&0.3707947936681053&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url2

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
	"created_dt": "",
	"updated_by": "",
	"updated_dt": "",
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
	"workname": "",
	"workcontent": "作业内容123",
	"worktypename": "作业许可证",
	"worktype": "xkz",
	"appointstarttime": "",
	"appointendtime": "",
	"material_medium": "物料介质123",
	"risksmeasures": "重点防控的风险123"
}
caseinfo['data'] =data
testsuit[0] = caseinfo
print(testsuit[0])
print(testsuit[0]['result'])