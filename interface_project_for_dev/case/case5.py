#作业预约修改，复制和删除
from globalpkg.global_var import work_appoint_id
from tools import tool
from globalpkg.global_var import tsi
from globalpkg.global_var import workticketid
from globalpkg.global_var import worktaskid
from globalpkg.global_var import jsaid
from globalpkg.global_var import safeclarid
from globalpkg.global_var import sql_query_work_appointid
from tools.gethost import host
from tools.gethost import pro

case = '作业预约修改，复制和删除'
projectname = pro()
host = host(projectname)
print(host)
#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime
#作业预约名称
name = tool.ran_name_with_str()
print(name)
#用例信息变量定义
testsuit5 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''
#work_appoint_id_plus1=  work_appoint_id+1

#作业预约创建使用ID
work_appoint_id_plus1 = sql_query_work_appointid+1
#work_appoint_id_plus1 = work_appoint_id_plus1
count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业预约'
caseinfo['isactive'] = 1
#拼写预约URL
url2='http://%s/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.3707947936681053&contentType=json&ajax=true&tid=1'%(host,work_appoint_id_plus1,work_appoint_id_plus1)
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
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
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
	"workname": name,
	"workcontent": "作业内容123",
	"worktypename": "作业许可证",
	"worktype": "xkz",
	"appointstarttime": starttime,
	"appointendtime": endtime,
	"material_medium": "物料介质123",
	"risksmeasures": "重点防控的风险123"
}
caseinfo['data'] =data
testsuit5.append(caseinfo.copy())

#作业预约修改接口
#用例信息
caseinfo['id'] = 2
caseinfo['name'] = '作业预约修改接口'
caseinfo['isactive'] = 1
url = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.18905889749571658&contentType=json&ajax=true&tid=1'%(work_appoint_id_plus1,work_appoint_id_plus1)
data = {
	"tableName": "hse_work_appoint",
	"task_worktype_code": "QT",
	"equt_name": "",
	"territorialdeviceid": 2000000003454,
	"created_by_name_nick": "用户",
	"worktaskid_no": 0,
	"cywlqfyxzz": "0",
	"specialenvironment": "ALLNOT",
	"isreport": "0",
	"created_by_name": "测试用户",
	"worklevel_dh": "",
	"sourcecode": "",
	"iscontainplayday": "",
	"worktype_name": "作业许可证",
	"sourcefunc": "",
	"equipmentcode": "",
	"territorialdevicename": "制氢装置",
	"sourcetype": "",
	"worktypename": "作业许可证",
	"sourceid": "",
	"worklevel_gx": "",
	"serviceplanid": "",
	"task_worktype_name": "其他",
	"standardmaintenance": "",
	"worklevel_sx": "",
	"material_medium": "物料介质123",
	"risksmeasures": "重点防控的风险123",
	"issjtssxzy": "0",
	"isupgradedh": "0",
	"isdzdh": "0",
	"worklevel_gc": "",
	"persistent_type": "newoperation",
	"territorialunitcode": "CS8082020",
	"worklevel_dz": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"work_appoint_id": work_appoint_id_plus1,
	"code": "",
	"iscontractor": "0",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workunitname_no": "长庆石化分公司",
	"workcontent": "作业内容123",
	"workname": name,
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"work_position_id": 2000000002019,
	"appointstarttime": starttime,
	"appointendtime": endtime,
	"work_position_name": "制氢北区",
	"status": "draft",
	"constructionscheme": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_type": "",
	"wf_instance": "",
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"worktype": "xkz",
	"worksite": "作业地点1234455",
	"equipmentnumber": "",
	"projecttype": "rcjx",
	"isspecialcondition": "",
	"specialcondition": ""
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit5.append(caseinfo.copy())

#作业预约复制
#用例信息
caseinfo['id'] = 3
caseinfo['name'] = '作业预约复制'
caseinfo['isactive'] = 1
url = "http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.6280400811634435&contentType=json&ajax=true&tid=1"%(work_appoint_id_plus1,work_appoint_id_plus1)

data = {
	"tableName": "hse_work_appoint",
	"task_worktype_code": "QT",
	"": "",
	"equt_name": "",
	"territorialdeviceid": 2000000003454,
	"created_by_name_nick": "用户",
	"worktaskid_no": 0,
	"cywlqfyxzz": "0",
	"specialenvironment": "ALLNOT",
	"isreport": "0",
	"created_by_name": "测试用户",
	"worklevel_dh": "",
	"sourcecode": "",
	"updated_by_name": "测试用户",
	"iscontainplayday": "",
	"worktype_name": "作业许可证",
	"sourcefunc": "",
	"equipmentcode": "",
	"territorialdevicename": "制氢装置",
	"sourcetype": "",
	"worktypename": "作业许可证",
	"sourceid": "",
	"worklevel_gx": "",
	"serviceplanid": "",
	"task_worktype_name": "其他",
	"standardmaintenance": "",
	"worklevel_sx": "",
	"material_medium": "物料介质123",
	"risksmeasures": "重点防控的风险123",
	"issjtssxzy": "0",
	"isupgradedh": "0",
	"isdzdh": "0",
	"worklevel_gc": "",
	"funccode": "HSE_WORK_APPOINT",
	"persistent_type": "newoperation",
	"territorialunitcode": "CS8082020",
	"worklevel_dz": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"work_appoint_id": work_appoint_id_plus1,
	"code": "",
	"iscontractor": "0",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workunitname_no": "长庆石化分公司",
	"workcontent": "作业内容123",
	"workname": name,
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"work_position_id": 2000000002019,
	"appointstarttime": starttime,
	"appointendtime": endtime,
	"work_position_name": "制氢北区",
	"status": "draft",
	"constructionscheme": 0,
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_type": "",
	"wf_instance": "",
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"worktype": "xkz",
	"worksite": "作业地点123",
	"equipmentnumber": "",
	"projecttype": "rcjx",
	"isspecialcondition": "",
	"specialcondition": ""
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit5.append(caseinfo.copy())


#作业预约删除
#用例信息
caseinfo['id'] = 4
caseinfo['name'] = '作业预约删除'
caseinfo['isactive'] = 1
num1 = work_appoint_id_plus1 + 1
url = "http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.8829315873575496&contentType=json&ajax=true&tid=1"%(work_appoint_id_plus1,num1)
data = [work_appoint_id_plus1]
caseinfo['url'] = url
caseinfo['data'] =data
testsuit5.append(caseinfo.copy())