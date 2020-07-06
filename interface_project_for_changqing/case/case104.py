#手机端作业票统计
from tools import tool
from globalpkg.global_var import workticketid
from tools import mname

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime
#作业预约名称
name = mname.name
print("use name",name)
case = '手机端作业票统计'
#用例信息变量定义
testsuitm104 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''



casename = '统计分析-作业票统计'
caseinfo['id'] = 1041
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORKTICKET_COUNT_M/showReport.json?queryParam=%7B%22starttime%22:%222020-06-02%20%22,%22endtime%22:%222020-06-30%20%22,%22orgid%22:1688712,%22territorialunitname%22:%22%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%88%86%E5%85%AC%E5%8F%B8%22,%22workstatus%22:%22draft,sceneConfirm,close,inJob,Invalid,inaudit,stop%22%7D'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm104.append(caseinfo.copy())

casename = '统计分析-作业耗时统计'
caseinfo['id'] = 1042
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TASK_TIME_CONSUME_M/showReport.json?queryParam=%7B%22starttime%22:%222020-06-02%20%22,%22endtime%22:%222020-06-30%20%22,%22territorialunitid%22:1688712,%22territorialunitname%22:%22%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%88%86%E5%85%AC%E5%8F%B8%22%7D'
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm104.append(caseinfo.copy())

casename = '公共功能-作业处理-作业票浏览'
caseinfo['id'] = 1043
caseinfo['name'] = casename
url = 'http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_M/showReport.json?workticketid=%d'%(workticketid)
data = {}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm104.append(caseinfo.copy())