#手机端主流程 作业任务添加

from case.case101 import *
from case.case100 import name
from tools import minsert
from tools import msql
case = '手机全流程'
#用例信息变量定义
testsuitm102 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

insert = minsert.get_insert_code1()

name = name
#安全交底-现场作业人员签字
url = 'http://192.168.6.27:6030/m/hse_m/HSE_SAFETY_DISCLOSURE_M/jsasignAudit.json?safe_name=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&safe_content=%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%AE%89%E5%85%A8%E4%BA%A4%E5%BA%95&confirm_content=1%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E4%BD%9C%E4%B8%9A%E5%8C%BA%E5%9F%9F%E5%8F%8A%E5%91%A8%E8%BE%B9%E7%94%9F%E4%BA%A7%E4%BD%9C%E4%B8%9A%E6%83%85%E5%86%B5%0D%0A2%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%AE%89%E5%85%A8%E9%A3%8E%E9%99%A9%EF%BC%88JSA%EF%BC%89%0D%0A3%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%9A%84%E5%85%B7%E4%BD%93%E5%AE%89%E5%85%A8%E8%A6%81%E6%B1%82%EF%BC%88%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E4%B8%AD%E7%9A%84%E6%8E%A7%E5%88%B6%E6%8E%AA%E6%96%BD%EF%BC%89%0D%0A4%E3%80%81%E5%B7%B2%E5%AF%B9%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E7%8E%B0%E5%9C%BA%E5%AE%89%E5%85%A8%E6%8E%AA%E6%96%BD%E8%BF%9B%E8%A1%8C%E4%BA%86%E6%A3%80%E6%9F%A5%E7%A1%AE%E8%AE%A4%0D%0A5%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E6%9C%AC%E6%AC%A1%E4%BD%9C%E4%B8%9A%E6%B6%89%E5%8F%8A%E7%9A%84%E4%BD%9C%E4%B8%9A%E8%AE%B8%E5%8F%AF%E8%AF%81%E7%9A%84%E6%9C%89%E9%99%90%E6%9C%9F%E9%99%90%20%0D%0A6%E3%80%81%E5%B7%B2%E6%8E%8C%E6%8F%A1%E4%B8%AA%E4%BA%BA%E9%98%B2%E6%8A%A4%E7%94%A8%E5%85%B7%E6%AD%A3%E7%A1%AE%E4%BD%A9%E6%88%B4%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%0D%0A7%E3%80%81%E5%B7%B2%E6%B8%85%E6%A5%9A%E7%AA%81%E5%8F%91%E6%83%85%E5%86%B5%E4%B8%8B%E7%9A%84%E5%BA%94%E6%80%A5%E9%81%BF%E9%99%A9%E6%96%B9%E6%B3%95&additional_content=&workTicketid=%d&worktaskid=%d&workType=aqjd&actionCode=clarsign'
data = {
	"vo": {
		"df": 0,
		"workname": name,
		"woid": "",
		"territorialdeviceid": 2000000003454,
		"workunitname": "长庆石化分公司",
		"work_position_name": "制氢北区",
		"jsa_code": name,
		"worktickettype_query": "",
		"created_by_name": "",
		"tableName": "hse_work_task",
		"iscontractor": 0,
		"updated_by_name": "",
		"insert__": insert,
		"equipmentcode": "",
		"territorialunitid": "2000000003339",
		"jsaid": 2000000001875,
		"territorialdevicename": "制氢装置",
		"tenantid": 1,
		"projecttype": "rcjx",
		"territorialunitname": "运行一部",
		"workstatus": "draft",
		"equipmentnumber": "",
		"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
		"ver": 1,
		"created_dt": now,
		"planendtime": endtime,
		"reminder": "",
		"work_appoint_name": name,
		"reminderid": "",
		"worktickettype_name": "作业许可证",
		"applyunitname": "运行一部",
		"equipmentname": "",
		"dataStatus": 0,
		"work_appoint_id": 2000000001775,
		"wo_code": "",
		"standardmaintenance": "",
		"created_by": "",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"workunit": 1688712,
		"updated_dt": now,
		"contractorname": "",
		"updated_by": "",
		"planstarttime": starttime,
		"territorialunitcode": "CS8082020",
		"applyunitid": "2000000003339",
		"workcontent": "作业内容123",
		"worktaskid": ""
        #"safety_task_img": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"isicon\":false,\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000003652,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-06-17 17:22:42\",\"updated_by\":null,\"updated_dt\":\"2020-06-17 17:22:42\",\"df\":0,\"tenantid\":1,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OWAFqCrAAIKVnDfoY0466.png\"}]"
	}
}

caseinfo['id'] = 2001
caseinfo['name'] = '安全交底-现场作业人员签字'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
#testsuitm102.append(caseinfo.copy())
#作业任务添加m
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKAPPLY_MCQ_M/cardSave.json'
data = {
	"vo": {
		"df": 0,
		"workname": name,
		"woid": "",
		"territorialdeviceid": 2000000003454,
		"workunitname": "长庆石化分公司",
		"work_position_name": "制氢北区",
		"jsa_code": name,
		"worktickettype_query": "",
		"created_by_name": "",
		"tableName": "hse_work_task",
		"iscontractor": 0,
		"updated_by_name": "",
		"insert__": insert,
		"equipmentcode": "",
		"territorialunitid": "2000000003339",
		"jsaid": jsaidxx,
		"territorialdevicename": "制氢装置",
		"tenantid": 1,
		"projecttype": "rcjx",
		"territorialunitname": "运行一部",
		"workstatus": "draft",
		"equipmentnumber": "",
		"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
		"ver": 1,
		"created_dt": now,
		"planendtime": endtime,
		"reminder": "",
		"work_appoint_name": name,
		"reminderid": "",
		"worktickettype_name": "作业许可证",
		"applyunitname": "运行一部",
		"equipmentname": "",
		"dataStatus": 0,
		"work_appoint_id": 2000000001775,
		"wo_code": "",
		"standardmaintenance": "",
		"created_by": "",
		"work_position_id": 2000000002019,
		"site": "作业地点123",
		"workunit": 1688712,
		"updated_dt": now,
		"contractorname": "",
		"updated_by": "",
		"planstarttime": starttime,
		"territorialunitcode": "CS8082020",
		"applyunitid": "2000000003339",
		"workcontent": "作业内容123",
		"worktaskid": ""
#"safety_task_img": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"isicon\":false,\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000003652,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-06-17 17:22:42\",\"updated_by\":null,\"updated_dt\":\"2020-06-17 17:22:42\",\"df\":0,\"tenantid\":1,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OWAFqCrAAIKVnDfoY0466.png\"}]"
	}
}

caseinfo['id'] = 2001
caseinfo['name'] = '手机端作业任务添加m'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm102.append(caseinfo.copy())
#c
worktaskidxx = worktaskid+1
#匹配taskid
#worktaskidxx = msql.sql_query_worktaskid(name)
work_appoint_id = sql_query_work_appointid +1
print("worktaskidxx",worktaskidxx)
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKAPPLY_MCQ_M/submit.json?dataId=%d&ts='%(worktaskidxx)
data = {
	"vo": {
		"df": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": 0,
		"jsa_code": name,
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_task",
		"territorialunitid": 2000000003339,
		"territorialdevicename": "制氢装置",
		"territorialunitname": "运行一部",
		"equipmentnumber": "",
		"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
		"ver": 1,
		"planendtime": endtime,
		"work_appoint_name": "Created_by_Python_CEI3Vy",
		"constructionscheme": 0,
		"applyunitname": "运行一部",
		"equipmentname": "",
		"iswfnotreport": 0,
		"dataStatus": 0,
		"wo_code": "",
		"standardmaintenance": "",
		"created_by": 1000,
		"pause": 0,
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"workcontent": "作业内容123",
		"wf_audit_state": "0",
		"constructionscheme_attachshowlist": [],
		"plan_type": 3,
		"woid": "",
		"territorialdeviceid": 2000000003454,
		"work_position_name": "制氢北区",
		"worktickettype_query": "",
		"iscontractor": 0,
		"updated_by_name": "卢健",
		"equipmentcode": "",
		"jsaid": 2000000001875,
		"tenantid": 1,
		"projecttype": "rcjx",
		"workstatus": "draft",
		"created_dt": now,
		"reminder": "",
		"reminderid": "",
		"worktickettype_name": "",
		"work_appoint_id": work_appoint_idx,
		"work_position_id": 2000000002019,
		"wf_create_user": 1000,
		"site": "作业地点123",
		"updated_dt": now,
		"contractorname": "",
		"territorialunitcode": "CS8082020",
		"applyunitid": 2000000003339,
		"worktaskid": worktaskidxx
	}
}
data = {
	"vo": {
		"df": 0,
		"workname": name,
		"workunitname": "长庆石化分公司",
		"delaynum": 0,
		"jsa_code": name,
		"created_by_name": "卢健",
		"beendelaynum": 0,
		"tableName": "hse_work_task",
		"territorialunitid": 2000000003339,
		"territorialdevicename": "制氢装置",
		"territorialunitname": "运行一部",
		"equipmentnumber": "",
		"worktickettype": "xkz,dh,sx,gc,dz,gx,dt,dl,lsyd,shex,zylx11,jsj,zylx12,zylx13,zylx14,zylx15,zylx16,zylx17,qx",
		"ver": 1,
		"planendtime": endtime,
		"work_appoint_name": name,
		"constructionscheme": 0,
		"applyunitname": "运行一部",
		"equipmentname": "",
		"iswfnotreport": 0,
		"dataStatus": 0,
		"wo_code": "",
		"standardmaintenance": "",
		"created_by": 1000,
		"pause": 0,
		"workunit": 1688712,
		"updated_by": 1000,
		"planstarttime": starttime,
		"workcontent": "不知道",
		"wf_audit_state": "0",
		"constructionscheme_attachshowlist": [],
		"plan_type": 3,
		"woid": "",
		"territorialdeviceid": 2000000003454,
		"work_position_name": "制氢北区",
		"worktickettype_query": "",
		"iscontractor": 0,
		"updated_by_name": "卢健",
		"equipmentcode": "",
		"jsaid": safeclaridxx,
		"tenantid": 1,
		"projecttype": "dx",
		"workstatus": "draft",
		"created_dt": now,
		"reminder": "",
		"reminderid": "",
		"worktickettype_name": "",
		"work_appoint_id": work_appoint_idx,
		"work_position_id": 2000000002019,
		"wf_create_user": 1000,
		"site": "作业地点",
		"updated_dt": now,
		"contractorname": "",
		"territorialunitcode": "CS8082020",
		"applyunitid": 2000000003339,
		"worktaskid": worktaskidxx
	}
}
caseinfo['id'] = 2002
caseinfo['name'] = '手机端作业任务提交'
caseinfo['isactive'] = 1
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm102.append(caseinfo.copy())