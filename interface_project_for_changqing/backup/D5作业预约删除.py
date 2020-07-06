#作业预约增删改查
import json
import requests
from globalpkg.global_var import *
from tools.tool import *

#临时cookies
cookies={'JSESSIONID': '719FF49AB0E6CB255165409E8ACB4C9Fqoevbc'}
print(cookies)
name = ran_name_with_str()
print("作业预约名称",name)


#开始作业预约
#拼写预约URL
work_appoint_id_l = work_appoint_id+1
print("作业预约NEW ID:",work_appoint_id_l)
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.3707947936681053&contentType=json&ajax=true&tid=1'%(work_appoint_id_l,work_appoint_id_l)

#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': 'bd95a01c276341b89715228e81d0ca3f',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }
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
#请求作业预约保存接口
rs=requests.post(url2, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
#获取接口返回状态
sta= data['status']
if sta == 3200:
    print("作业预约成功", sta)
else:
    print("rulst",data)

#作业预约修改接口

url = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.18905889749571658&contentType=json&ajax=true&tid=1'%(work_appoint_id_l,work_appoint_id_l)
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
	"work_appoint_id": work_appoint_id_l,
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
#请求作业预约修改接口
rs=requests.post(url2, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
print(data)
#获取接口返回状态
sta= data['status']
if sta == 3200:
    print("作业预约修改成功", sta)
else:
	print("rulst", data)

num1 = work_appoint_id_l + 1
url = "http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.8829315873575496&contentType=json&ajax=true&tid=1"%(work_appoint_id_l,num1)

data = [work_appoint_id_l]

#请求作业预约删除接口
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
print(data)
#获取接口返回状态
sta= data['status']
if sta == 3200:
    print("作业删除成功", sta)

else:

    print(data)


