#查询
from globalpkg.global_var import work_appoint_id
from tools import tool
from globalpkg.global_var import tsi
from globalpkg.global_var import workticketid
from globalpkg.global_var import worktaskid
from globalpkg.global_var import jsaid
from globalpkg.global_var import safeclarid
from globalpkg.global_var import sql_query_work_appointid
from tools.gethost import host
from tools.gethost import pro

case = '手机端查询'
projectname = pro()
host = host(projectname)
print(host)
#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now
#mendtime = tool.mendtime
#作业预约名称
name = tool.ran_name_with_str()
print(name)
#用例信息变量定义
testsuit4 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = 'get'
caseinfo['isactive'] = ''
#work_appoint_id_plus1=  work_appoint_id+1


count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业预约查询'
caseinfo['flag'] = 'get'
caseinfo['isactive'] = 1
#拼写预约URL
url2='http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_APPOINT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22status%22%3Anull%2C%22territorialunitid%22%3Anull%2C%22territorialunitname%22%3Anull%2C%22territorialunitcode%22%3Anull%2C%22territorialdeviceid%22%3A2000000003454%2C%22territorialdevicename%22%3A%22%E5%88%B6%E6%B0%A2%E8%A3%85%E7%BD%AE%22%7D&page=1&rows=50&0.6030011008821943&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url2
testsuit4.append(caseinfo.copy())

#
#用例信息
caseinfo['id'] = 2
caseinfo['name'] = '安全分析查询'
caseinfo['isactive'] = 1
url = 'http://192.168.6.27:6030/hse/HSE_SAFETY_TASK_RISK/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_SAFETY_TASK_RISK&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workstatus%22%3Anull%2C%22workunit%22%3A1688712%2C%22workunitname%22%3A%22%E9%95%BF%E5%BA%86%E7%9F%B3%E5%8C%96%E5%88%86%E5%85%AC%E5%8F%B8%22%7D&page=1&rows=50&0.8145466573055407&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url
caseinfo['flag'] = 'get'
testsuit4.append(caseinfo.copy())

#
#用例信息
caseinfo['id'] = 3
caseinfo['name'] = '作业任务查询'
caseinfo['isactive'] = 1
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_MCQ/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_MCQ&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workstatus%22%3Anull%2C%22territorialunitid%22%3A2000000003339%2C%22territorialunitname%22%3A%22%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8%22%2C%22territorialunitcode%22%3A%22CS8082020%22%7D&page=1&rows=50&0.1631214342555447&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url
caseinfo['flag'] = 'get'
testsuit4.append(caseinfo.copy())
#用例信息
caseinfo['id'] = 4
caseinfo['name'] = '任务台账查询'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_ACCOUNT_MCQ/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_ACCOUNT_MCQ&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workticketstatus%22%3Anull%2C%22territorialunitid%22%3A2000000003339%2C%22territorialunitname%22%3A%22%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8%22%2C%22territorialunitcode%22%3A%22CS8082020%22%7D&page=1&rows=50&0.3403124629856198&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url
caseinfo['flag'] = 'get'
testsuit4.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 5
caseinfo['name'] = '作业票台账查询'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_ACCOUNT_MCQ/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_ACCOUNT_MCQ&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktype%22%3Anull%2C%22level_upgrade%22%3Anull%2C%22close_type%22%3Anull%2C%22territorialunitid%22%3A2000000003339%2C%22territorialunitname%22%3A%22%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8%22%7D&page=1&rows=50&0.945051611176241&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url
caseinfo['flag'] = 'get'
testsuit4.append(caseinfo.copy())

