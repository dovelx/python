from case.case15 import *

case = '长岭项目作业许可-PC-安全关闭'

#times
starttime = tool.starttime
endtime = tool.endtime
now = tool.now

#作业预约名称
name = tool.ran_name_with_str()
print("作业预约名称：",name)

#用例信息变量定义
testsuit16 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = 'post'
caseinfo['isactive'] = ''

count =0
#用例信息
caseinfo['id'] = 1
caseinfo['name'] = '安全分析-关闭'
caseinfo['isactive'] = 1
#拼写预约URL
#http://192.168.6.156/hse/HSE_SAFETY_TASK/closeSafety?parentEntityId=&parentFuncCode=&topEntityId=2000000000915&topFuncCode=HSE_SAFETY_TASK&0.9754051630981275&contentType=json&ajax=true&tid=2000000001003
url = 'http://192.168.6.156/hse/HSE_SAFETY_TASK/closeSafety?parentEntityId=&parentFuncCode=&topEntityId=%d&topFuncCode=HSE_SAFETY_TASK&0.9754051630981275&contentType=json&ajax=true&tid=2000000001003'%(topEntityId)
caseinfo['url'] = url
#全票数据
data = {"worktaskid":topEntityId,"revampandadvide":"很好"}
caseinfo['data'] =data
testsuit16.append(caseinfo.copy())
