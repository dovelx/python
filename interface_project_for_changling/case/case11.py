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

case = '长岭项目作业许可-PC-预约-添加，送交，审核'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

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
testsuit11.append(caseinfo.copy())
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
testsuit11.append(caseinfo.copy())

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
testsuit11.append(caseinfo.copy())