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

case = '作业预约全票'
projectname = pro()
host = host(projectname)
print("url:",host)
#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime
#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)
#用例信息变量定义
testsuit11 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

#作业预约创建使用ID
work_appoint_idx = sql_query_work_appointid
#work_appoint_id_plus1 = work_appoint_id_plus1
count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业预约全票'
caseinfo['isactive'] = 1
url = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.621597217691122&contentType=json&ajax=true&tid=1'%(work_appoint_idx,work_appoint_idx)
data = {
	"tableName": "hse_work_appoint",
	"task_worktype_code": "GCN",
	"": "",
	"equt_name": "",
	"territorialdeviceid": 2000000003454,
	"worktaskid_no": 0,
	"created_by_name_nick": "用户",
	"isreport": "0",
	"specialenvironment": "ALLNOT",
	"cywlqfyxzz": "1",
	"created_by_name": "测试用户",
	"worklevel_dh": "mcq_dh_workLevel01",
	"sourcecode": "",
	"updated_by_name": "测试用户",
	"iscontainplayday": "",
	"worktype_name": "作业许可证,动火作业,受限空间,高处作业,吊装作业,管线/设备打开,挖掘作业,断路作业,临时用电,射线作业,承包商作业,脚手架作业,非计划性维修工作,交叉作业,屏蔽报警、解除连锁和安全应急设备,偏离规则/程序要求的工作,没有安全程序可遵循的工作,其他,清洗作业",
	"sourcefunc": "",
	"equipmentcode": "",
	"territorialdevicename": "制氢装置",
	"sourcetype": "",
	"worktypename": "作业许可证,动火作业,受限空间,高处作业,吊装作业,管线/设备打开,挖掘作业,断路作业,临时用电,射线作业,承包商作业,脚手架作业,非计划性维修工作,交叉作业,屏蔽报警、解除连锁和安全应急设备,偏离规则/程序要求的工作,没有安全程序可遵循的工作,其他,清洗作业",
	"sourceid": "",
	"worklevel_gx": "",
	"serviceplanid": "",
	"task_worktype_name": "储罐浮舱内",
	"standardmaintenance": "",
	"worklevel_sx": "mcq_sx_workLevel01",
	"material_medium": "物料介质",
	"risksmeasures": "重点防控的风险",
	"issjtssxzy": "1",
	"isupgradedh": "1",
	"isdzdh": "1",
	"worklevel_gc": "mcq_gc_workLevel01",
	"funccode": "HSE_WORK_APPOINT",
	"persistent_type": "newoperation",
	"territorialunitcode": "CS8082020",
	"worklevel_dz": "mcq_dz_workLevel01",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"work_appoint_id": work_appoint_idx,
	"code": "",
	"iscontractor": "0",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"workunitname_no": "",
	"workcontent": "作业内容",
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
	"worktype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
	"worksite": "作业地点",
	"equipmentnumber": "",
	"projecttype": "rcjx",
	"isspecialcondition": "1",
	"specialcondition": "好艰苦"
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit11.append(caseinfo.copy())

#送交用例信息
caseinfo['id'] = 2
caseinfo['name'] = '作业预约送交'
#送交接口地址
url3=  'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(work_appoint_idx,work_appoint_idx)
#url3 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=2000000001995&topFuncCode=HSE_WORK_APPOINT&dataId=2000000001995&0.7895122255202975&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url3
data = {
	"opinion": "申请审批",
	"nodeStr": "2000000009070",
	"2000000009070": "测试用户",
	"2000000009070_id": 1000
}
caseinfo['data'] = data
print(caseinfo['id'] )
testsuit11.append(caseinfo.copy())

#作业预约审批用例信息
caseinfo['id'] = 3
caseinfo['name'] = '作业预约审批'
#审批接口地址
url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(work_appoint_idx)
caseinfo['url'] = url4
#参数
formdata ={
	"opinion": "同意",
	"cC": "1000",
	"cCName": "测试用户",
	"nickName": "用户",
	"is_normal_finish": "true",
	"nodeStr": ""
}
caseinfo['data'] =formdata
testsuit11.append(caseinfo.copy())

#安全分析及交底保存
casename = '安全分析及交底保存'
caseinfo['id'] = 4
caseinfo['name'] = casename
urlfenxi ='http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK_RISK&0.6529845051499572&contentType=json&ajax=true&tid=1'
formdatafenxi ={
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
	"projecttype": "rcjx",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",

	"work_appoint_id": work_appoint_idx,
	"workcontent": "作业内容123",
	"workname": name,
	"worktickettype": "xkz,dh",
	"worktickettype_name": "作业许可证,动火作业",
	"workunitname": "长庆石化分公司",
	"workunit": 1688712,
	"planstarttime":starttime,
	"planendtime": endtime,
	"site": "作业地点123",
	"equipmentname": "",
	"work_position_name": "制氢北区",
	"work_position_id": 2000000002019,
	"equipmentnumber": "",
	"equipmentcode": "",
	"constructionscheme": "",
	"standardmaintenance": ""
}
caseinfo['url'] = urlfenxi
caseinfo['data'] =formdatafenxi
testsuit11.append(caseinfo.copy())

#安全分析步骤添加接口用例信息
jsaidxx = jsaid+1
print ("安全分析步骤添加使用ID:",jsaidxx)

casename = '安全分析步骤添加'
caseinfo['id'] = 5
caseinfo['name'] = casename
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
caseinfo['url'] = url
caseinfo['data'] =data
testsuit11.append(caseinfo.copy())

#安全分析步保存加接口用例信息
casename = '安全分析保存'
caseinfo['id'] = 6
caseinfo['name'] = casename
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
caseinfo['url'] = url
caseinfo['data'] =data
testsuit11.append(caseinfo.copy())

#安全交底，环境影响大
casename = '安全交底'
caseinfo['id'] = 7
caseinfo['name'] = casename
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
caseinfo['url'] = url
caseinfo['data'] =data
testsuit11.append(caseinfo.copy())

#安全送交接口用例信息

casename = '安全送交'
caseinfo['id'] = 8
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK_RISK&dataId=%d&0.9498759321537273&contentType=json&ajax=true&tid=1'%(jsaidxx,jsaidxx)
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit11.append(caseinfo.copy())

#作业任务添加接口用例信息
casename = '作业任务添加'
caseinfo['id'] = 9
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK_MCQ&0.9651365781343351&contentType=json&ajax=true&tid=1'
data = {
	"tableName": "hse_work_task",
	"iscontractor": "0",
	"isupgrade": "0",
	"work_appoint_name": name,
	"territorialunitid": "2000000003339",
	"applyunitname": "运行一部",
	"task_pause": "0",
	"territorialunitname": "运行一部",
	"territorialunitcode": "CS8082020",
	"applyunitid": "2000000003339",
	"workstatus": "draft",
	"autorisklevel": 1,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"projecttype": "rcjx",
	"isrecord": "",
	"eq_position": "",
	"territorialdeviceid": 2000000003454,
	"territorialdevicename": "制氢装置",
	"jsaid": 2000000002030,
	"work_appoint_id": work_appoint_idx,
	"jsa_code": name,
	"site": "作业地点123",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"work_position_id": 2000000002019,
	"work_position_name": "制氢北区",
	"workcontent": "作业内容123",
	"planstarttime": starttime,
	"planendtime": endtime,
	"standardmaintenance_name": "",
	"constructionscheme": 1,
	"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
	"worktickettype_name": "作业许可证,动火作业,受限空间,高处作业,吊装作业,管线/设备打开,挖掘作业,断路作业,临时用电,射线作业,承包商作业,脚手架作业,非计划性维修工作,交叉作业,屏蔽报警、解除连锁和安全应急设备,偏离规则/程序要求的工作,没有安全程序可遵循的工作,其他,清洗作业",
	"standardmaintenance": "",
	"equipmentname": "",
	"equipmentnumber": "",
	"equipmentcode": "",
	"workname": name
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit11.append(caseinfo.copy())



#作业任务提交接口用例信息
worktaskidxx = worktaskid+1
print("作业任务提交-worktaskidxx:",worktaskidxx)

casename = '作业任务提交'
count =count+1
caseid = count
caseinfo['id'] = 10
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.412998005925274&contentType=json&ajax=true&tid=1'%(worktaskidxx,worktaskidxx)
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/hse_work_task_submit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK_MCQ&dataId=%d&0.9505796541855793&contentType=json&ajax=true&tid=1'%(worktaskidxx,worktaskidxx)

data = {
	"tableName": "hse_work_task",
	"task_worktype_code": "",
	"hasrescueplan": "",
	"territorialdeviceid": 2000000003454,
	"drawshow": "",
	"cywlqfyxzz": "",
	"autorisklevel": 1,
	"worktools": "",
	"othercontent": "",
	"equipmentcode": "",
	"ishasworker": "",
	"territorialdevicename": "制氢装置",
	"hasdrawpaper": "",
	"hassafetyplan": "",
	"worker": "",
	"card_code": "",
	"reminder": "",
	"constructionscheme": 1,
	"reminderid": "",
	"worktickettype_name": "作业许可证,动火作业,受限空间,高处作业,吊装作业,管线/设备打开,挖掘作业,断路作业,临时用电,射线作业,承包商作业,脚手架作业,非计划性维修工作,交叉作业,屏蔽报警、解除连锁和安全应急设备,偏离规则/程序要求的工作,没有安全程序可遵循的工作,其他,清洗作业",
	"task_worktype_name": "",
	"standardmaintenance": "",
	"attaches": "",
	"material_medium": "",
	"risksmeasures": "",
	"isrecord": "",
	"persistent_type": "",
	"flights": "",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 1000,
	"created_dt": now,
	"updated_by": 1000,
	"updated_dt": now,
	"df": 0,
	"tenantid": 1,
	"ts": "",
	"worktaskid": worktaskidxx,
	"workname": name,
	"work_position_name": "制氢北区",
	"work_appoint_name": name,
	"actualstarttime": "",
	"actualendtime": "",
	"isgas_detection": "",
	"delayreason": "",
	"cancelreason": "",
	"pause": 0,
	"isupgrade": "0",
	"sourcetaskid": "",
	"nlglnumber": "",
	"isreport": "",
	"iswfnotreport": 0,
	"gas_standard_type": "",
	"parentid": "",
	"lsydticketid": "",
	"dqyzticketid": "",
	"dqezticketid": "",
	"task_pause": "0",
	"device_id": "",
	"territorialunitid": 2000000003339,
	"territorialunitname": "运行一部",
	"site": "作业地点123",
	"work_property": "bespeak",
	"equipmentnumber": "",
	"workunit": 1688712,
	"workunitname": "长庆石化分公司",
	"projecttype": "rcjx",
	"iscontractor": "0",
	"planstarttime": starttime,
	"planendtime": endtime,
	"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
	"workstatus": "draft",
	"applyunitid": 2000000003339,
	"applyunitname": "运行一部",
	"created_by_name": "测试用户",
	"updated_by_name": "测试用户",
	"workcontent": "作业内容123",
	"woid": "",
	"wo_code": "",
	"territorialunitcode": "CS8082020",
	"equt_position": "",
	"position_name": "",
	"equipmentname": "",
	"safeclar": "",
	"safecode": "",
	"work_position_id": 2000000002019,
	"jsa_code": name,
	"jsaid": 2000000002030,
	"work_appoint_id": work_appoint_idx,
	"wf_current_nodeid": "",
	"wf_audit_time": "",
	"task_risklevel": "",
	"task_closereason": "",
	"task_closetype": "",
	"wf_current_user": "",
	"wf_audit_state": "0",
	"wf_create_user": 1000,
	"wf_instance": "",
	"wf_type": "",
	"delaynum": 0,
	"beendelaynum": 0,
	"jobstatus": "",
	"weekplanid": "",
	"plan_type": 3,
	"gasdetecttype": "",
	"close_type": "",
	"closereason": "",
	"jsa_code2": "",
	"jsaid2": "",
	"isproprietor": "",
	"planendtime_org": "",
	"specialenvironment": "",
	"gas_aging": "",
	"safetyanalysisid": "",
	"safetyanalysiscode": "",
	"isspecialcondition": "",
	"specialcondition": "",
	"task_risklevel_org": "",
	"eq_position": ""
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit11.append(caseinfo.copy())