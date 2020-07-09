#from globalpkg.global_var import sql_query_jsa_step_harm_id
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
from globalpkg.global_var import workticketmbcdid
# from tools import getdata
#
case = '长岭项目作业许可-PC-盲板管理'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)


#用例信息变量定义
testsuit84 = []
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
caseinfo['name'] = '盲板管理-添加'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'post'
caseinfo['exresult'] = ""
editId = jsaid +40
topEntityId = jsaid+40
#caseinfo['exresult'] =  {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_TICKET_MBCD/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_TICKET_MBCD&0.6211012111566583&contentType=json&ajax=true&tid=2000000001003
url = "http://192.168.6.156/hse/HSE_TICKET_MBCD/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_TICKET_MBCD&0.6211012111566583&contentType=json&ajax=true&tid=2000000001003"
caseinfo['url'] = url
data = {
	"tableName": "hse_ticket_mbcd",

	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": "0",
	"tenantid": 2000000001003,
	"ts": "",
	"blind_type": "flat",
	"workstatus": "jia",
	"normalproductionstatus": "chou",
	"commenceperiodstatus": "jia",
	"downmaintenancestatus": "jia",
	"mbcdnumber": topEntityId,
	"territorialunitid": 2000000005066,
	"territorialunitname": "炼油一部",
	"territorialunitcode": "000000010300",
	"device": "装置名称",
	"worksite": "安装/拆除位置",
	"blindplate_material": "盲板材质",
	"pressure": "工作压力",
	"temperature": "工作温度",
	"medium": "工作介质",
	"pidnumber": "图号",
    "blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000012000,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-03 14:33:14\",\"updated_by\":null,\"updated_dt\":\"2020-07-03 14:33:14\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SuABJCoAAIKVnDfoY0618.png\"}]",
	#"blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000012450,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-01 10:57:46\",\"updated_by\":null,\"updated_dt\":\"2020-07-01 10:57:46\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6uAMYvFAAIKVnDfoY0222.png\"}]",
     #"blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"isicon\":false,\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000003652,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-06-17 17:22:42\",\"updated_by\":null,\"updated_dt\":\"2020-06-17 17:22:42\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OWAFqCrAAIKVnDfoY0466.png\"}]",
	"design_pressure": "1000",
	"dn": "20"
}
caseinfo['data'] =data
testsuit84.append(caseinfo.copy())


caseinfo['id'] = 2
caseinfo['name'] = '盲板管理-修改'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'post'
caseinfo['exresult'] = ""
editId = jsaid +40
topEntityId = jsaid+40
#caseinfo['exresult'] =  {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_TICKET_MBCD/cardSave?parentEntityId=&parentFuncCode=&topEntityId=2000000000020&topFuncCode=HSE_TICKET_MBCD&dataId=2000000000020&0.8579503023106407&contentType=json&ajax=true&tid=2000000001003
url = "http://192.168.6.156/hse/HSE_TICKET_MBCD/cardSave?parentEntityId=&parentFuncCode=&topEntityId=2000000000020&topFuncCode=HSE_TICKET_MBCD&dataId=%d&0.8579503023106407&contentType=json&ajax=true&tid=2000000001003"%(workticketmbcdid)
caseinfo['url'] = url
data = {
	"tableName": "hse_ticket_mbcd",

	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": "0",
	"tenantid": 2000000001003,
	"ts": "",
	"blind_type": "flat",
	"workstatus": "jia",
	"normalproductionstatus": "chou",
	"commenceperiodstatus": "jia",
	"downmaintenancestatus": "jia",
	"mbcdnumber": topEntityId,
	"territorialunitid": 2000000005066,
	"territorialunitname": "炼油一部",
	"territorialunitcode": "000000010300",
	"device": "装置名称",
	"worksite": "安装/拆除位置",
	"blindplate_material": "盲板材质",
	"pressure": "工作压力",
	"temperature": "工作温度",
	"medium": "工作介质",
	"pidnumber": "图号",
    "blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000012000,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-03 14:33:14\",\"updated_by\":null,\"updated_dt\":\"2020-07-03 14:33:14\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SuABJCoAAIKVnDfoY0618.png\"}]",
	#"blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000012450,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-01 10:57:46\",\"updated_by\":null,\"updated_dt\":\"2020-07-01 10:57:46\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6uAMYvFAAIKVnDfoY0222.png\"}]",
     #"blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"isicon\":false,\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000003652,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-06-17 17:22:42\",\"updated_by\":null,\"updated_dt\":\"2020-06-17 17:22:42\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OWAFqCrAAIKVnDfoY0466.png\"}]",
	"design_pressure": "1000",
	"dn": "20"
}
data = {
	"tableName": "hse_ticket_mbcd",
	"commenceperiodstatus": "jia",
	"created_by_name_nick": "cl",
	"downmaintenancestatus": "jia",
	"created_by_name": "长岭石化管理员",
	"normalproductionstatus": "chou",
	"dataStatus": 0,
	"ver": 1,
	"created_by": 2000000012062,
	"created_dt": now,
	"updated_by": 2000000012062,
	"updated_dt": now,
	"df": "0",
	"tenantid": 2000000001003,
	"ts": "",
	"workticketmbcdid": workticketmbcdid,
	"mbcdnumber": "modify",
	"territorialunitid": 2000000005066,
	"territorialunitcode": "000000010300",
	"territorialunitname": "炼油一部",
	"device": "装置名称",
	"worksite": "安装/拆除位置",
	"medium": "工作介质",
	"temperature": "工作温度工作温度",
	"pressure": "工作压力",
	"blindplate_material": "盲板材质",
	"pidnumber": "图号",
"blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000012000,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-03 14:33:14\",\"updated_by\":null,\"updated_dt\":\"2020-07-03 14:33:14\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SuABJCoAAIKVnDfoY0618.png\"}]",
	#"blindattaches": "[ {\n  \"dfs_file_name\" : \"微信图片_20200617160345.jpg\",\n  \"dfs_file_group_name\" : null,\n  \"dfs_file_key\" : \"M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\n  \"dfs_file_size\" : 78172,\n  \"dfs_preview_url\" : \"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\n  \"dfs_thumbnail_url\" : \"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6uAMYvFAAIKVnDfoY0222.png\"\n} ]",
	"design_pressure": "1000",
	"dn": "20",
	"blind_type": "flat",
	"workstatus": "jia"
}
caseinfo['data'] =data
testsuit84.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = '盲板管理-删除'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'post'
caseinfo['exresult'] = ""
editId = jsaid +40
topEntityId = jsaid+40
workticketmbcdid = workticketmbcdid +1
#caseinfo['exresult'] =  {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_TICKET_MBCD/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=2000000000020&topFuncCode=HSE_TICKET_MBCD&dataId=2000000000020&0.9236103189336689&contentType=json&ajax=true&tid=2000000001003
url = "http://192.168.6.156/hse/HSE_TICKET_MBCD/listDeleteBatch?parentEntityId=&parentFuncCode=&topEntityId=2000000000020&topFuncCode=HSE_TICKET_MBCD&dataId=%d&0.9236103189336689&contentType=json&ajax=true&tid=2000000001003"%(workticketmbcdid)
caseinfo['url'] = url
data = {
	"tableName": "hse_ticket_mbcd",

	"dataStatus": 0,
	"ver": 1,
	"created_by": "",
	"created_dt": now,
	"updated_by": "",
	"updated_dt": now,
	"df": "0",
	"tenantid": 2000000001003,
	"ts": "",
	"blind_type": "flat",
	"workstatus": "jia",
	"normalproductionstatus": "chou",
	"commenceperiodstatus": "jia",
	"downmaintenancestatus": "jia",
	"mbcdnumber": topEntityId,
	"territorialunitid": 2000000005066,
	"territorialunitname": "炼油一部",
	"territorialunitcode": "000000010300",
	"device": "装置名称",
	"worksite": "安装/拆除位置",
	"blindplate_material": "盲板材质",
	"pressure": "工作压力",
	"temperature": "工作温度",
	"medium": "工作介质",
	"pidnumber": "图号",
    "blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000012000,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-03 14:33:14\",\"updated_by\":null,\"updated_dt\":\"2020-07-03 14:33:14\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SqAGcF2AAExXFSqfEE473.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.156:8888//group1//M00/00/2C/wKgGnF7-0SuABJCoAAIKVnDfoY0618.png\"}]",
	#"blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000012450,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-01 10:57:46\",\"updated_by\":null,\"updated_dt\":\"2020-07-01 10:57:46\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6qANYSfAAExXFSqfEE541.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF77-6uAMYvFAAIKVnDfoY0222.png\"}]",
     #"blindattaches": "[{\"dfs_file_name\":\"微信图片_20200617160345.jpg\",\"isicon\":false,\"tableName\":\"sy_attach_dfs\",\"dfs_id\":2000000003652,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-06-17 17:22:42\",\"updated_by\":null,\"updated_dt\":\"2020-06-17 17:22:42\",\"df\":0,\"tenantid\":2000000001003,\"ts\":null,\"dfs_file_group_name\":\"group1\",\"dfs_file_key\":\"M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_file_size\":78172,\"dfs_preview_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OKAaPXcAAExXFSqfEE896.jpg\",\"dfs_thumbnail_url\":\"http://192.168.6.26:8888//group1//M00/01/17/wKgGGl7p4OWAFqCrAAIKVnDfoY0466.png\"}]",
	"design_pressure": "1000",
	"dn": "20"
}
data = [workticketmbcdid]
caseinfo['data'] =data
testsuit84.append(caseinfo.copy())