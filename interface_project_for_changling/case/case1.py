
from case.case33 import  *

case = '长岭项目作业许可-安全分析'



#用例信息变量定义
testsuit1 = []
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
	"work_position_name": "炼油北区",
	"site": "作业地点",
	"planstarttime": starttime,
	"planendtime": endtime,
	"workcontent": "作业内容",
	"worktickettype_name": "用火作业,受限空间,盲板抽堵,高处作业,起重作业,临时用电,动土作业",
	"worktickettype": "dh,sx,mbcd,gc,dz,lsyd,dt"
}
caseinfo['url'] = urlfenxi
caseinfo['data'] = data
testsuit1.append(caseinfo.copy())



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
#http://192.168.6.156/hse/HSE_SAFETY_ANALYSIS_STEP/cardSave?parentEntityId=2000000000830&parentFuncCode=HSE_SAFETY_ANALYSIS&topEntityId=2000000000870&topFuncCode=HSE_SAFETY_TASK&0.7124130928687566&contentType=json&ajax=true&tid=2000000001003
url ='http://192.168.6.156/hse/HSE_SAFETY_ANALYSIS_STEP/cardSave?parentEntityId=%d&parentFuncCode=HSE_SAFETY_ANALYSIS&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK&0.7124130928687566&contentType=json&ajax=true&tid=2000000001003'%(jsaidx,topEntityId)
#url = 'http://192.168.6.156/hse/HSE_SAFETY_ANALYSIS_STEP/cardSave?parentEntityId=2000000000830&parentFuncCode=HSE_SAFETY_ANALYSIS&topEntityId=2000000000870&topFuncCode=HSE_SAFETY_TASK&0.7124130928687566&contentType=json&ajax=true&tid=2000000001003'

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
#testsuit1.append(caseinfo.copy())

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
testsuit1.append(caseinfo.copy())


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
testsuit1.append(caseinfo.copy())

