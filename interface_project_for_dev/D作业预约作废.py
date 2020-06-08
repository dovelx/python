#a安全分析增删改查
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
work_appoint_id_l = sql_query_work_appointid+1
print("作业预约NEW ID:work_appoint_id_l",work_appoint_id_l)
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

    ####

#送交用例信息
casename = '作业预约送交'
#送交接口地址
url3='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfSend?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.30092471197648707&contentType=json&ajax=true&tid=1'%(work_appoint_id_l,work_appoint_id_l)
formdata2={
	"opinion": "申请审批",
	"nodeStr": "2000000009070",
	"2000000009070": "测试用户",
	"2000000009070_id": 1000
}
#请求送交接口
rs=requests.post(url3, json = formdata2, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']
if status == 3200:

    print("作业预约送交", status)
    #caseinfo['result'] = 1
else:
    print("作业预约送交", data)
#收集用例执行信息
#testsuit.append(caseinfo.copy())
#作业预约审批用例信息

casename = '作业预约审批'
# count =count+1
# caseid = count
# caseinfo['id'] = caseid
# caseinfo['name'] = casename
#审批接口地址
#url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(work_appoint_id_l,work_appoint_id_l)
url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(work_appoint_id_l)

#参数
formdata ={
	"opinion": "同意",
	"cC": "1000",
	"cCName": "测试用户",
	"nickName": "用户",
	"is_normal_finish": "true",
	"nodeStr": ""
}
#请求接口
rs=requests.post(url4, json = formdata, headers = headers,cookies=cookies)
#rs.encoding='utf-8'
#cc = str(rs.content, 'utf8')
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("作业预约审批", status)
    #caseinfo['result'] = 1

casename = '作业预约作废'
# count =count+1
# caseid = count
# caseinfo['id'] = caseid
# caseinfo['name'] = casename
#审批接口地址
#url4='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfFinish?parentEntityId=&parentFuncCode=&topEntityId=+&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.027850408425730055&contentType=json&ajax=true&tid=1'%(work_appoint_id_l)
url4 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/wfInvalid?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.9786549083065863&contentType=json&ajax=true&tid=1'%(work_appoint_id_l,work_appoint_id_l)
#参数
formdata = {
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
	"iscontainplayday": 0,
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
	"status": "approval",
	"constructionscheme": "",
	"wf_current_user": "1000",
	"wf_audit_state": "2",
	"wf_create_user": 1000,
	"wf_type": "2",
	"wf_instance": 2000000010669,
	"wf_current_nodeid": "2000000009070",
	"wf_audit_time": now,
	"worktype": "xkz",
	"worksite": "作业地点123",
	"equipmentnumber": "",
	"projecttype": "rcjx",
	"isspecialcondition": "",
	"specialcondition": ""
}
#请求接口
rs=requests.post(url4, json = formdata, headers = headers,cookies=cookies)
#rs.encoding='utf-8'
#cc = str(rs.content, 'utf8')
#返回值转码
data = rs.content.decode('utf-8')
#json格式化
data = json.loads(data)
#获取接口返回状态
status= data['status']

if status == 3200:

    print("作业预约作废", status)
    #caseinfo['result'] = 1
#DONE