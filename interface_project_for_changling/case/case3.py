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
from tools import getdata

case = '长岭项目作业许可-PC-预约-修改-删除'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)


#用例信息变量定义
testsuit3 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业预约-添加'
caseinfo['isactive'] = 1
#拼写预约URL
#http://192.168.6.156/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_APPOINT&0.899866420894208&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_APPOINT&0.899866420894208&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
#全票数据
data = {
	"tableName": "hse_work_appoint",
	"iscontractor": "0",
	"workunitname_no": "",
	"territorialunitid": 2000000004016,
	"worktaskid_no": 0,
	"territorialunitname": "中石化长岭分公司",
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000001003,
	"ts": "",
	"isspecialcondition": "",
	"plantype": "",
	"wf_audit_state": "",
	"territorialdeviceid": 2000000005066,
	"territorialdevicename": "炼油一部",
	"territorialdevicecode": "000000010300",
	"work_position_id": 2000000001791,
	"work_position_name": "炼油一部",
	"worksite": "作业地点",
	"workunit": 2000000004016,
	"workunitname": "中石化长岭分公司",
	"workname": name,
	"worktypename": "用火作业,受限空间,盲板抽堵,高处作业,起重作业,临时用电,动土作业",
	"worktype": "dh,sx,mbcd,gc,dz,lsyd,dt",
	"appointstarttime": starttime,
	"appointendtime": endtime
}
caseinfo['data'] =data
testsuit3.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = '作业预约-修改'
caseinfo['isactive'] = 1
#拼写预约URL
work_appointid = sql_query_work_appointid+1
#http://192.168.6.156/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=2000000000427&topFuncCode=HSE_WORK_APPOINT&dataId=2000000000427&0.8196616519099322&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.8196616519099322&contentType=json&ajax=true&tid=2000000001003'%(work_appointid,work_appointid)
caseinfo['url'] = url
#全票数据
data = {
	"tableName": "hse_work_appoint",
	"task_worktype_code": "",
	"equt_name": "",
	"territorialdeviceid": 2000000005066,
	"created_by_name_nick": "cl",
	"worktaskid_no": 0,
	"cywlqfyxzz": "",
	"specialenvironment": "",
	"isreport": "",
	"plantype": "",
	"created_by_name": "长岭石化管理员",
	"worklevel_dh": "",
	"iscontainplayday": "",
	"worktype_name": "用火作业,受限空间,盲板抽堵,高处作业,起重作业,临时用电,动土作业",
	"territorialdevicename": "炼油一部",
	"worktypename": "用火作业,受限空间,盲板抽堵,高处作业,起重作业,临时用电,动土作业",
	"worklevel_gx": "",
	"task_worktype_name": "",
	"standardmaintenance": "",
	"worklevel_sx": "",
	"material_medium": "",
	"risksmeasures": "",
	"issjtssxzy": "",
	"territorialdevicecode": "000000010300",
	"isupgradedh": "",
	"isdzdh": "",
	"worklevel_gc": "",
	"persistent_type": "",
	"territorialunitcode": "",
	"worklevel_dz": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 2000000012062,
	"created_dt": now,
	"updated_by": 2000000012062,
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000001003,
	"ts": "",
	"work_appoint_id": work_appointid,
	"code": "",
	"iscontractor": "0",
	"workunit": 2000000004016,
	"workunitname": "中石化长岭分公司",
	"workunitname_no": "中石化长岭分公司",
	"workcontent": "",
	"workname": "modify",
	"territorialunitid": 2000000004016,
	"territorialunitname": "中石化长岭分公司",
	"work_position_id": 2000000001791,
	"appointstarttime": starttime,
	"appointendtime":endtime,
	"work_position_name": "炼油一部",
	"status": "draft",
	"constructionscheme": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 2000000012062,
	"wf_type": "",
	"wf_instance": "",
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"worktype": "dh,sx,mbcd,gc,dz,lsyd,dt",
	"worksite": "作业地点",
	"equipmentnumber": "",
	"projecttype": "",
	"isspecialcondition": "",
	"specialcondition": ""
}
caseinfo['data'] =data
testsuit3.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = '作业预约-删除'
caseinfo['isactive'] = 1
#拼写预约URL
work_appointid = work_appointid-1
#http://192.168.6.156/hse/HSE_WORK_APPOINT/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=2000000000429&topFuncCode=HSE_WORK_APPOINT&dataId=2000000000427&0.09290835707212919&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.09290835707212919&contentType=json&ajax=true&tid=2000000001003'%(work_appointid,work_appointid)
caseinfo['url'] = url
#全票数据
data = [work_appointid]
caseinfo['data'] =data
testsuit3.append(caseinfo.copy())