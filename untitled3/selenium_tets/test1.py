
b = []
case = {}
caseinfo = {}
caseinfo['id'] = {}
caseinfo['name'] = {}
caseinfo['result'] = {}






caseid = 1
casename = '预约列表接口获取'
count =1



caseinfo['id'] = caseid
caseinfo['name'] = casename
caseinfo['result'] = 1
print(caseinfo)

b.append(caseinfo.copy())


casename = '预约列表接口获取11'
count =count+1
caseid =count
caseinfo['id'] = caseid
caseinfo['name'] = casename
caseinfo['result'] = 1
print(caseinfo)
b.append(caseinfo.copy())

print(b)