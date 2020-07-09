#手机端主流程 预约，审批
from tools import tool
from globalpkg.global_var import sql_query_work_appointid
from tools import mname
from tools import minsert
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
testsuitm100 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

insert = minsert.get_insert_code()
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
caseinfo['id'] = 1
caseinfo['name'] = '手机端作业预约'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm100.append(caseinfo.copy())

#作业预约送交

#Url
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfSend.json?dataId=%d&ts='%(work_appoint_idx)
data= {"nodeStr":"2000000009070","opinion":"申请审批","2000000009070":"测试用户","2000000009070_id":"1000","cCName":"","cC":""}
caseinfo['id'] = 2
caseinfo['name'] = '作业预约送交'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm100.append(caseinfo.copy())

#作业预约审核
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_APPOINTAUDIT_M/wfFinish.json?dataId=%d&ts='%(work_appoint_idx)
data ={"cC":"1000","nickName":"用户","nodeStr":"","opinion":"同意","cCName":"测试用户","is_normal_finish":'true'}
caseinfo['id'] = 3
caseinfo['name'] = '作业预约审核'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm100.append(caseinfo.copy())
