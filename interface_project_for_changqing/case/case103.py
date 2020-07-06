#手机端查询
#作业许可-作业申请，现场确认，作业处理
from tools import tool
from globalpkg.global_var import sql_query_work_appointid
from tools import mname
from tools import minsert
#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime
#作业预约名称
name = mname.name
print("use name",name)
case = '手机端查询'
#用例信息变量定义
testsuitm103 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

#公共功能
casename = '公共功能-作业处理-查询'
caseinfo['id'] = 1031
caseinfo['name'] = casename
url = '''http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_WORK_TASK_MCQ&0.9651365781343351&contentType=json&ajax=true&tid=1http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/listQuery.json?queryType=2&level=2&page=1&rows=10&extWhere=(workname%20like%20'%25%E5%8C%97%E5%8C%BA%25'%20or%20workunitname%20like%20'%25%E5%8C%97%E5%8C%BA%25'%20or%20workcontent%20like%20'%25%E5%8C%97%E5%8C%BA%25')'''
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm103.append(caseinfo.copy())

#公共功能
casename = '公共功能-现场确认-查询'
caseinfo['id'] = 1032
caseinfo['name'] = casename
url = '''http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_M/listQuery.json?queryType=2&level=2&page=1&rows=10&extWhere=(workname%20like%20'%25Python%25'%20or%20workunitname%20like%20'%25python%25'%20or%20workcontent%20like%20'%25python%25')'''
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm103.append(caseinfo.copy())

casename = '公共功能-作业处理-查询'
caseinfo['id'] = 1033
caseinfo['name'] = casename
url = '''http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/listQuery.json?queryType=2&level=2&page=1&rows=10&extWhere=(workname%20like%20'%25Python%25'%20or%20workunitname%20like%20'%25Python%25'%20or%20workcontent%20like%20'%25Python%25')'''
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm103.append(caseinfo.copy())

casename = '公共功能-作业处理-查询'
caseinfo['id'] = 1034
caseinfo['name'] = casename
url = '''http://192.168.6.27:6030/m/hse_m/HSE_WORKTASK_INJOB_M/listQuery.json?queryType=2&level=2&page=1&rows=10&extWhere=(workname%20like%20'%25Python%25'%20or%20workunitname%20like%20'%25Python%25'%20or%20workcontent%20like%20'%25Python%25')'''
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm103.append(caseinfo.copy())

