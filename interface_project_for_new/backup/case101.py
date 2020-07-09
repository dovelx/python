from globalpkg.global_var import jsaid
from globalpkg.global_var import safeclarid
from backup.case100 import *
case = 'PC端安全'
# projectname = pro()
# host = host(projectname)
# print("url:",host)
# #times
# starttime = tool.starttime
# endtime = tool.endtime
# now = tool.now
#
# #作业预约名称
# name = tool.ran_name_with_str()
# print("作业预约名称：",name)
#用例信息变量定义
testsuit101 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''


#work_appoint_idx = work_appoint_idx-1
#安全分析及交底保存
work_appoint_idx = sql_query_work_appointid+1
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
caseinfo['id'] = 1001
caseinfo['name'] = '安全分析及交底保存'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuit101.append(caseinfo.copy())

#安全分析步骤添加接口用例信息
jsaidxx = jsaid+1
print ("安全分析步骤添加使用ID:",jsaidxx)

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
caseinfo['id'] = 1002
caseinfo['name'] = '安全分析步骤添加'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuit101.append(caseinfo.copy())

#安全分析步保存加接口用例信息

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
caseinfo['id'] = 1003
caseinfo['name'] = '安全分析保存'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuit101.append(caseinfo.copy())
#安全交底，环境影响大

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
caseinfo['id'] = 1004
caseinfo['name'] = '安全交底'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuit101.append(caseinfo.copy())
#安全送交接口用例信息

url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.9498759321537273&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {}
caseinfo['id'] = 1005
caseinfo['name'] = '安全送交'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuit101.append(caseinfo.copy())