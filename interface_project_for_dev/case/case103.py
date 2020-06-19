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
case = '手机全流程'
#用例信息变量定义
testsuitm100 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''