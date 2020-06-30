
from case.case1 import testsuit1
from case.case2 import testsuitm2
from case.case31 import testsuitm31
from case.case32 import testsuitm32
from case.case33 import testsuitm33
from case.case34 import testsuitm34
from case.case36 import testsuitm36
from case.case37 import testsuitm37
from case.case38 import testsuit38
from case.case39 import testsuitm39
from case.case40 import testsuitm40
from case.case60 import testsuitm60

tt = []
caseinfo = {}
caseinfo['num'] = 1

caseinfo['num'] = len(testsuit1)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm2)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm31)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm32)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm33)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm34)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm36)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm37)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm39)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm40)
tt.append(caseinfo.copy())
caseinfo['num'] = len(testsuitm60)
tt.append(caseinfo.copy())



print (len(tt))
print(tt)
for i in range(len(tt)):
    tt[i] = tt[i]['num']
print(tt)

print(sum(tt))