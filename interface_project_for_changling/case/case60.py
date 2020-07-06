#手机端-列表获取
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

case = '长岭项目作业许可-手机端-列表获取'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)


#用例信息变量定义
testsuitm60 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''
caseinfo['exresult'] = ''

#作业预约
caseinfo['id'] = 6001
caseinfo['name'] = '作业预约-待我审批-列表获取'
#http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/getMetaData.json?mv=-835157820&dv=-1082749909
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_APPOINTAUDIT_M/getMetaData.json?mv=-835157820&dv=-1082749909'
data = {}
caseinfo['url'] = url
caseinfo['exresult'] = 'HSE_WORK_APPOINT'
caseinfo['exresult'] = {
"检查":"body",
"匹配规则":"匹配正则表达式",
"条件":[{"模式":"HSE_WORK_APPOINT", "消息":"失败，未找到HSE_WORK_APPOINT"}]
}
caseinfo['data'] =data
testsuitm60.append(caseinfo.copy())

#作业预约
caseinfo['id'] = 6002
caseinfo['name'] = '作业预约-全部-列表获取'
#http://192.168.6.156/m/hse_m/HSE_WORK_APPOINT_M/getMetaData.json?mv=-1336033614&dv=-1082749909
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_APPOINT_M/getMetaData.json?mv=-1336033614&dv=-1082749909'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
caseinfo['exresult'] = {"条件":[{"模式":"pythnnnon", "消息":"失败，python"}]}
testsuitm60.append(caseinfo.copy())

#安全分析
caseinfo['id'] = 6003
caseinfo['name'] = '安全分析-列表获取'
#http://192.168.6.156/m/hse_m/HSE_SAFETY_TASK_M/getMetaData.json?mv=1641905207&dv=1930087840
url = 'http://192.168.6.156/m/hse_m/HSE_SAFETY_TASK_M/getMetaData.json?mv=1641905207&dv=1930087840'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
caseinfo['exresult'] = ''
testsuitm60.append(caseinfo.copy())

#作业申请
caseinfo['id'] = 6004
caseinfo['name'] = '作业申请-列表获取'
#http://192.168.6.156/m/hse_m/HSE_WORKAPPLY_GB_M/getMetaData.json?mv=-874476096&dv=-1377575074
url = 'http://192.168.6.156/m/hse_m/HSE_WORKAPPLY_GB_M/getMetaData.json?mv=-874476096&dv=-1377575074'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
caseinfo['exresult'] = ''
testsuitm60.append(caseinfo.copy())

#现场确认
caseinfo['id'] = 6005
caseinfo['name'] = '现场确认-列表获取'
#http://192.168.6.156/m/hse_m/HSE_WORK_TASK_M/getMetaData.json?mv=218310574&dv=889100042
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TASK_M/getMetaData.json?mv=218310574&dv=889100042'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
caseinfo['exresult'] = ''
testsuitm60.append(caseinfo.copy())

#作业处理
caseinfo['id'] = 6006
caseinfo['name'] = '作业处理-列表获取'
#http://192.168.6.156/m/hse_m/HSE_WORKTASK_INJOB_M/getMetaData.json?mv=395905252&dv=-13421365
url = 'http://192.168.6.156/m/hse_m/HSE_WORKTASK_INJOB_M/getMetaData.json?mv=395905252&dv=-13421365'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
caseinfo['exresult'] = ''
testsuitm60.append(caseinfo.copy())

#补票
caseinfo['id'] = 6007
caseinfo['name'] = '作业处理-补票'
#http://192.168.6.156/m/hse_m/HSE_WORKAPPLY_BP_GB_M/getMetaData.json?mv=2082979805&dv=-412486718
url = 'http://192.168.6.156/m/hse_m/HSE_WORKAPPLY_BP_GB_M/getMetaData.json?mv=2082979805&dv=-412486718'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
caseinfo['exresult'] = ''
testsuitm60.append(caseinfo.copy())

#办票耗时
caseinfo['id'] = 6008
caseinfo['name'] = '作业处理-办票耗时'
#http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_TIME_CONSUM_M/workTimeConsum.json?orgid=2000000004016&starttime=2020-5-01&endtime=2020-5-31&displayorder=0
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_TIME_CONSUM_M/workTimeConsum.json?orgid=2000000004016&starttime=2020-5-01&endtime=2020-5-31&displayorder=0'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
caseinfo['exresult'] = ''
testsuitm60.append(caseinfo.copy())