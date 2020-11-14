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
testsuit = []
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
caseinfo['name'] = '作业任务添加'
caseinfo['isactive'] = 1
#拼写预约URL
#http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK&0.5097455282880827&contentType=json&ajax=true&tid=2000000000453
url = 'http://v3-test-linux-hse.hd-cloud.com/hse/HSE_WORK_TASK/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK&0.5097455282880827&contentType=json&ajax=true&tid=2000000000453'
caseinfo['url'] = url
#全票数据
data = {
	"tableName": "hse_work_task",
	"ischoisedevice": 1,
	"work_appoint_name": "",
	"applyunitname": "现场总管演示单位",
	"territorialunitid": 2000000001623,
	"territorialunitname": "现场总管演示单位",
	"applyunitid": 2000000001623,
	"jsa_code": "",
	"workstatus": "draft",
	"autorisklevel": 1,
	"status": "draft",
	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": "2020-11-14 13:49:06",
	"updated_by": "",
	"updated_dt": "2020-11-14 13:49:06",
	"df": 0,
	"tenantid": 2000000000453,
	"ts": "",
	"projecttype": "",
	"isspecialcondition": "",
	"work_property": "",
	"iscontractor": "0",
	"gas_standard_type": "hasoxygen",
	"eq_position": "",
	"work_position_id": 2000000000604,
	"work_position_name": "位置",
	"device_id": 2000000000160,
	"device_code": "ZZ20200002",
	"site": "测试地点",
	"workunit": 2000000001623,
	"workunitname": "现场总管演示单位",
	"workunitname_no": "",
	"workname": name,
	"workcontent": "内容",
	"worktickettype_name": "动火作业",
	"worktickettype": "dh",
	"planstarttime": "2020-11-16 11:49:36",
	"planendtime": "2020-11-16 16:49:42"
}
caseinfo['data'] =data
testsuit.append(caseinfo.copy())


