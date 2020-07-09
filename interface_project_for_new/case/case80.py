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
case = '长岭项目作业许可-PC-查询'
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
testsuit80 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''
caseinfo['exresult'] = {}

count =0

#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业预约-查询'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ''
#http://192.168.6.156/hse/HSE_WORK_APPOINT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000000603&topFuncCode=HSE_WORK_APPOINT&dataId=2000000000603&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22wf_audit_state%22%3Anull%2C%22workname%22%3A%22Python%22%7D&page=1&rows=50&0.9318498526180168&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000000603&topFuncCode=HSE_WORK_APPOINT&dataId=2000000000603&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22wf_audit_state%22%3Anull%2C%22workname%22%3A%22Python%22%7D&page=1&rows=50&0.9318498526180168&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit80.append(caseinfo.copy())

caseinfo['id'] = 2
caseinfo['name'] = '安全分析模板-查询'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ''
#http://192.168.6.156/hse/HSE_JSA_TEMPLETE/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000000121&topFuncCode=HSE_JSA_TEMPLETE&dataId=2000000000121&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22temp_type%22%3Anull%2C%22temp_name%22%3A%22%E4%B8%80%E9%83%A8%22%7D&page=1&rows=50&0.8768547035065575&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_JSA_TEMPLETE/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000000121&topFuncCode=HSE_JSA_TEMPLETE&dataId=2000000000121&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22temp_type%22%3Anull%2C%22temp_name%22%3A%22%E4%B8%80%E9%83%A8%22%7D&page=1&rows=50&0.8768547035065575&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit80.append(caseinfo.copy())

caseinfo['id'] = 3
caseinfo['name'] = '任务台账-查询'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ''
#http://192.168.6.156/hse/HSE_WORK_TASK_ACCOUNT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_ACCOUNT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workname%22%3A%22Python%22%2C%22site%22%3A%22%E5%8C%97%E4%BA%AC%22%7D&page=1&rows=50&0.48421305260078307&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TASK_ACCOUNT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_ACCOUNT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22workname%22%3A%22Python%22%2C%22site%22%3A%22%E5%8C%97%E4%BA%AC%22%7D&page=1&rows=50&0.48421305260078307&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit80.append(caseinfo.copy())

caseinfo['id'] = 4
caseinfo['name'] = '作业票台账-查询'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ''
#http://192.168.6.156/hse/HSE_WORK_TICKET_ACCOUNT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000004537&topFuncCode=HSE_WORK_TICKET_ACCOUNT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktype%22%3Anull%2C%22level_upgrade%22%3Anull%2C%22close_type%22%3Anull%2C%22workname%22%3A%22Python%22%2C%22site%22%3A%22%E5%8C%97%E4%BA%AC%22%7D&page=1&rows=50&0.416309376363438&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TICKET_ACCOUNT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000004537&topFuncCode=HSE_WORK_TICKET_ACCOUNT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktype%22%3Anull%2C%22level_upgrade%22%3Anull%2C%22close_type%22%3Anull%2C%22workname%22%3A%22Python%22%2C%22site%22%3A%22%E5%8C%97%E4%BA%AC%22%7D&page=1&rows=50&0.416309376363438&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit80.append(caseinfo.copy())

caseinfo['id'] = 5
caseinfo['name'] = '作业预约-查询'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ''
#http://192.168.6.156/hse/HSE_WORK_APPOINT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_APPOINT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22wf_audit_state%22%3Anull%2C%22workname%22%3A%22Python%22%2C%22worksite%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22appointstarttime%22%3A%222020-06-25%2009%3A25%3A52%22%2C%22to_appointstarttime%22%3A%222020-07-31%2009%3A25%3A59%22%7D&page=2&rows=50&0.8754441527842027&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_APPOINT/listQuery?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_APPOINT&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22wf_audit_state%22%3Anull%2C%22workname%22%3A%22Python%22%2C%22worksite%22%3A%22%E5%8C%97%E4%BA%AC%22%2C%22appointstarttime%22%3A%222020-06-25%2009%3A25%3A52%22%2C%22to_appointstarttime%22%3A%222020-07-31%2009%3A25%3A59%22%7D&page=2&rows=50&0.8754441527842027&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit80.append(caseinfo.copy())

caseinfo['id'] = 6
caseinfo['name'] = '气体检测录入-查询'
caseinfo['isactive'] = 1
caseinfo['flag'] = 'get'
caseinfo['exresult'] = ''
#http://192.168.6.156/hse/HSE_WORK_TICKET_VIEW_GAS/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000004541&topFuncCode=HSE_WORK_TICKET_VIEW_GAS&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktype%22%3Anull%2C%22worklevel_dh%22%3Anull%2C%22worklevel_sx%22%3Anull%2C%22workcontent%22%3A%22%E4%BD%9C%E4%B8%9A%E5%86%85%E5%AE%B9%22%7D&page=1&rows=50&0.3947778044568262&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_WORK_TICKET_VIEW_GAS/listQuery?parentEntityId=&parentFuncCode=&topEntityId=2000000004541&topFuncCode=HSE_WORK_TICKET_VIEW_GAS&queryParam=%7B%22tableName%22%3Anull%2C%22columnValues%22%3Anull%2C%22worktype%22%3Anull%2C%22worklevel_dh%22%3Anull%2C%22worklevel_sx%22%3Anull%2C%22workcontent%22%3A%22%E4%BD%9C%E4%B8%9A%E5%86%85%E5%AE%B9%22%7D&page=1&rows=50&0.3947778044568262&contentType=json&ajax=true&tid=2000000001003'
caseinfo['url'] = url
data = {}
caseinfo['data'] =data
testsuit80.append(caseinfo.copy())
