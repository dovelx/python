import json
import requests
import random
import string
import datetime

#临时cookies
cookies={'JSESSIONID': '829D66F9731C78E762EE90156E732AE8IKEAdt'}
#作业预约作业任务名称随机数生成函数
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters+string.digits,num))
    return  salt
name = "Created_by_Python_"+ranstr(6)
print("作业预约名称",name)

#获取当前时间，为作业预约提供时间变量
now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=5)
now2 = now + datetime.timedelta(minutes=10)
fnow1 = now1.strftime("%Y-%m-%d %H:%M:%S")
fnow2 = now2.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")
#获取作业票id
from mobile import mydb
from globalpkg.global_var import logger

testdb = mydb.MyDB('./config/dbconfig.conf', 'CHANGQING')

sql_query_ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
sql_query_ts = 'select ts from hse_work_ticket order by ts desc limit 1'
sql_query_worktaskid = 'select worktaskid from hse_work_ticket ORDER BY worktaskid desc limit 1'
#sql_query_work_appoint_id ='SELECT work_appoint_id from hse_safety_task ORDER BY  work_appoint_id desc LIMIT 1'
sql_query_work_appointid ='SELECT work_appoint_id from hse_work_appoint ORDER BY  work_appoint_id desc LIMIT 1'
logger.info('正在更新步骤执行结果')
#testdb.execute_update(sql_update, data)
temp = testdb.select_one_record(sql_query_ticket)
#temp = temp.decode('utf-8')
workticketid = temp[0]
#作业票数据库当前ID
workticketid = workticketid[0]
print("workticketid",workticketid)

temp = testdb.select_one_record(sql_query_ts)
#print(temp)
ts = temp[0][0]
#print(ts)
ts = ts.decode('utf-8')
#TS ID
tsi = int(ts)
print("ts",ts)

temp = testdb.select_one_record(sql_query_worktaskid)
worktaskid = temp[0]
#worktaskid
worktaskid = worktaskid[0]
print("worktaskid",worktaskid)

temp = testdb.select_one_record(sql_query_work_appointid)
work_appoint_id = temp[0]
#worktaskid
work_appoint_id = work_appoint_id[0]
print("work_appoint_id",work_appoint_id)
testdb.close()
#暂时关闭登录

print(cookies)


#开始作业预约

#拼写预约URL

num = work_appoint_id+1
print("作业预约NEW ID:",num)
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.3707947936681053&contentType=json&ajax=true&tid=1'%(num,num)
#作业预约作业任务名称随机数生成函数
#print ("预约url\n",url2)

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
	"appointstarttime": fnow1,
	"appointendtime": fnow2,
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
#name = ranstr(7)
#print(name)
url = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.18905889749571658&contentType=json&ajax=true&tid=1'%(num,num)
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
	"work_appoint_id": num,
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
	"appointstarttime": fnow1,
	"appointendtime": fnow2,
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

# num1 = num + 1
# url = "http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.8829315873575496&contentType=json&ajax=true&tid=1"%(num,num1)
#
# data = [num]
#
# #请求作业预约删除接口
# rs=requests.post(url, json = data, headers = headers,cookies=cookies)
# #返回值转码
# data = rs.content.decode('utf-8')
# #json化
# data = json.loads(data)
# print(data)
# #获取接口返回状态
# sta= data['status']
# if sta == 3200:
#     print("作业删除成功", sta)
#
# else:
#
#     print(data)


#作业预约复制
#name = ranstr(7)
#num = num + 1
url = "http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/cardSave?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&dataId=%d&0.6280400811634435&contentType=json&ajax=true&tid=1"%(num,num)

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
	"work_appoint_id": num,
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
	"appointstarttime": fnow1,
	"appointendtime": fnow2,
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


#作业预约复制
rs=requests.post(url, json = data, headers = headers,cookies=cookies)
#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
print(data)
#获取接口返回状态
sta= data['status']
if sta == 3200:
    print("作业预约复制", sta)

else:
    print(data)
