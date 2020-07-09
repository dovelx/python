#作业票统计
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

case = '作业统计'
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
testsuit6 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = 'gh'
caseinfo['isactive'] = ''
#work_appoint_id_plus1=  work_appoint_id+1


count =0


#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '作业票统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_WORKTICKET_COUNT/reportCommonShow?rpx=HSE_WORKTICKET_COUNT.rpx&scroll=no&pcContext=http%3A%2F%2F192.168.6.27%3A6030&endtime=2020-06-30&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&starttime=2020-06-01&uuid=9d8c9c18a99a42548b538093bada71ddlbztQoQMMwTiUvIjVMrTEGqmilRoIg&orgid=2000000003339'
url = 'http://192.168.6.27:6030/hse/HSE_WORKTICKET_COUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_COUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522orgid%2522%253A2000000003339%252C%2522workstatus_name%2522%253Anull%252C%2522workstatus%2522%253Anull%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-06-30%2522%257D&0.008379536495610518'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 2
caseinfo['name'] = '作业任务耗时统计'
caseinfo['isactive'] = 1

url = 'http:/192.168.6.27:6030/rqreports/hse/HSE_WORK_TASK_TIME_CONSUME/reportCommonShow?rpx=HSE_WORK_TASK_TIME_CONSUME.rpx&scroll=no&territorialunitid=2000000003446%2C2000000003447%2C2000000003448%2C2000000003454%2C2000000003339&pcContext=http%3A%2F%2F192.168.6.27%3A6030&endtime=2020-06-30&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&starttime=2020-06-01&uuid=1cbe8564037d459bb4db4a39cd4020a8HosHIqZOmPDLcybRhaJGoQwYhaiuLh'
url = 'http://192.168.6.27:6030/hse/HSE_WORK_TASK_TIME_CONSUME/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TASK_TIME_CONSUME&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522territorialunitid%2522%253A2000000003339%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-06-30%2522%257D&0.12146890279915779'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 3
caseinfo['name'] = '作业方式统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_WORKTICKET_COUNT_WAY/reportCommonShow?rpx=HSE_WORKTICKET_COUNT_WAY.rpx&scroll=no&pcContext=http%3A%2F%2F192.168.6.27%3A6030&endtime=2020-06-30&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&starttime=2020-06-01&uuid=ed11c0e6d9514f4198ddbeee63a11843fpdVAKtDNDaLXHRjQvYPncJTyxhyxD&orgid=2000000003339'
url = 'http://192.168.6.27:6030/hse/HSE_WORKTICKET_COUNT_WAY/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_COUNT_WAY&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522orgid%2522%253A2000000003339%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-06-30%2522%257D&0.9642268208485587'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 4
caseinfo['name'] = '超期关闭作业数量统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_WORKTASK_OVERDUE/reportCommonShow?planendtime=2020-06-30&pcContext=http%3A%2F%2F192.168.6.27%3A6030&planstarttime=2020-06-01&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&rpx=HSE_WORKTASK_OVERDUE.rpx&uuid=7cf6492b9e934c32b79c61428c2c98d9axZnSdGQOussOtKtyTPpAuunSxpYYS&orgid=2000000003339'
url = 'http://192.168.6.27:6030/hse/HSE_WORKTASK_OVERDUE/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTASK_OVERDUE&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522isleaf%2522%253Anull%252C%2522orgid%2522%253A2000000003339%252C%2522planstarttime%2522%253A%25222020-06-01%2522%252C%2522planendtime%2522%253A%25222020-06-30%2522%257D&0.6552339188722254'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 5
caseinfo['name'] = '加急票比率统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_WORKTASK_URGENT/reportCommonShow?planendtime=2020-06-30&pcContext=http%3A%2F%2F192.168.6.27%3A6030&planstarttime=2020-06-01&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&rpx=HSE_WORKTASK_URGENT.rpx&uuid=4b475c00d3fd4acd92235126f57061c9PKtbdeXATfudipvvlZfYclMjvmKTDC&orgid=2000000003339'
url = 'http://192.168.6.27:6030/hse/HSE_WORKTASK_URGENT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTASK_URGENT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522isleaf%2522%253Anull%252C%2522orgid%2522%253A2000000003339%252C%2522planstarttime%2522%253A%25222020-06-01%2522%252C%2522planendtime%2522%253A%25222020-07-01%2522%257D&0.1314452009483691'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 6
caseinfo['name'] = '气体检测超期统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_WORKTICKET_OVERGAS/reportCommonShow?planendtime=2020-06-30&pcContext=http%3A%2F%2F192.168.6.27%3A6030&planstarttime=2020-06-01&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&rpx=HSE_WORKTICKET_OVERGAS.rpx&uuid=dddf6232745e40ae8ed1e0394226df23hQoildDuCodcUGhaApmziwbgqCttDE&orgid=2000000003339'
url = 'http://192.168.6.27:6030/hse/HSE_WORKTICKET_OVERGAS/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_OVERGAS&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522isleaf%2522%253Anull%252C%2522orgid%2522%253A2000000003339%252C%2522planstarttime%2522%253A%25222020-06-01%2522%252C%2522planendtime%2522%253A%25222020-06-30%2522%257D&0.7025271429863089'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 7
caseinfo['name'] = '非固定动火日动火统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_WORKTICKET_NONFIREDAY/reportCommonShow?planendtime=2020-06-30&pcContext=http%3A%2F%2F192.168.6.27%3A6030&planstarttime=2020-06-01&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&rpx=HSE_WORKTICKET_NONFIREDAY.rpx&uuid=42ec3c86819e49f4a9f4af82a32bbf49ZJXyLtvdzmEoYEjIzhBpgDpsqMCUjX&orgid=2000000003339'
url = 'http://192.168.6.27:6030/hse/HSE_WORKTICKET_NONFIREDAY/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORKTICKET_NONFIREDAY&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522isleaf%2522%253Anull%252C%2522orgid%2522%253A2000000003339%252C%2522planstarttime%2522%253A%25222020-06-01%2522%252C%2522planendtime%2522%253A%25222020-06-30%2522%257D&0.699220057174867'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 8
caseinfo['name'] = '作业执行率统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_APPOINT_EXECUTE_ACCOUNT/reportCommonShow?pcContext=http%3A%2F%2F192.168.6.27%3A6030&endtime=2020-06-30&territorialunitname=%E8%BF%90%E8%A1%8C%E4%B8%80%E9%83%A8&starttime=2020-06-01&rpx=HSE_APPOINT_EXECUTE_ACCOUNT.rpx&uuid=42d56d7549a84f14afa8edc90a223928PQTuPiEOUHhWyyWxelRmFzUfEdIOUc&orgid=2000000003339'
url = 'http://192.168.6.27:6030/hse/HSE_APPOINT_EXECUTE_ACCOUNT/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_APPOINT_EXECUTE_ACCOUNT&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522territorialunitname%2522%253A%2522%25E8%25BF%2590%25E8%25A1%258C%25E4%25B8%2580%25E9%2583%25A8%2522%252C%2522isleaf%2522%253Anull%252C%2522orgid%2522%253A2000000003339%252C%2522starttime%2522%253A%25222020-06-01%2522%252C%2522endtime%2522%253A%25222020-06-30%2522%257D&0.22794907445984158'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 9
caseinfo['name'] = '数据上报汇总统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/rqreports/hse/HSE_DATA_REPORT_CQSH/reportCommonShow?pcContext=http%3A%2F%2F192.168.6.27%3A6030&strdate=2020-06-01&rpx=HSE_DATA_REPORT_CQSH.rpx&uuid=6c645824a037425ea0e775f60daa8809SgODtRQonEdfwcQbFxpWkNOayHfAFB'
url = 'http://192.168.6.27:6030/hse/HSE_DATA_REPORT_CQSH/showReport?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_DATA_REPORT_CQSH&queryParam=%257B%2522tableName%2522%253Anull%252C%2522columnValues%2522%253Anull%252C%2522strdate%2522%253A%25222020-05-01%2522%257D&0.6193284880765868'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())

#用例信息
caseinfo['id'] = 10
caseinfo['name'] = '办票耗时统计'
caseinfo['isactive'] = 1

url = 'http://192.168.6.27:6030/hse/HSE_WORK_TICKET_TIME_CONSUM/workTimeConsum?parentEntityId=&parentFuncCode=&topEntityId=&topFuncCode=HSE_WORK_TICKET_TIME_CONSUM&orgid=&starttime=&endtime=&displayorder=0&0.5077457100068974&contentType=json&ajax=true&tid=1'
caseinfo['url'] = url
caseinfo['flag'] = 'gh'
testsuit6.append(caseinfo.copy())