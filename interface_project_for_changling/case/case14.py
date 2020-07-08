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

case = '长岭项目作业许可-PC-预约-安全-申请-作业票提交'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)

#用例信息变量定义
testsuit14 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = 'post'
caseinfo['isactive'] = ''

count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业预约'
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
testsuit14.append(caseinfo.copy())


#送交用例信息
#getdata.get_work_appoint_id(cookies=c)
#work_appoint_id_plus1=  work_appoint_id+1
work_appoint_id_plus1 = sql_query_work_appointid+1
#作业预约创建使用ID
yuyueid = work_appoint_id_plus1
caseinfo['id'] = 2
caseinfo['name'] = '作业预约送交'
#送交接口地址

#http://192.168.6.156/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=2000000000431&topFuncCode=HSE_WORK_APPOINT&dataId=2000000000431&0.06389849673294723&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.06389849673294723&contentType=json&ajax=true&tid=2000000001003'%(work_appoint_id_plus1,work_appoint_id_plus1)
caseinfo['url'] = url
formdata2={
	"opinion": "申请审批",
	"nodeStr": "2000000013477",
	"2000000013477": "长岭石化管理员",
	"2000000013477_id": 2000000012062
}
caseinfo['data'] =formdata2
print(caseinfo['id'] )
testsuit14.append(caseinfo.copy())

#作业预约审批用例信息
caseinfo['id'] = 3
caseinfo['name'] = '作业预约审批'
#审批接口地址
#http://192.168.6.156/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=2000000000430&topFuncCode=HSE_WORK_APPOINT&dataId=2000000000430&0.7556673624348265&contentType=json&ajax=true&tid=2000000001003
url4='http://192.168.6.156/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.7556673624348265&contentType=json&ajax=true&tid=2000000001003'%(work_appoint_id_plus1,work_appoint_id_plus1)
caseinfo['url'] = url4
#参数
data = {
	"opinion": "同意",
	"cC": "2000000012062",
	"cCName": "长岭石化管理员",
	"nickName": "cl",
	"is_normal_finish": "true",
	"nodeStr": ""
}
caseinfo['data'] =data
testsuit14.append(caseinfo.copy())

#安全分析及交底保存
casename = '安全分析及交底保存'
caseinfo['id'] = 4
caseinfo['name'] = casename
#http://192.168.6.156/hse/HSE_SAFETY_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK&0.666941462228346&contentType=json&ajax=true&tid=2000000001003
urlfenxi ='http://192.168.6.156/hse/HSE_SAFETY_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_SAFETY_TASK&0.666941462228346&contentType=json&ajax=true&tid=2000000001003'

data = {
	"tableName": "hse_safety_task",
	"wf_create_user": 2000000012062,
	"iscontractor": "0",
	"workstatus": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 2000000012062,
	"created_dt": now,
	"updated_by": 2000000012062,
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000001003,
	"ts": "",
	"analyze_type": "jsa",
	"projecttype": "rcjx",
	"workname": name,
	"territorialunitid": 2000000005066,
	"territorialunitname": "炼油一部",
	"territorialdeviceid": 2000000005066,
	"territorialdevicename": "炼油一部",
	"territorialdevicecode": "000000010300",
	"work_position_id": 2000000001891,
	"work_position_name": "炼油一部",
	"site": "作业地点",
	"planstarttime": starttime,
	"planendtime": endtime,
	"workcontent": "作业内容",
	"worktickettype_name": "用火作业,受限空间,盲板抽堵,高处作业,起重作业,临时用电,动土作业",
	"worktickettype": "dh,sx,mbcd,gc,dz,lsyd,dt"
}
caseinfo['url'] = urlfenxi
caseinfo['data'] = data
testsuit14.append(caseinfo.copy())

#jsaidxx = work_appoint_id-33
jsaidx = jsaid+1
print ("安全分析列表使用ID:",jsaidx)

#安全分析步骤添加接口用例信息
casename = '安全分析步骤添加'
count =count+1
caseid = count
caseinfo['id'] = 5
caseinfo['name'] = casename
topEntityId = jsaidx +40
url ='http://192.168.6.156/hse/HSE_SAFETY_ANALYSIS_STEP/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK&0.7124130928687566&contentType=json&ajax=true&tid=2000000001003'%(jsaidx,topEntityId)
data = {
	"tableName": "hse_safety_analysis_step",
	"qualify_level": "no_qualify",
	"jsaid": jsaidx,
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": "2020-06-17 11:39:49",
	"updated_by": "",
	"updated_dt": "2020-06-17 11:39:49",
	"df": 0,
	"tenantid": 2000000001003,
	"ts": "",
	"evaluate_type": "",
	"worktickettype_name": "一般作业",
	"worktickettype": "xkz",
	"worknumber": "10086",
	"step_name": "步骤活动"
}
caseinfo['url'] = url
caseinfo['data'] =data
#testsuit14.append(caseinfo.copy())

#安全分析步保存加接口用例信息

casename = '安全分析保存'
count =count+1
caseid = count
caseinfo['id'] = 6
caseinfo['name'] = casename
print("topEntityId（安全分析步骤添加）",topEntityId)
print("jsaidx（安全分析步骤添加）",jsaidx)
#http://192.168.6.156/hse/HSE_SAFETY_ANALYSIS/cardSave?parentEntityId=2000000000876&parentFuncCode=HSE_SAFETY_TASK&topEntityId=2000000000876&topFuncCode=HSE_SAFETY_TASK&dataId=2000000000836&0.6015172226353962&contentType=json&ajax=true&tid=2000000001003
url=  'http://192.168.6.156/hse/HSE_SAFETY_ANALYSIS/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_TASK&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK&dataId=%d&0.6015172226353962&contentType=json&ajax=true&tid=2000000001003'%(topEntityId,topEntityId,jsaidx)
#url = 'http://192.168.6.156/hse/HSE_SAFETY_ANALYSIS/cardSave?parentEntityId=2000000000876&parentFuncCode=HSE_SAFETY_TASK&topEntityId=2000000000876&topFuncCode=HSE_SAFETY_TASK&dataId=2000000000836&0.6015172226353962&contentType=json&ajax=true&tid=2000000001003'

data = {
	"tableName": "hse_safety_analysis",

	"dataStatus": 0,
	"ver": 1,
	"created_by": 2000000012062,
	"created_dt": now,
	"updated_by": 2000000012062,
	"updated_dt": now,
	"df": 0,
	"tenantid": 2000000001003,
	"ts": "",
	"jsaid": jsaidx,
	"jsa_templete_name": "炼油一部安全分析数据模板",
	"jsa_templete_id": 2000000000140,
	"temp_type": "",
	"jsa_monitor_userid": "",
	"jsa_monitor_name": "测试用户",
	"jsa_menber_userids": "",
	"jsa_menber_username": "测试用户",
	"analyze_time": now,
	"worktickettype": "",
	"equip_stuff": "",
	"worktaskid": topEntityId,
	"workstatus": "",
	"worktype": "jsa",
	"revampandadvide": "",
	"inspection_name": "",
	"work_position_id": 2000000001891,
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

	"sourcejsaid": "",
	"remainsrisk_level": "",
	"risk_level": ""
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit14.append(caseinfo.copy())

#安全送交接口用例信息

casename = '安全送交'
count =count+1
caseid = count
caseinfo['id'] = 8
caseinfo['name'] = casename
#http://192.168.6.156/hse/HSE_SAFETY_TASK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=2000000000886&topFuncCode=HSE_SAFETY_TASK&dataId=2000000000886&0.6665362277729903&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_SAFETY_TASK/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK&dataId=%d&0.6665362277729903&contentType=json&ajax=true&tid=2000000001003'%(topEntityId,topEntityId)
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuit14.append(caseinfo.copy())
