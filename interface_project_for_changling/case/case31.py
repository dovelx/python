#手机端主流程全票-全票-作业处理-作业票关闭

from case.case2 import *

#用例信息变量定义
testsuitm31= []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

#用火作业-作业票关闭
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid1+1
caseinfo['id'] = 311
caseinfo['name'] = '作业处理-用火作业-生产单位监护人-作业票关闭'
#http://192.168.6.156/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketAudit.json?actionCode=close&workticketid=2000000003758
url = 'http://192.168.6.156/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketAudit.json?actionCode=close&workticketid=%d'%(workticketidx)
data = {
	"reason": "说明",
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007465",
		"personList": [{
			"cardnum": "16143013651646800519",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646800519",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000016201,
				"person_name": "赵成"
			},
			"person_name": "赵成",
			"personid": 2000000016201,
			"specialworktype": "",
			"uuid": "1592960372875"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 16,
		"isinputidnumber": 0,
		"name": "生产单位监护人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 16
	}],
	"mainAttributeVO": {
		"cardnum": "16143013651646800519",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646800519",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000016201,
			"person_name": "赵成"
		},
		"person_name": "赵成",
		"personid": 2000000016201,
		"specialworktype": "",
		"uuid": "1592960372875"
	},
	"closeType": "completion"
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm31.append(caseinfo.copy())

#用火作业-作业票关闭
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid1+1
caseinfo['id'] = 312
caseinfo['name'] = '作业处理-用火作业-施工单位监护人-作业票关闭'
#http://192.168.6.156/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketAudit.json?actionCode=close&workticketid=2000000003758
url = 'http://192.168.6.156/m/hse_m/HSE_WORKTASK_INJOB_M/saveCloseTicketAudit.json?actionCode=close&workticketid=%d'%(workticketidx)
data = {
	"reason": "说明",
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007466",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 17,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nkv8CMrfOA9o14mMAAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "施工单位监护人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nkv8CMrfOA9o14mMAAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 17
	}],
	"mainAttributeVO": {},
	"closeType": "completion"
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm31.append(caseinfo.copy())