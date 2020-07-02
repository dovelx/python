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
case = '长岭项目作业许可-PC-修改'
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
testsuit83 = []
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
caseinfo['name'] = '修改-安全分析及交底'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ""
editId = jsaid +40
topEntityId = jsaid+40
#caseinfo['exresult'] =  {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_SAFETY_TASK/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=2000000001060&topFuncCode=HSE_SAFETY_TASK&dataId=2000000001066&editId=2000000001060&0.6141283312839432&contentType=json&ajax=true&tid=2000000001003
url = "http://192.168.6.156/hse/HSE_SAFETY_TASK/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK&editId=%d&0.4490311559930189&contentType=json&ajax=true&tid=2000000001003"%(topEntityId,editId)
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit83.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = '修改-作业任务'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
dataId = jsaid+40
topEntityId =worktaskid
editId = worktaskid
#caseinfo['exresult'] = {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TASK/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=2000000003089&topFuncCode=HSE_WORK_TASK&dataId=2000000003089&editId=2000000003089&0.9743156611924968&contentType=json&ajax=true&tid=2000000001003

url = 'http://192.168.6.156/hse/HSE_WORK_TASK/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TASK&dataId=%d&editId=%d&0.9743156611924968&contentType=json&ajax=true&tid=2000000001003'%(topEntityId,dataId,editId)
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit83.append(caseinfo.copy())


caseinfo['id'] = 3
caseinfo['name'] = '修改-作业预约'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] = {"条件":[{"模式":"用火作业", "消息":"失败，python没找到预期结果"}]}
topEntityId = sql_query_work_appointid
editId = sql_query_work_appointid
#http://192.168.6.156/hse/HSE_WORK_APPOINT/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=2000000000390&topFuncCode=HSE_WORK_APPOINT&editId=2000000000390&0.8780054258522736&contentType=json&ajax=true&tid=2000000001003
#http://192.168.6.156/hse/HSE_WORK_APPOINT/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=2000000000603&topFuncCode=HSE_WORK_APPOINT&dataId=2000000000547&editId=2000000000603&0.9438259609803084&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_APPOINT&editId=%d&0.8780054258522736&contentType=json&ajax=true&tid=2000000001003'%(topEntityId,editId)
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit83.append(caseinfo.copy())

caseinfo['id'] = 4
caseinfo['name'] = '修改-气体检测录入'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
topEntityId = workticketid
editId = workticketid
#caseinfo['exresult'] = {"条件":[{"模式":"票证明细", "消息":"失败，python没找到预期结果"}]}
#http://192.168.6.156/hse/HSE_WORK_TICKET_VIEW_GAS/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=2000000004548&topFuncCode=HSE_WORK_TICKET_VIEW_GAS&editId=2000000004548&0.8603140809617669&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TICKET_VIEW_GAS/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_WORK_TICKET_VIEW_GAS&editId=%d&0.8603140809617669&contentType=json&ajax=true&tid=2000000001003'%(topEntityId,editId)
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit83.append(caseinfo.copy())

caseinfo['id'] = 5
caseinfo['name'] = '修改-盲板管理'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
#caseinfo['exresult'] =  {"条件":[{"模式":"中石化长岭分公司", "消息":"失败，python没找到预期结果"}]}
topEntityId = workticketmbcdid
editId = workticketmbcdid
dataId = workticketmbcdid
print("topEntityId",topEntityId)
#url = 'http://192.168.6.156/hse/HSE_TICKET_MBCD/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=2000000000010&topFuncCode=HSE_TICKET_MBCD&editId=2000000000010&0.7293659931303327&contentType=json&ajax=true&tid=2000000001003'
url = 'http://192.168.6.156/hse/HSE_TICKET_MBCD/cardEdit?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_TICKET_MBCD&editId=%d&0.7293659931303327&contentType=json&ajax=true&tid=2000000001003'%(topEntityId,editId)
#print(url)
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit83.append(caseinfo.copy())

