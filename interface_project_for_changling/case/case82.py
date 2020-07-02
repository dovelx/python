#from globalpkg.global_var import sql_query_jsa_step_harm_id
from tools import tool
# from globalpkg.global_var import tsi
# from globalpkg.global_var import workticketid
# from globalpkg.global_var import worktaskid
# from globalpkg.global_var import worktaskid1
# from globalpkg.global_var import jsaid
# from globalpkg.global_var import safeclarid
# from globalpkg.global_var import sql_query_work_appointid
# from globalpkg.global_var import sql_query_jsastepid
# from globalpkg.global_var import sql_query_jsa_step_measure_id
# from tools import getdata
#
case = '长岭项目作业许可-PC-各列表获取'
#
# #times
# starttime = tool.starttime
# endtime = tool.endtime
# now = tool.now
#
#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)


#用例信息变量定义
testsuit82 = []
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
caseinfo['name'] = '列表获取-安全分析模板'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ""
#caseinfo['exresult'] =  {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_JSA_TEMPLETE/getMetaData?0.21735623021556605&contentType=json&ajax=true&tid=2000000001003
url = "http://192.168.6.156/hse/HSE_JSA_TEMPLETE/getMetaData?0.21735623021556605&contentType=json&ajax=true&tid=2000000001003"
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = '列表获取-安全分析及交底'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] = {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_SAFETY_TASK/getMetaData?0.16264440079676246&contentType=json&ajax=true&tid=2000000001003

url = 'http://192.168.6.156/hse/HSE_SAFETY_TASK/getMetaData?0.16264440079676246&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = '列表获取-作业任务'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] = {"条件":[{"模式":"长岭石化管理员", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TASK/getMetaData?0.5747339420608581&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TASK/getMetaData?0.5747339420608581&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 4
caseinfo['name'] = '列表获取-任务台账'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] = {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TASK_ACCOUNT/getMetaData?0.5907983814673263&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TASK_ACCOUNT/getMetaData?0.5907983814673263&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 5
caseinfo['name'] = '列表获取-作业票台账'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] = {"条件":[{"模式":"票证明细", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TICKET_ACCOUNT/getMetaData?0.6478634844788336&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TICKET_ACCOUNT/getMetaData?0.6478634844788336&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 6
caseinfo['name'] = '列表获取-作业预约'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_APPOINT/getMetaData?0.7380381398921954&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/getMetaData?0.7380381398921954&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 7
caseinfo['name'] = '列表获取-气体检测录入'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TICKET_VIEW_GAS/getMetaData?0.35406928108572977&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TICKET_VIEW_GAS/getMetaData?0.35406928108572977&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 8
caseinfo['name'] = '列表获取-盲板管理'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/MSG_NOTICE_PORTAL/qryNotice?0.9089411082178633&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/MSG_NOTICE_PORTAL/qryNotice?0.9089411082178633&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())


caseinfo['id'] = 9
caseinfo['name'] = '列表获取-四类资质台账-申请人资质台账'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_SQR/getMetaData?0.7202539328628557&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_SQR/getMetaData?0.7202539328628557&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 10
caseinfo['name'] = '列表获取-四类资质台账-作业人资质台账'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/getMetaData?0.4272139951368694&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_ZYR/getMetaData?0.4272139951368694&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 11
caseinfo['name'] = '列表获取-四类资质台账-监护人资质台账'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_JHR/getMetaData?0.14439526182521178&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_JHR/getMetaData?0.14439526182521178&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

caseinfo['id'] = 12
caseinfo['name'] = '列表获取-四类资质台账-批准人资质台账'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_PZR/getMetaData?0.6495802126366548&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/sy/SY_USER_PERSONAPTITUDE_HSE_PZR/getMetaData?0.6495802126366548&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit82.append(caseinfo.copy())

