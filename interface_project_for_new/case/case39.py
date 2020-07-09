#手机端主流程全票-全票-现场确认会签

from case.case38 import *

#用例信息变量定义
testsuitm39 = []
caseinfo = {}
caseinfo['id'] = 1
caseinfo['name'] = ''
caseinfo['result'] = ""
caseinfo['url'] = ''
caseinfo['data'] = ''
caseinfo['sign'] =''
caseinfo['flag'] = ''
caseinfo['isactive'] = ''

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid1+1
caseinfo['id'] = 108
caseinfo['name'] = '现场确认-用火作业-属地确认'
#http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=workticketidx&workType=dh&worklevel=gb_dh_workLevel01&tabtype=measure&businesstype=SDQR
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&tabtype=measure&businesstype=SDQR'%(workticketidx)

data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874004509",
		"businesstype": "SDQR"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000007450",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874004509",
			"businesstype": "SDQR"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "确认人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "开展JSA等风险分折,制定相应的作业程序和安全措施。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007153,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs01",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022143,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "用火设备内部的物料、构件清理干净，蒸汽吹扫或水洗合格，达到用火条件。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007154,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs02",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022144,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "断开与用火设备相连的所有管线，加盲板（  哈）块。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007155,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs03",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022145,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "用火前及时通知班长、操作员，涉及（影响）系统、排洪沟等上下游区域通知调度和相关装置负责人。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007156,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs04",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022146,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "特级用火，通知消气防中心现场保镖。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007157,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs05",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022147,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "用火作业已经申报上级业务主管和安全管理部门。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007158,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs06",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022148,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "用火点周围（最小半径15米）下水井、地漏、地沟、电缆沟等采取覆盖、水封等隔离措施。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007159,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs07",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022149,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "距用火点30m内不得排放可燃气体，15m内不得排放可燃液体，同一围堰和防火间距内不得有脱水、采样作业。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007160,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs08",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022150,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "取得合格分析数据，监护人随身携带便携式可燃、有毒气体检测仪随时监测。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007161,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs09",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022151,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "视频监控已落实。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007162,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs10",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022152,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "现场备蒸汽带（  1）根，灭火器（  1）个，防火毯（  3）块。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007163,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs11",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022153,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 109
caseinfo['name'] = '现场确认-用火作业-作业确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&tabtype=measure&businesstype=ZYDY'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "ZYDY"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007451",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "乙炔气瓶（禁止卧放）、氧气瓶与火源的距离不得少于10米；气瓶各连接牢固。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007164,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs12",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022154,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "焊机、开关柜摆放在安全位置；电焊回路线应接在焊件上，焊把线不得穿过下水井或与其它设备搭接。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007165,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs13",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022155,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 110
caseinfo['name'] = '现场确认-用火作业-双方确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&tabtype=measure&businesstype=SFQE'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "SFQE"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007453",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nPLoAEAAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "signandcard",
		"specialworktype": "",
		"value": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAlNSURBVHic7d19yJ1lHQfwr2sznViwiIgghSgRIa2RWc1iLbEXtFaSEvQCle7PCkPK\nqBAzKjBwkCXYH70Rmxk1UqjoD6WwF9DE1VPaK4aFmDlIqWZPfxyrtee613O2c93XOdf5fOBmcMbz\n7HuPh13f/a5zrjsBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADg\nvy5M8vUkO1sHAQD6cXqSm5KsFq7HGuYCABbcjiQPp1wyDr9e0igjALCAtif5WdZXMg69bmwRFgCY\nfyckuTzJfZm+YBx+vX7k7ADAHLs0x14uShcAQJLJFOJYSsWeJO8d+D0AgCTJXzJ9ybj2sO9Ren/H\nF0fIDgAsiD35/wXjYJJrkpw48D1KX7O5amoAYOGUCsPuJCet42ufNvD1AAAzc3PWlo2fNE0EAHSn\nNN04s2kiYOEc1zoAMPdK2yf+7QCmsqF1AGCufazw2oHRUwAAXSttp1zSNBGwkIxFgSOxnQLMhC0V\nYMi7WwcAAPpX2k75SNNEwMIyGgWG2E4BZsaWClBSmmQ4XRQAmKnSdsqupokAgK4cH89OAQAqW8na\nsvFY00QAQHdK043tTRMBAF35bGynAACVlcrGB5smAgC6clVMNwCAykplY1/TRABAV/bGdAMAqKxU\nNvY2TQQAdOXemG4AABWdlXLZuLJlKKA/nvwIy21okuHfBmCmPC0WltedA69vGzUFANCt56W8lfKb\nlqGAfhmbwnKylQKMypYKLJ+fD7y+Y9QUAEC3zk15K+X+lqGA/hmfwnKxlQI0YUsFlscDA69vHTUF\nANCt01LeSrm7ZShgeRijwnKwlQI0ZUsF+vepgddfNGoKAKBrpa2Uh5smAgC68ot4EiwAUNGmlMvG\n7pahAIC+PBTTDQCgoi0pl42LW4YCAPry95huAAAVPT3lsvHClqEAgL4cyNqy8XjTRABAVzamPN04\ntWEmAKAzzt0AAKorlY0dTRMBAF25KaYbAEBlpbKxq2kiAKArl8d0AwCorFQ2bmiaCADoyraYbgAA\nlT2etWVjpWkiAKArQ8eYH98yFADQl9Ix5o82TQQAdMUx5gBAdY4xBwCqc4w5AFDV92K6AQBUViob\nlzZNBAB05Wsx3QAAKiuVjSuaJgIAuvLlmG4AAJWVysbHmyYCALqyN6YbAEBlpbJxddNEAEBXvhHT\nDQCgslLZeH/TRABAV26P6QYAUFmpbOxqmggA6MpKTDcAgIo2pFw23twyFADQl1/FdAMAqOhJKZeN\n81uGAgD68vuYbgAAFW1MuWyc3TIUANCX38V0AwCoaGi6cU7LUABAX34b0w0AoKKhczdMNwCAmbkn\nphsAQGWlsrGjaSIAoCt3xXQDAKjMM1MAgKr2x3QDAKjoySmXjYtahgIA+nIgphvMzqlJPpDk4sY5\nAJgjW+PcDY7OpiRvSfKtlH+GVpMcbJYOgLkytFDAoS5M8pUM/7wc6bqgQV4o2tg6ACypOwde3zJq\nCubJq5Ncksmnk06c0ff08wSwxF6T8v9Gb2sZitG8MsnnkjySo5taTHMBsMQsDsvhFUmuS/Jg6heL\nQ6+fJtk1wv0BMMeGFokzWobimJyS5ENJVjJusXgkyfVJzq1/iwAskjtSXji+3zIUU3l5ki9k3GLx\n6BN/5mtHuD8AFtyLU15M/tkyFEd0XpI9Ga9Y/C3JV5PsTLJhhPsDoENDi4yFZT5ckOSbGadYHExy\ncyafSNk0xs0BsByG3jR4fstQS+xNSb6dccrFviRvS3LCKHcGwNIa+gjsvS1DLZG3ZvJx49rFYiXJ\nFUmePc5tAcD/GlqgmL3XJbk19cvF3kzeZwEAc+H2lBesrS1DdeKUJJ9O3WJxXyZTi6eOdE8AMLVn\nZHgRY3rnJflu6pWL/Unek+SksW4IAGbBVsqx2ZnkrtQpFw8m+Wg8ZwSABXd9ygvd2S1Dzbk3pE7B\n+EeSG5KcOd6tAMA4Sgvf/U0TzZfnJrk2yV8z+4JxayZvHgWArg29d2NZvSDJ7kyO5551ufhzkiuT\nbB7tbgBgTmzL2oXxB00TjWdLkg8neSh13nvx4yRvHO1uAGCOPSvlxfKdLUNV8KokN6ZOsfj39Zkk\np411QwCwaI60iF7WMNfROD3J1Un+kLrlYjXJVXEEOACs23VZ3wJ7TZKTG2U81DOTvD3Jl5L8KfWL\nxWomj1t/6Rg3BwA9+3WmX4S/k+RdSZ4zowwnJzkjk+e5XJbkE5m8D2KMQnHo9aNMCg0AUMEtGX9x\nb319Psn2WfzlAQDrtzmTMzhaF4FZX3ckeV+c1gkAc+cdaV8Upr0eSPLJOKkTABbS85PsS/tCsZrk\nl5kcx35RkqfUvGlgeR3XOgDwHzuTvCzJOU/8Ogt3Z/Ik1P1J7knywyR/nNH3BgAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIDp/QvZeZ4m\nPLoAEAAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "用火点周围（最小半径15米）易燃物、可燃物已经清除。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007166,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs14",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022156,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "高处作业（2米以上）采取防火花飞溅措施，备接火盆（  1）个。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007167,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs15",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022157,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "其他补充安全措施：（ 哈哈）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007168,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "yhcs16",
		"dataStatus": 0,
		"worktype": "dh",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022158,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 111
caseinfo['name'] = '现场确认-用火作业-气体检测'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/gasAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=gas&detectiontype=audit'%(workticketidx)
data = {
	"unCompleteStaticValueList": [{
		"downlimit": 0,
		"groupType": "3",
		"code": "combustible",
		"isincludeboundary": 1,
		"name": "可燃气",
		"dataStatus": 0,
		"value": "0.1",
		"isShow": 1,
		"upperlimit": 0.5
	}, {
		"code": "detectiontype",
		"value": ""
	}, {
		"code": "gasdetectionid",
		"value": ""
	}, {
		"code": "analysisname",
		"value": "作业地点"
	}, {
		"code": "part",
		"value": "炼油北区"
	}, {
		"code": "workticketid",
		"value": ""
	}, {
		"code": "detectiontime",
		"value": now
	}, {
		"code": "iscomplete",
		"value": ""
	}, {
		"code": "created_by",
		"value": ""
	}, {
		"code": "created_dt",
		"value": ""
	}, {
		"code": "updated_by",
		"value": ""
	}, {
		"code": "updated_dt",
		"value": ""
	}, {
		"code": "tenantid",
		"value": ""
	}, {
		"code": "remark",
		"value": ""
	}],
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874193018"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007454",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874193018"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 1,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 0,
		"name": "分析人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 112
caseinfo['name'] = '现场确认-用火作业-会签-申请人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874296404"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007532",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874296404"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 0,
		"name": "申请人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 113
caseinfo['name'] = '现场确认-用火作业-会签-接收人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874312468"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007827",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874312468"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 0,
		"name": "接收人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 6
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 114
caseinfo['name'] = '现场确认-用火作业-会签-用火人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007456",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "用火人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 7
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 115
caseinfo['name'] = '现场确认-用火作业-会签-生产单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874327702"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007457",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874327702"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 1,
		"name": "生产单位监护人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 8
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 116
caseinfo['name'] = '现场确认-用火作业-会签-施工单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007458",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\nAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "施工单位监护人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 9
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 117
caseinfo['name'] = '现场确认-用火作业-会签-施工单位'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007459",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nAAAAwJL6H7ldyW1U+mcNAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "施工单位",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nAAAAwJL6H7ldyW1U+mcNAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 10
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 118
caseinfo['name'] = '现场确认-用火作业-会签-基层安全管理人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874352267"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007461",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874352267"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 5,
		"isinputidnumber": 0,
		"name": "基层安全管理人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 12
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 119
caseinfo['name'] = '现场确认-用火作业-会签-基层领导'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874364158"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007530",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874364158"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 13,
		"isinputidnumber": 0,
		"name": "基层领导",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 13
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 120
caseinfo['name'] = '现场确认-用火作业-会签-基层业务负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874376465"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007529",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874376465"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 13,
		"isinputidnumber": 0,
		"name": "基层业务负责人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 13
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#用火作业
workticketidx = workticketid+3
ts = tsi+3
worktaskidx = worktaskid+1
caseinfo['id'] = 121
caseinfo['name'] = '现场确认-用火作业-会签-二级单位领导'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dh&worklevel=gb_dh_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {
		"cardnum": "16143013651646775869",
		"saveApprvoalInfo": "true",
		"person_type": "orgperson",
		"idnumber": "",
		"busdata": {
			"cardnum": "16143013651646775869",
			"person_type": "orgperson",
			"dataStatus": 0,
			"personid": 2000000013918,
			"person_name": "刘庆红"
		},
		"person_name": "刘庆红",
		"personid": 2000000013918,
		"specialworktype": "",
		"uuid": "1592874385855"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007464",
		"personList": [{
			"cardnum": "16143013651646775869",
			"saveApprvoalInfo": "true",
			"person_type": "orgperson",
			"idnumber": "",
			"busdata": {
				"cardnum": "16143013651646775869",
				"person_type": "orgperson",
				"dataStatus": 0,
				"personid": 2000000013918,
				"person_name": "刘庆红"
			},
			"person_name": "刘庆红",
			"personid": 2000000013918,
			"specialworktype": "",
			"uuid": "1592874385855"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 15,
		"isinputidnumber": 0,
		"name": "二级单位领导",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 15
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())


workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 127
caseinfo['name'] = '现场确认-受限空间-属地确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=sx&tabtype=measure&businesstype=SDQR'%(workticketidx)
data = {
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
		"uuid": "1592874824450",
		"businesstype": "SDQR"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000007467",
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
			"uuid": "1592874824450",
			"businesstype": "SDQR"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "确认人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "开展JSA风险分析，并制定相应作业程序和安全措施。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007138,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs01",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022162,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "盛装过可燃有毒液体、气体的受限空间，所有与受限空间有联系的阀门、管线加盲板隔离，列出盲板清单，并落实拆装盲板责任人。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007139,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs02",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022163,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "盛装过可燃有毒液体、气体的受限空间，设备必须经过置换、吹扫、蒸煮。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007140,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs03",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022164,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "设备打开通风孔进行自然通风，温度适宜人员作业；必要时采取强制通风或佩戴空气呼吸器，但设备内缺氧时，严禁用通氧气的方法补充氧。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007141,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs04",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022165,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 128
caseinfo['name'] = '现场确认-受限空间-作业确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=sx&tabtype=measure&businesstype=ZYDY'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "ZYDY"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007727",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAApWSURBVHic7d1LryVlFYDhdWwioLSQ0AI6aPESheCVGCEkJAYYaIwmgg78U/4SxYEO\nJERNcERi1ADxBpqIhkbEGGhEabv7ONrxuGvtc/al1ldVn8+T7MkarVHlTdX+qiIAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAgE48EBFvRsTTUy8CAPTpoYg4XvsBAIzqcggOoMDR1AsAs5IFhusE\ncLB3Tb0AANA/wQEAlBMcAEA5wQEAlBMcwMrHk9mfm28BdElwACufSWa/bL4F0CXBAazcm8yea74F\n0CXBAazck8x+13wLoEuCA1jJguO3zbcAALr2Rgxfa377pBsB3fDKYmDFa82BMh6pAADlBAcAUE5w\nAADlBAcAUE5wAADlBAcAUE5wAADlBAcQEXFjMrvSfAugW4IDiIi4M5n9pfkWQLcEBxARcVcye7X5\nFkC3BAcQkd/hEBzAaAQHEBFxIZm93nwLoFuCA4iIuCWZvdV8C6BbggOIiDifzAQHMBrBAUTkdzgu\nN98C6JbgACI8UgGKCQ4gwiMVoJjgACIi3pPM3m6+BdAtwQFERJxLZteabwF0S3AAERE3JLOrzbcA\nuiU4gAjBARQTHECERypAMcEBRLjDARQTHECE4ACKCQ4gIuI4mR013wLoluAAIiKuJzPXB2A0LihA\nhOAAirmgABGCAyjmggJE5Edgs6OyAHsRHECEOxxAMRcUIEJwAMVcUICIiCvJ7N3NtwC6JTiAiIh/\nJbObmm8BdEtwABGCAygmOIAIwQEUExxAhOAAigkOIEJwAMUEBxAR8U4yExzAaAQHEOEOB1BMcAAR\neXDc3HwLoFuCA4iIeCuZnW++BdAtwQFERFxOZoIDGI3gACIi3kxmtzTfAuiW4AAi3OEAigkOICK/\nwyE4gNEIDiDCHQ6gmOAAIgQHUOxo6gWA2ThOZq4RwCjc4QAAygkOAKCc4AAAygkOAKCc4AAAygkO\nAKCc4AAAygkOAKCc4AAAygkOAKCc4AAAygkOAKCc4AAAygkOAKCc4ABW3k5m55tvAXRJcAArf01m\n72++BdAlwQGsvJ7MBAcwCsEBrLjDAZQRHMBKFhwXmm8BdElwACvucABlBAew8koyu7P5FkCXBAew\ncimZfaD5FkCXBAewkgXHB5tvAXRJcAAr7nAAAOVujYjjtd8bk24EdONo6gWAWTlOZq4TwME8UgEA\nygkOAKCc4AAAygkOAKCc4AAAygkOAKCc4AAAygkOAKCc4ABOup7MXCeAg7mQACf9KZldbL4F0B3B\nAZz0x2QmOICDCQ7gpJeT2YeabwF0R3AAJ7nDAZQQHMBJWXC4wwEcTHAAJ2WPVNzhAA4mOICT3OEA\nAMrdFBHHa79/TroR0IWjqRcAZuc4mblWAAfxSAUAKCc4AIByggMAKCc4AIByggMAKCc4AIByggNY\n9/dkdnvzLYCuCA5g3UvJ7KPNtwC6IjiAdb9PZh9rvgXQFcEBrMuCwx0O4CCCA1j3YjL7RPMtgK4I\nDmDdb5LZPc23AAC6dmsMvxj7j0k3AhbPFyCBjC/GAqPySAUAKCc4AIByggMAKCc4AIByggMAKCc4\ngMyVZPa+5lsA3RAcQOZXyeze5lsA3RAcQMbbRoFRCQ4g83wy+3TzLYBuCA4g80Iy+1TzLQCArn04\nht9TeWXSjYBF820EYBPfUwFG45EKAFBOcAAA5QQHAFBOcAAA5QQHAFBOcACbvJbMLjbfAuiC4AA2\nyd42+snmWwBdEBzAJllweNsosBfBAWySvd7c91QAgFHdH8PXm2efrQc4k9cUA5scRcT1DXOAnXik\nAmySfUsFYC+CAwAoJzgAgHKCAwAoJziAXfnTKLAzwQGc5tfJ7HPNtwAWT3AAp/l5MhMcwM4EB3Ca\nLDjub74FsHiCAziN4AAAyp2P4evNr0y6EbBI/m0OnCV746hrB7ATj1QAgHKCAwAoJzgAgHKCAzjL\nv5PZbc23ABZNcABneTaZPdB8C2DRBAdwliw4Hmy+BbBoggM4izscAEC5izF8+dffJt0IWBwv7wG2\n4eVfwEE8UgEAygkOAKCc4AAAygkOYBtXk9mF5lsAiyU4gG08k8webr4FsFiCA9jGT5OZ4AAARvVo\nDN/F8bNJNwIAunNDDIMjezcHQMqLe4BtefkXsDf/4QAAygkOAKCc4AAAygkOYFvPJbPHmm8BLJLg\nALb1o2T2aPMtgEUSHMC2suB4pPkWAEDXbg7v4gD25Aw9sAvv4gD24pEKAFBOcAAA5QQHsIuryeyu\n5lsAiyM4gF38JJk5qQKcSXAAu/AuDgCg3OdjeCz25Uk3AhbBcTZgV47GAjvzSAUAKCc4AIByggMY\nw7mpFwDmTXAAu/pFMvtS8y2ARREcwK5+mMy+3HwLAKBrD8fwaOxLk24EzJ6jbMA+HI0FduKRCgBQ\nTnAAAOUEBzAWR2OBjQQHsI8XktljzbcAFkNwAPv4QTL7avMtAICuPRS+GgvswDE2YF+OxgJb80gF\nACgnOACAcoIDGNMdUy8AzJPgAPb1VDL7WvMtgEUQHMC+vp/MHI0FAEZ1MYZHY69OuhEwW46wAYdw\nNBbYikcqAEA5wQEAlBMcwCEuJbMHm28BzJ7gAA7xZDL7evMtAICuPRLDkyovTroRMEv+TQ4cykkV\n4EweqQAA5QQHAFBOcACHupbM7m69BDBvggM41PeSmZMqAMCovhXDkyrPTLoRANCdG2MYHNnJFeD/\nmKNrwBgcjQVO5T8cAEA5wQFUee/UCwDzITiAMfw4mX2z+RbAbAkOYAzfSWZPNN8CAOjaHeGkCnAK\n/yIHxuKkCrCRRyoAQDnBAVQ6N/UCwDwIDmAszyazx5tvAcyS4ADGkp1U+UbzLQCArt0dw1Mq70y5\nEDAf/kEOjMlJFSDlkQoAUE5wAADlBAcwpueT2VeabwHMjuAAxvTdZOabKgDAqO6L4UmVy5NuBMyC\nf48DY3NSBRjwSAUAKCc4AIByggMY2x+S2RdbLwHMi+AAxuabKgBAuS/E8KTKpUk3Aibnn+NABSdV\ngP/hkQoAUE5wAADlBAdQ4dVk9tnmWwCzITiACt9OZq813wIA6N61+O8placn3gUA6NhHpl4AAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAXv0HvkALlME5hJQAAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "检查受限空间内部，具备作业条件，清罐时应使用防爆工具。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007144,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs07",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022168,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "检查受限空间进出口通道，不得有阻碍人员进出的障碍物。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007145,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs08",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022169,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 129
caseinfo['name'] = '现场确认-受限空间-双方确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=sx&tabtype=measure&businesstype=SFQE'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "SFQE"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007728",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "signandcard",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "相关设备进行处理，带有搅拌机的设备应切断电源，挂“禁止合闸”标示牌，设专人监护。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007142,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs05",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022166,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "在进入受限空间作业期间，严禁其它与该设备相关的试车、试压或试验工作及活动。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007143,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs06",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022167,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "盛装过可燃有毒液体、气体的受限空间，应分析可燃、有毒有害气体含量。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007146,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs09",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022170,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "进入受限空间作业人员（首先进入人员和最后出来人员）要携带与作业环境相适应的报警仪（包括可燃气、氧、硫化氢等报警仪）。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007147,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs10",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022171,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业人员应清楚受限空间内存放的其他危害因素，如内部附件、集渣坑等。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007148,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs11",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022172,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业监护人应清楚出入受限空间作业人数、工具、材料。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007149,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs12",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022173,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业监护措施：视频监控（1）消防器材（2）、救生绳（3）、气防装备（4）。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007150,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs13",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022174,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "严禁无防护救援。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007151,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs14",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022175,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "其他补充措施：（ 哈喽）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007152,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "sxcs15",
		"dataStatus": 0,
		"worktype": "sx",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022176,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 130
caseinfo['name'] = '现场确认-受限空间-气体检测'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/gasAudit.json?workticketid=%d&workType=sx&worklevel=&datatype=gas&detectiontype=audit'%(workticketidx)
data = {
	"unCompleteStaticValueList": [{
		"downlimit": 19.5,
		"groupType": "3",
		"code": "oxygen",
		"isincludeboundary": 1,
		"name": "氧气",
		"dataStatus": 0,
		"value": "21",
		"isShow": 1,
		"upperlimit": 23.5
	}, {
		"downlimit": 0,
		"groupType": "3",
		"code": "combustible",
		"isincludeboundary": 1,
		"name": "可燃气",
		"dataStatus": 0,
		"value": "",
		"isShow": 1,
		"upperlimit": 0.5
	}, {
		"downlimit": 0,
		"groupType": "3",
		"code": "Hydrogensulfide",
		"isincludeboundary": 1,
		"name": "H2S",
		"dataStatus": 0,
		"value": "",
		"isShow": 1,
		"upperlimit": 10
	}, {
		"downlimit": 0,
		"groupType": "3",
		"code": "Carbonmonoxide",
		"isincludeboundary": 1,
		"name": "CO",
		"dataStatus": 0,
		"value": "",
		"isShow": 1,
		"upperlimit": 30
	}, {
		"downlimit": 0,
		"groupType": "3",
		"code": "Sulfurdioxide",
		"isincludeboundary": 1,
		"name": "SO2",
		"dataStatus": 0,
		"value": "",
		"isShow": 1,
		"upperlimit": 15
	}, {
		"downlimit": 0,
		"groupType": "3",
		"code": "ammonia",
		"isincludeboundary": 1,
		"name": "氨",
		"dataStatus": 0,
		"value": "",
		"isShow": 1,
		"upperlimit": 30
	}, {
		"code": "detectiontype",
		"value": ""
	}, {
		"code": "gasdetectionid",
		"value": ""
	}, {
		"code": "analysisname",
		"value": "作业地点"
	}, {
		"code": "part",
		"value": "炼油北区"
	}, {
		"code": "workticketid",
		"value": ""
	}, {
		"code": "detectiontime",
		"value": now
	}, {
		"code": "iscomplete",
		"value": ""
	}, {
		"code": "created_by",
		"value": ""
	}, {
		"code": "created_dt",
		"value": ""
	}, {
		"code": "updated_by",
		"value": ""
	}, {
		"code": "updated_dt",
		"value": ""
	}, {
		"code": "tenantid",
		"value": ""
	}, {
		"code": "remark",
		"value": ""
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
		"uuid": "1592875169587"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007468",
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
			"uuid": "1592875169587"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"name": "分析人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 2
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 131
caseinfo['name'] = '现场确认-受限空间-会签-生产单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=sx&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592875245936"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007469",
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
			"uuid": "1592875245936"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"name": "生产单位监护人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 3
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 132
caseinfo['name'] = '现场确认-受限空间-会签-施工单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=sx&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007470",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\nP1EpnI5oCXosAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "施工单位监护人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nP1EpnI5oCXosAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 4
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 133
caseinfo['name'] = '现场确认-受限空间-会签-作业人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=sx&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007471",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\njaHiMyO2fgAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "作业人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\njaHiMyO2fgAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 134
caseinfo['name'] = '现场确认-受限空间-会签-施工作业负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=sx&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007472",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "施工作业负责人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 6
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 135
caseinfo['name'] = '现场确认-受限空间-会签-技术员'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=sx&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592875345479"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007473",
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
			"uuid": "1592875345479"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 7,
		"isinputidnumber": 0,
		"name": "技术员",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 7
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#受限空间
workticketidx = workticketid+4
ts = tsi+4
worktaskidx = worktaskid+1
caseinfo['id'] = 136
caseinfo['name'] = '现场确认-受限空间-会签-二级分管负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=sx&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592875357404"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007474",
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
			"uuid": "1592875357404"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 8,
		"isinputidnumber": 0,
		"name": "二级分管负责人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 8
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 145
caseinfo['name'] = '现场确认-高处作业-属地确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&tabtype=measure&businesstype=SDQR'%(workticketidx)
data = {
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
		"uuid": "1592879233500",
		"businesstype": "SDQR"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000007487",
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
			"uuid": "1592879233500",
			"businesstype": "SDQR"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "确认人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "开展JSA风险分析，并制定相应作业程序和安全措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007227,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs01",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022212,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 146
caseinfo['name'] = '现场确认-高处作业-作业确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&tabtype=measure&businesstype=ZYDY'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "ZYDY"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007731",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "作业人员身体条件符合要求、着装符合工作要求",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007228,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs02",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022213,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业人员佩戴符合要求的安全带",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007229,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs03",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022214,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业人员携带工具袋，所用工具系有安全绳",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007230,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs04",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022215,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "使用的脚手架、吊笼、防护栏、梯子等符合要求",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007232,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs06",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022217,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "在石棉瓦等轻型材料上方作业时需铺设牢固的脚手板",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007234,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs08",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022219,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "15米以上进行高处作业配备通讯、联络工具",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007236,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs10",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022221,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "视频监控已落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007238,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs12",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022223,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 147
caseinfo['name'] = '现场确认-高处作业-双方确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&tabtype=measure&businesstype=SFQE'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "SFQE"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007732",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "signandcard",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "交叉作业已落实措施错位硬隔离要求",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007231,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs05",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022216,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "临边及洞口四周设置防护栏、警示标志或覆盖，垂直分层作业有隔离设施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007233,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs07",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022218,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "高处作业有充足的照明",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007235,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs09",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022220,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业人员佩戴：空气呼吸器（    1）过滤式呼吸器（    2）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007237,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs11",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022222,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "其它补充措施（  哈哈）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007239,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "gccs13",
		"dataStatus": 0,
		"worktype": "gc",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022224,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 148
caseinfo['name'] = '现场确认-高处作业-会签-作业人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007489",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAlZSURBVHic7d1dq61VGcfhsZUKoySJyuhEooRCrJ0S2tumzIz6Nn25lDLDUDalhSDS\nRg2UoqiDpAwSxNVhsua93Otl/seb1wXr5D66DxaTH/N5xpitAQAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAADAdF5srb3VWvvp6EUAgD2dnPr74dh1AIAdnQ6Ov4xdB/7v2ugFADiak2Lmc54p\n3DF6AQCO4hPF7O3uW8AZBAfAHr5YzN7svgWcQXAA7OH+YvZa9y3gDIIDYA9fLWa3um8BZxAcAHt4\nsJi93H0LAGBrt9rhsdivDd0IANjO6dg4aa19ZOhG8D7OZwPswR0cTM07HABAnOAAAOIEBwAQJzgA\n1uddDaYnOADW93Axc8soUxEcAOt7qJi90H0L+ACCA2B9VXC82H0L+ACCA2B91SMV33AAAEf1Xju8\nZfTjQzeCU7zZDLA+t4wyPY9UAIA4wQEAxAkOACBOcACsrXo5tHqnA4YSHABr+2Yxe6n7FnAbggNg\nbd8oZr/rvgXchuAAWNsjxexm9y0AgK292Q4v/frK0I2g4GIYgLW59IsleKQCAMQJDgAgTnAAAHGC\nA2Bdd41eAM5LcACs63vF7Lfdt4BzEBwA66qC49nuW8A5CA6Add0oZoIDADiq0xd+nTTvdTApl8MA\nrMulXyzDIxUAIE5wAABxggNgTXeOXgAuQnAArOnxYuYODqYlOADW9Fgxe7r7FgDA1n7fDo/EVhEC\nAHBp1R0c3utgWs5rA6zJHRwsxTscAECc4AAA4gQHwHruL2b/6r4FXIDgAFhPdQfHU923gAsQHADr\n+VEx+0X3LQCArf23HR6JvW/kQnA7jlABrMeRWJbjkQoAECc4AIA4wQGwlk+PXgAuQ3AArOWJYvZM\n9y3gggQHwFp+XMx+3n0LAGBrf2+HR2IfGLoRnINjVABrcSSWJXmkAgDECQ4AIE5wAKzjY6MXgMsS\nHADr+Ekxe7b7FnAJggNgHdWR2Ce7bwEAbO2Ndngk9vrQjeCcHKUCWIcjsSzLIxUAIE5wAABxggMA\niBMcAGu4Ucxe6r4FXJLgAFjD48Xsl923AAC2drMdHol9YuhGAMB2TsfGSWvtzqEbwQU4vw2wBndw\nsDTvcAAAcYIDAIgTHADz+1wxe6f7FnAFggNgfj8oZr/qvgVcgeAAmN9jxezp7lsAAFv7U/Oz9CzO\nkSqA+TkSy/I8UgEA4gQHABAnOACAOMEBMLf7ipk7OFiO4ACY2/eL2ZPdt4ArEhwAc7tRzH7dewkA\nYG/u4GALznEDzM0dHGzBIxUAIE5wAABxggMAiBMcAPO6p5i9230LOALBATCv7xaz33TfAo5AcADM\n6zvFTHCwJMEBMK8qOJ7rvgUAsLX32uGlX3cN3QguyeUxAPNy6Rfb8EgFAIgTHABAnOAAAOIEB8Cc\nHihmb3TfAo5EcADM6VvFzJFYliU4AOb07WL2fPctAICtvdoO7+C4PnQjuALnuQHm5A4OtuKRCgAQ\nJzgAgDjBAQDECQ6A+XhXg+0IDoD5PFTMbnXfAo5IcADM55FidrP7FnBEggNgPo8WM8EBABzV6+3w\n0q+vD90IrsiLSQDzcekX2/FIBQCIExwAQJzgAADiBAcAECc4AOZyTzF7t/sWcGSCA2Au14vZC923\ngCMTHABzqYLjD923gCMTHABzERwAQNwr7fCW0YeHbgRH4OY6gLlUt4zeccYcluGRCsD8xAbLExwA\nQJzgAADiBAcAECc4AObhRX62JTgA5vFgMXu9+xYQIDgA5lEFh0u/2ILgAJjHl4vZH7tvAQGCA2Ae\nXypmr3bfAgIEB8A8qm84BAcAcFRvtcPfUfnM0I3gSBzBAphHdYW5z2m24JEKABAnOACAOMEBAMQJ\nDgAgTnAAAHGCAwCIExwAc/hsMftn9y0gRHAAzMEto2xNcADMofodlde6bwEhggNgDr7hYGuCA2AO\ngoOtCQ6AOXyhmP25+xYQIjgA5vD5Yva37lsAAFv7Tzv8afq7h24ER+RnjwHm4Kfp2ZpHKgBAnOAA\nAOIEBwAQJzgAgDjBAQDECQ4AIE5wAABxggMAiBMcAECc4AAYz2cx2/NPDjDevcXsr923gCDBATCe\n4GB7ggNgvE8Vs3903wKCBAfAeJ8sZv/uvgUECQ6A8QQH2xMcAONVwfF29y0gSHAAjOcbDrYnOADG\nExxsT3AAjHd3MRMcbEVwAIznHQ62JzgAxvNIhe0JDoDxBAfbExwA43mkwvYEB8B4vuFge4IDYDzB\nwfYEB8B4HqkAAHHvtNZOTv19dOhGcGTXRi8AQDspZj6f2YpHKgBAnOAAAOIEBwAQJzgAgDjBAQDE\nCQ4AIE5wAABxggMAiBMcAECc4AAA4gQHABAnOACAOMEBAMQJDgAgTnAAAHGCAwCIExwAQJzgAADi\nBAcAECc4AIA4wQEAxAkOACBOcAAAcYIDAIgTHABAnOAAAOIEBwAQJzgAgDjBAQDECQ4AIE5wAABx\nggMAiBMcAECc4AAA4gQHABAnOACAOMEBAMQJDgAgTnAAAHGCAwCIExwAQJzgAADiBAcAECc4AIA4\nwQEAxAkOACBOcAAAcYIDAIgTHABAnOAAGOva6AWgB8EBMJbg4ENBcACMJTj4UPCPDjDeSTHz+cxW\nfMMBAMQJDgAgTnAAAHGCAwCIExwAQJzgAADiBAcAECc4AIA4wQEAxAkOACBOcAAAcYIDAIgTHABA\nnOAAAOIEBwAQJzgAgDjBAQDECQ4AIE5wAMznqdELAAD7+Vlr7eR9fwAAAAAAAAAAAAAAAAAAAAAA\nAAAAADCh/wF/wNyQYq9xcAAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "作业人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nAAAAADCh/wF/wNyQYq9xcAAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 3
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 149
caseinfo['name'] = '现场确认-高处作业-会签-施工单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007490",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAmXSURBVHic7d1tqGVVHQbwZyaTphdsAsEiK5GQohyYCCaqDykjYjVTRuRbSUEWhYla\nFGVQkWUFNgQpghBFYKRUFGh9KJLJog9jYQyVTNBIDAlqJOL40tzpw23iMnvtO/eee/ZeZ6/5/WB/\nOXcz9zkMl/XwX+vskwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABM3FVJ7kjy6tpBAID2fCPJ0eOuP1ZNBAA0Y3OS\nZ9MtG8eubfWiAQAteEP6i8ax62C1dADA5F2eE5eNYxcAwLq9L2svGwoHALBuO7O+sqFwAADrcm5O\nfFZD4QAAZvaa9JeNvSvuUzgAgJmsNtlY+ayNqws//+uoSQGASdqd/rLx0HH3Pl245+LRkgIAk/Sl\n9JeNvxfut50CAKzLapONA4X7P95zLwBAr0dSLhAP9NxfuveG4WMCAFN2b7oF4tc9924p3Gu6AQCs\nycry8O1V7vtDumXjicHTAQAnldJ047VVEwEATflcbKcAAAMrlY2bqiYCAJrS97hzAIC5eSrdsvG3\nqokAgKZsTnm68fyaoQCAttyXbtlYqpoIAGhOabpxftVEAEBTbo7DogDAwEpl4ytVEwEATbk8phsA\nwMBKZeM3VRMBAE3ZHtMNAGBgR9ItG49VTQQANGVrytONrTVDAQBteSzdsnGkaiIAoCl9jzF/Xc1Q\nAEBb9sdhUQBgQJtSLhuX1gwFALTFdAMAGFypbHysaiIAoCn3x3QDABhYqWxcUzURANCUB2K6AQAM\nqO+5G5+sGQoAaMuBmG4AAAN6bspl49qaoQCAtjwa0w0AYECnpVw2LqsZCgBoy+GYbgAAAzor5bJx\nfs1QwMllU+0AwOD6Jhn+/oHRbK4dABjUW3peP2fUFABA00pbKYerJgIAmnJFyoXjtJqhAIC2lMrG\nP6omAgCa8p6UC4dzWwDA3JTKxv6qiQCAplwQ0w0AYGClsnGwaiIAoCk7Ui4cp9QMBQC05Zl0y8ah\nqokAgOaUphtbqiYCAJpya7plY6lqIgCgOaXpxmVVEwEATXllyoUDAGBuDqVbNvZVTQQANMeXtAEA\ng9od2ykAwMBKz97YUzURwHE21Q4AbFhpmuFvG1govswJpu2a2gEAgPaVzm5cVzURQIGxK0yb7RRg\nEmypwHTdXnjt2dFTAABNK22n7KqaCABoyunx7A0AYGC/T7dsPFg1EQDQnNJ042VVEwEATdke2ykA\nwMAeTrds3F01EQDQnNJ043lVEwEATbkotlMAgIE9km7ZuK1qIgCgOaXpxnOqJgJYA482h+l4Vc/r\nR8YMAQC0bW+6040fV00EADSntJ3yoqqJANbI11jDdPgqemCynOGAafhC4bVDY4cAANq2lO52yjuq\nJgJYB+NYmAbbKcCk2VKBxbe9dgAAoH33pLudckvVRABAc0ofh31x1UQA62QPGBaf8xvA5DnDAYvt\nwsJrvh0WAJirfelup3ytaiIAoDml8xsvqJoIYAb2gWGxOb8BNMEZDlhc5xVeWxo9BQDQtF+mu52y\np2oiAKA5pfMbL6maCGBG9oJhcTm/ATTDGQ5YTOfUDgAAtO+2dLdTflg1EQDQnNL5jR1VEzGEC5N8\nPp6tAkAlpcLBtO1K8rOU/2+PpvwxaAAYlMIxbTuT/CT95aLvAoDR7Ep3Ifpn1USs5o1JvpP1lwuF\nA4Cq7kx3IbqxaiJWuijJbzOfgrHy+sCYbwIASouRj8nW864kf8r8C8ax6854oBsAFRi11/XylKdM\nG73+nOSzSc4c760AQD+FY3wfTPLvzK9cPJjk2iRbxnwTALAeCsfwTk1yS+ZXMG5Pcsao7wAANmBb\nuovZw1UTtePsJPdlPgXj1iSnjxsfAObnI+kubndVTTRt5yV5KPOZYGwdOTsADGZPuovddVUTTc/F\nSR7PxgrGX5JcMHZwABjLd9Nd/K6smmgaPpTk6WysZOzJ8tkOAGjeT9NdCN9ZNdHiuj7JUmYvGI8m\nuWT01ACwAPamuzC+uWqixfLhJEcye8n4VZKzRk8NAAvm5+kukjurJqpvd5LDmb1kfGv8yACw2L6f\n7oJ5adVEdexIciizl4wvjx8ZAKaj9CmVT1RNNJ5tSQ5ktoKxlOUzHQDAGlyZ7mL6i6qJhnV2kv2Z\nrWT8J8lHx48MANN3asqLa0tekWRfZp9kXD1+ZABoT4uF49zM/hXvS/HwMwCYu9Kie1XVRLN5a5KD\nmf3g56fHjwwAJ4+bM90px9uT/Cuzl4wvjh8ZAE5epcX4YNVE/a7P8gHOWUvGTeNHBgCS/k9u3F0z\n1P+ckeSOzF4wjmZ5igMALIC+xfqZkXOckuSGJE+tkknJAICJelNWX8B/NNDvPTPL2xxPnOD3KxkA\n0IhPZW0L+5NJvp5k+zr+7dcn+UySe9f4O9Z6fXXG9woAVPTezLcQzPt6PMkVg717AGA0L0z9YrHy\nuivJSwd9xwBANTemTsG4P8m7R3h/AMACeX+Wz20MUS6OJPlelg+tAgD839uSfDPJ77L2YvFkkh8k\nuaRCXgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAIb0X/gTINviwzEUAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "施工单位监护人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 4
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 150
caseinfo['name'] = '现场确认-高处作业-会签-生产单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592879499478"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007491",
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
			"uuid": "1592879499478"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"name": "生产单位监护人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 151
caseinfo['name'] = '现场确认-高处作业-会签-施工单位负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007492",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAA6HSURBVHic7d19zGRXXQfw7253CQVjbaltWikqUCA1jUVdjagkNaYI7V9YEMVoBYsv\nJGJJjRhFbQ0aJWoiqWJMKkrakCgviiEGs5QqVqCoWKG2UrCUVgnQYhVb2LfHP56u1uee2e7MM/f8\nZu58PslNmpPtPt+5d3fOd8+5cycBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAABgibYedVxZnAUAmKCb8v8Lx1ZtHJiGPdUBAFZMq2B4r4Rd2lsdAGCF\nnFYdAACYvvdkuJ3y4dJEAMDk7CwbW0meWpoIAJiUS9MuHAAAS3M0w7JxQ2kiAGBS9qa9uuHTKbAk\nPqUCkPxFY+xIbKkAAEvUWt24uDQRADApV8bNogDAyFpl4w9LEwEAk/IVsboBAIzsIxmWjf8uTQQA\nTE5rdePC0kQAwKS8LLZTAICRuVkUOvIUPWAT7UlybMY4MAJPGgU20Y2NMdspAMBStbZTXlKaCACY\nlK+Nm0UBgJHdl2HZ+ERpIgBgclqrG+eWJgIAJuV7YjsFABjZoQzLxltKE8GG8JlzYJO0VjNOSfuZ\nHMASeQ4HsCleM2Nc2QAAlqZ178ZrSxPBBrGlAmyK1naK90DoxJYKsAne0Bg72j0FADBpre2UF5cm\nAgAmZX88ewMAGNlbMiwb95UmAgAmp7W68S2liQCASTk9tlMAgJEdzLBs3FWaCACYnNbqxtNKEwEA\nk3JebKcAACO7LcOy8deliQCAyWmtbpxemggAmJQDsZ0CAIzs0xmWjXeUJgIAJqe1uvH40kQAwKS8\nILZTAFhzR/N/E9gVtVGY4eEMy8b1pYkAYA7vjH81r4PW6sYppYkAYA6W6VffD8V1AmDNmchW35EM\nr9HrSxMBSZI91QFgjbQKhr9Dq8U1ghW1tzoArIkfaIzd3TsEJ3R1dQAA2K1/zHCp/lWlidipteX1\ns6WJgP9lqRFOTmupfn+27xlgNdhOgRVmSwUWp2ysjl9rjLmpF4C18t0ZLtUfLk3ETq3tlFeUJgKA\nOR3McDK7pjQRj3ZKfGQZgAnwRWCr7foMr8+h0kQAsAD/el5tretzeWkiAJjT/igcq+zxcX1gLfiU\nCpzY9zfG3ts7BDP9cWPs891TAMAuvTs+/bDKWqsbF5cmAoAFtCa0J5Qm4rizYzsFgIkwoa2u92d4\nbe4pTQQAC1I4Vlfr2nx9aSIAWJDCsZrOi2sDwEScHo80X1Wt7ZTbShMBwIKen+GkdnNpIo5rrW48\nvTQRcEKewwGzfWtj7APdU7DT2TPG7+qaApiLwgGzPbsxdmv3FOzUetiXsgHA2ro3w2X7Z5QmIvHp\nFAAmxqcgVk/rRl7XBYC1ZmJbPQfjYV8ATIzCsXpa1+RAaSIA2CWFY7U8Lq4JrC2fUgHWxRsaY/d3\nTwEAS+Zf06uldT1eWJoIAHbp/Awnt3tLE6EAwhqzpQJtX9cY+2j3FBz3E9UBgN1ROKDtgsbY7d1T\ncNxvNcZ+qXcIAFi2GzJcvr+yNNFms50Ca84KB7S1VjhsqdT4tuoAADCWL2X4L+ozShNtrn/K8Fq8\ntTQRACyJJfzV0boWTypNBMxtT3UAWFGtguHvS397khybMQ6sEfdwAKvsmsbYZ7unAICR2FJZDccy\nvA4vLU0ELMSyJLTZUlkNrgNMhC0VYFVdVB0AAMZmS6XeezO8Bm+rDAQAy6Zw1GtdgyeXJgIWZi8U\n2tw7UM81gAlxDwcM7W+MHe6eYrO9sjH2pe4pAGBE52S4lP9vpYk2z+czvAavLk0EAEt2YYaT3W2l\niTaPe2hgYmypwNCZjbHPdU+xudynAROkcMDQqY2xh7qn2Fw/3Rj7TPcUADCyb8pwOf+DpYk2yxcz\nPP8vK00EACN4SoYT3r+WJtos7t9Y3GXZvsH5b6uDAPDYTs1wwrOl0se+KByL+PU4bwBryZt3jWsz\nPO93lCZaXfuSfCDtP6v+zAKsCW/eNQ5neN5fVJpo9TwrycM5cdHwZxZgTXjzruG8z/ajObmScfz4\nhZqYAMzDxFfDeR96a+YrGm+uiQnAIkx8/f14huf846WJ6pyX5P7MVzSuKkkKwK4oHP19IsNz/mOl\nifp7beYrGVtJnluSFIClUDj6a53zTXga8hlJ7sp8JeOzSZ5UERaA5VI4+tu0c/6azL+a8Z6SpACM\n5j8zfLM/qzTRtH1Hhuf7aGmicRxI8kDmLxpXV4QFYHw3Z/im/7zSRNP2Zxme7+tKEy3PE5O8K/OX\njC8keWZBXgA6en2GE8CvliaattaE+zWVgXZpT5I3Zv6SsZXkDwryAlDkeRlOBLeWJpq2qdy/cU0W\nKxkPJXlOQV4AivkSsX5aX5a3Tuf6F7NYydhK8hsFeQFYMes8Ca6Tn8zwPN9SmuixLfK8jOPHR5Kc\n2T8yAKtK4ejjwxme55eXJmr7uSxeMh5IcnH/yACsg9bEcUppomlqnef9pYm27UnyuixeMo4k+cHu\nqQFYOx/KcBL53tJE07RKK0lnJHn7jEwncxxL8lPdUwOw1q7KcEJ5e2miaaouHN+e5I4ZOU62ZLy6\nc2YAJuTs1E+GU/d9GZ7fOzv83Fckebjxs+c5PP0TgKVROMb1lxme358Z4ec8McnvNn7WvMcY2QCg\nOemcWppoWlrn97Ql/d6XJ7l3xs842eNwklctKQ8AzHRLhpPQ75cmmpZlriCdleSGGb/nPMen4ntz\nAOjsu2JbZUy7PbdXZ/f3YmwlOZjkq3b3UgBgd1oTlOdx7N43Z3he/+Mx/p8XpP2gsEWO67Iaz/sA\ngCTJ/RlOVu8sTTQNv5LheX3jjl9zYZI/b/y6RY77k1wx4usBgF25JLZVxnB7huf0pUne1Bhf9Pij\nbD/MCwDWQmsyu6M00fpbVqnYeU0u7fkiAGCZWg+o2kryDZWh1tBZ2b534liWUzCOZPvr4ff2fBEA\nMKZZkx6zXZDlfFT10ccNSc7t+SIAoKcXpz0BPlAZasU8J8m7styCcUuS5/Z8EQBQ7d/TnhRvqgxV\n6NK0H462m+PvklzW80UAwCqaNVHeWBmqg9OT/HKSBzPODZ+v7PdSAGD1PSWzJ83rCnMt2+VJ/irL\nLxbvmzH+5D4vCwDWx2WZPaF+rDDXop6a5LeTHMryC8afZvupoo/W+nUAQMMVOfFE+51lyU7sadne\nGrkn42yNvCnJ+Y+RQeEAgDlcm8eegK8tS7f9rac3zsi1rOM3M//TPBUOAJjTy3Pyk/P1SS5a4s8+\nLcmLkvxeko/PkWPR4+YkL9xl5nMav++xXf6eALARzs3uJ/O7k7w/ya2P/PcXlvB77ub4TJKfT/Jl\nSztL217S+FnvW/LPAIBJuym1JWHR41iSNyc5sPxTMvA7jZ//ug4/FwAm5+9TXyJmHV/M9tZO1dM7\nP9rIdElRFgCYhB9JXbF4KMmfJPnhbH9p2qpoZd1XmggAJuT5Sd6d5ReLg0muSvKMfi9lV1qvAZi4\nPdUBgCTbHys985HjaJLPPXI8WBlqJK2C4b0IJs5fcqA3hQM20N7qAMBGObU6AFBD4QB62vmdKsn2\np1aAiVM4gJ5aheOD3VMA3SkcQE8KBwAwuk9m+JHYbyxNBHThznCgp9YnVPbOGAcmxJYKUE3ZgA2g\ncAAAo1M4AIDRKRwAwOgUDqCX1jfWHumeAiihcAC9PLsx9qHuKYASCgfQS6tw/EP3FEAJhQPo5aLG\nmMIBACzVnRk+ZfRAaSIAYHJ2lo2tJPtKEwHdeLQ50EvriaLeg2BDuIcDABidwgEAjE7hAABGp3AA\nAKNTOIAevrIxdrh7CqCMwgH0cEFj7LbuKYAyCgfQQ6tw3N49BVBG4QB6eFZj7J+7pwDKKBxAD89s\njN3ZPQVQRuEAelA4YMN5rDDQQ+ux5ntnjAMTZIUDqKJswAZROACA0SkcAMDoFA4AYHQKBwAwOoUD\nABidwgEAjE7hAABGp3AAAKNTOICxPa4xdqh7CqCUwgGM7csbYw92TwGUUjiAsZ3WGFM4YMMoHMDY\nrHAACgcwOt9KDSgcwOiONMb2d08BlFI4gLEpHIDCAYyuVTj2dU8BlFI4gLFZ4QAUDmB0VjgAhQMY\n3eHGmBUOAGCpnpBka8fxcGkioDufjwd62GqMef+BDWJLBQAYncIBAIxO4QAARqdwAACjUzgAgNEp\nHADA6BQOAGB0CgcAMDqFAwAYncIBAIxO4QB6+HRj7JzuKYAyCgfQwycbY1/dPQVQRuEAerinMaZw\nwAZROIAe7m6MKRywQRQOoIe7GmPnd08BlFE4gB4+1hhTOACApTovydaO477SREBXe6oDABtjqzHm\nPQg2hC0VAGB0CgcAMDqFAwAYncIBAIxO4QAARqdwAACjUziAXg41xk7tngIooXAAvfxLY8zTRmFD\nKBxAL63vU3l69xRACYUD6MX3qcAGUziAXqxwwAZTOIBerHAAAKPzjbGwwaxwAL18qjoAALAZdq5w\nXFwbBwCYqr9J8l9JLqkOAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAACvufwBugHkQvoyxdAAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "施工单位负责人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 6
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 152
caseinfo['name'] = '现场确认-高处作业-会签-基层现场负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592879517040"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007493",
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
			"uuid": "1592879517040"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"name": "基层现场负责人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 7
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#高处作业
workticketidx = workticketid+7
ts = tsi+7
worktaskidx = worktaskid+1
caseinfo['id'] = 153
caseinfo['name'] = '现场确认-高处作业-会签-基层领导'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=gc&worklevel=gb_gc_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592879526711"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007494",
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
			"uuid": "1592879526711"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 8,
		"isinputidnumber": 0,
		"name": "基层领导",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 8
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 155
caseinfo['name'] = '现场确认-起重作业-属地确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&tabtype=measure&businesstype=SDQR'%(workticketidx)
data = {
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
		"uuid": "1592879747983",
		"businesstype": "SDQR"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000007497",
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
			"uuid": "1592879747983",
			"businesstype": "SDQR"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "确认人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "开展JSA风险分析，并制定相应作业程序和安全措施。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007217,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs1",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022196,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业前按规定进行安全技术交底，作业人员应穿戴合格的劳保用品。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007225,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs8",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022204,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#起重作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 156
caseinfo['name'] = '现场确认-起重作业-作业确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&tabtype=measure&businesstype=ZYDY'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "ZYDY"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007733",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\niPajSQAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAA9QSURBVHic7d1trGVVfQbwZ2AAZ0B5KeXFig1SlNL0JSYF0mrBl2jpG5E2tU1sqwhW\nW9Ea8UNrxDS1aWwiTWoEtTThgw1a9YMtRdqkWKqWptG2SUsbUgxEQaFNmEFghhGY2w+TSZCz9p25\nc8/e/3PX/v2S82VNOOc5K+Gu56y1zz4JAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCQtWc8fqM4CwDQob357sKx\nVhsHAOjNDVksGwoHALA0L0i7bCgcAMDSDJWNkypDAQD9+EbaZeP9laEAgH5cmXbZ2FUZCgDox/a4\nbgMAGNlQ2Ti/MhQA0I9b0i4bt1SGAgD6cXbaZWN/ZSgAoC9DRynbK0MBAP34Vtpl402VoQCAflyV\ndtn4emUoAKAfvgILAIxuf9pl46zKUABAP4a+AntTYSYAoCMvTrtsPFkZCjgy26oDAAwYukbjqHX+\nDVhRR1UHAGj41sD4z0XZAACW4DfTPkq5uzIUANCPY+MrsADAyIa+AntqZSgAoB/Xp102rqsMBQD0\n43lpl429laGA5fG1WGAVDF2j4W8UdMLXYoFqtw2M//qkKQCAbp2Z9lHKw5WhgOWzXQlUcpQCM+FI\nBahy88D4KyZNAQB0a0faRyn3VIYCxmPbEqjwVJKjG+P+JkGnHKkAU3tb2mXjDVMHAQD61TpK2Vea\nCADoyv1pF47tlaEAgH6clXbZ+EhlKGAaLtACpuKeGzBjLhoFpnD1wPgLJ00BAHStdZTyzdJEAEBX\nvpR24QAAWIrj0i4bH6sMBQD05YnY3QAARnRR2mXjJytDAQB9aZWN75QmAgC6cnXahWNnZSgAoC+t\nsnF3aSIAoCs3xYWiAMDIWmXjU6WJAICu3BW7GwDAiIZu8nVtZSgAoC+7Y3cDABjRiWmXjcsrQwEA\nfdkTuxsAwIjOSLtsXFAZCgDoy77Y3QAARnRW2mXjvMpQAEBfns5i2Xi6NBEA0JXz0t7dOKsyFADQ\nl1bZ2FeaCADoyrlpF44zKkMBAH1pXbuxtzQRANCVM9Pe3Ti1MhQA0JfWXUWfLE0EAHTlhLR3N86t\nDAUA9GVXFsvG/tJEAEBXjk17d+OllaEAgL7cF7+ZAgCMrFU2Li1NBAB05dbY3QAARtYqG2+sDAQA\n9OUDsbsBAIysVTY+XJoIAOjK5bG7AQCMrFU2vlyaCADoytlpF46jKkMBAH15PItl4+HSRABAd1q7\nG6eVJgIAuvLZuFgUABhZq2z8amkiAKArvxK7GwDAyFpl47OliQCAruyM3Q0AYGT3ZLFsPF6aCADo\nTmt34/zSRABAV34njlMAgJG1ysa1pYkAgK4cE7sbAMDIPp/FsvFYaSIAoDut3Y0LSxMBAF15WRyn\nAAAjeyyLZeOvSxMBAN1p7W4cU5oIAOjKO+I4BQAY2f4slo3fLk0EdGlbdQCgVGs3w98FYOmOqg4A\nlLmiOgAA0L99WTxOuaY0EdAtW6cwX45TgMk4UoF5+uXqAABA//Zk8TjlD0oTAV2zfQrz5DgFmJQj\nFZifk6oDAAD9+0gWj1PuLE0EAHSndSvzi0sTAd1zZgvz4/oNYHKu4YB5eXF1AACgf5/O4nHKp0oT\nAQDdaV2/8cLSRMAsOLeFeXH9BlDCNRwAwOgUDpiPVzbGHpk8BTBLCgfMx5sbYx+dPAUA0LXWBaPn\nlCYCZsPFYjAfLhgFyjhSAQBGp3AAAKNTOGAefqIxdvfkKYDZUjhgHl7VGLt98hTAbCkcMA+te3D8\n/eQpAICutb4Se3JpImBWfCUO5sFXYoFSjlQAgNEpHADA6BQOAGB0CgcAMDqFA/p3SmPssclTALOm\ncED/zm+M/dfkKYBZUzigf2c0xu6ZPAUwawoH9K91g69dk6cAZk3hgP61ruHYPXkKYNYUDuhfa4dD\n4QAmpXBA/+xwAOUUDuifHQ6gnMIB/Tu+MbZn8hTArCkc0L+9jbEdk6cAZk3hgP61djN2Tp4CmDWF\nA/rXKhx2OIBJKRzQP0cqQDmFA/rnSAUop3BA/1q/DNv6qizAaBQO6N+9jbFzJk8BzJrCAf37WmNM\n4QAAlurUJGvPejxamgiYnW3VAYBJrDXG/P8PTMaRCgAwOoUDABidwgEAjE7hAABGp3DAPDzVGPu+\nyVMAs6VwwDzc0Rh7+eQpgNlSOGAe/rEx9lOTpwAAunZJFm/+dXdloA16Uw6Upj1ZfB/Pftyb5E+S\nvLYkKQDMXGtxXlU/ngPF4VDlYiOPv0vysinfBADM0VYoHJ/IckvGeo/fn+g9AcCsrGrhOD2Hd1Qy\n5uO3Rn+XADATD2Vxoa08Yjg9yd5GpsrHw0lOHPNNw1z5lgrMx82NsddPniLZmQOL+4NJnrOB/+5P\nk1yYAz86t97jsiR/kQNlZqNOTrI7yeNJTjmC/x4AZu+iLH6i//bEGX6vkWHo8aElvu5pSa7bwGsf\nfOxZYgYAmI3K6zgeHnj9Zz7+N8nZE2S5OMmuw8hz8PFXE2QCgG5UFY5DLegPJjl2oizPdkWS/YeR\ncS01R1AAsOU8ksVF9LKRX3O9BXx3khNGfv3D9cIk+3Lo0rGrKiAAbBXvy+IC+sURX2+9hftdI77u\nZnxvDlzbcqji8dNVAQFg1e3IdMcq6y3WVccnG3FBDl06vlaWDgBW3BSFY70LRLeaG3Po4nFmWToA\nWFGtBfM1S3z+2wZeYyuWjYOOTvJk1i8dbylLBwArqHU/in9f0nO/uvHcW71sPNMNWb90fKUuGgCs\nluMyTiE4euB515KcuoTnXxXfk/VLx766aACwWsYoHEM/wPbaJTz3Krov6xePbWXJAGBFtO6y+c5N\nPmdr0f38Jp9z1f1x1i8dx9VFA4B6b8ni4vjYJp+zVWLm4Ieyfuk4qS4aANQb41jl4Ndhj+SXWre6\n9UrHFL8PAwAryafx5Xs6w6XjuYW5AKDMnVlcFG8oTdSHoYtn15IcVZgLAEq8PP3eL6Na63oW8wvA\nbFkQxzP0A3BPVYYCgAqtBfHVpYn6MnRNx12VoQBgan+WxcXwgdJE/Rk6WrmqMhQATOnYOFYZ23q3\nfPfNFQBmo7UQPr80UX/W+/0VAJiFL2VxEfzb0kR9enfaheP+ylAAMJXz4pP3VO5Le64vqYsE0/Br\nhkDSLhjbc+BbFizXUJnz95iuuesdkCSPNMaumzzFPOwcGP+nSVMAQIHL41hlSjenPd9nVIaCMdnC\nAw5qFQx/I8bjaIVZcaQCrOdt1QE69qKB8ddNmgIAJvbeOFaZ2l0x5wDMkMVveq05f0dpIgAYWWvx\ne2tpov59LooeADPzwSwufPtLE81Dq3C8vzQRAIzMp+3pXR/zDsDMtBa+a0oTzUNr3i8sTQQAI3pf\nfNqucFsW5/zJ0kQAMLJW4TimNFH/tqU979srQwHAmL6TxYXv1tJE8/B4Fuf9HyoDAcCYLo1jlQrn\nxLwDMDOthe9VpYnmoTXvP1CaCABG9IW4iLHCp7M47/9TmggARvScuIixwo44VgFgZloL37+WJpqH\n1rxfXJoIAEb08/Fpu8Jnsjjn/1maCABG1ioc15Um6t/xUfQAmJkPxeJXwZwDMDutxe89pYn6tyvm\nHICZuTM+cU/tzVmc7ydKEwHABFqF492lifqn5AEwO1+OBXBq5huAWWotgDeWJurbQ1mc79eXJgKA\nCdwen7qn9LtZnOs7ShMBwERaheOB0kT9cptzAGbr2rQXwedXhuqYwkEXtlUHALakoUXP35Tla821\neWbLOao6ALAlvXRg/IpJU8yXX+wFYDYeie3+KbRuuvazpYngCNjhAI7UqQPjn5s0Rf/ubIxdNHkK\n2CSFAzhST6b9Fc1fSHLixFl69mBj7JTJU8AmKRzAZlwyML57yhCde6gxdvLkKWCTFA5gs94+MP7n\nk6bo1zcbYydNngIAVsC+tC8gPaEyVCfemsV5/WRpIjgCdjiAZdg5MP7opCn69MONsfsnTwGbpHAA\ny/B0kvcM/NtHpwzSoR9pjCkcAMzanjhaWbbdcR8OAPgu29IuHG4IduRac7mjNBEArIB3pr1IXl8Z\nagtT3gBgwNDRygsqQ21RCgcADHC0shznxhwCwLremPZi+X+FmbaaG7M4f/9SmggAVtC9aZeOD1SG\n2kJac3dlaSIAWFFDRyvnVYbaIhynAMBhOimu5zhS5gwANuBdUTo26hNZnKv/Lk0EAFvAV9MuHA9X\nhlphrbl6ZWkiANginkp7If1qZagVdErsBgHApgwdrdxUmGnVPJjF+flGaSIA2GJOz3Dp8HXZA1pz\n86LSRACwBV2Q4dJxTWGuVfDFOE4BgKW5KsOl4+rCXNXMBwAs2YczXDr+sjBXlUdjdwMARvHxDJeO\newpzTe2X0p6Dt1eGAoCefDLDpWMtyfa6aJPYETdGA4BJXJ/1S8elddFGN/Sez6wMBQC9uizrl45/\nq4s2mqH3eltlKADo3fdn/dKxluQVZemW53kZfn97CnMBwKzsy/qlY3eSnWXpNufqrP/eAIAJfSaH\n3u34elm6jTszh34/AECBH8yhF+m1JA8kOaEo46G8JMM/XPfMx7aqgADAAbfk8IrHviSvKcr4bO/N\n4WV+rCogALDouUn25vAW8bUkt2b6e3j84QbyrSX52MT5AIDD9GPZ2KK+luT2JGcvOcfJSf4oB75V\nstE8a0mOX3IeAGAEV+bIFvq1JHckuSLJWYf5Wj+a5Lokuzbxmgcf5x3xOwYAylyczZeAsR+Px51D\nAaALpyX5j9SXi4OPJ5L82qjvGAAo9brUlIxvJ3nDBO8PAFgxL0nyNxmnYPxzkl+c7q0AAFvJzyT5\nYJKv5PDLxRfiiAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOjM/wOmC/vo\niPajSQAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "补充措施：（  哈哈）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007218,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs10",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022197,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "起重操作人员、指挥人员、司索人员持有有效资质证书；指挥人员应佩戴鲜明标志，并按规定的联络信号统一指挥；作业人员应坚守岗位。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007219,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs2",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022198,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "起重指挥人员必须按规定的指挥信号进行指挥，操作人员应清楚吊装方案和指挥信号。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007220,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs3",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022199,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "起重指挥人员应严格执行吊装方案，发现问题及时与编制人协商解决。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007221,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs4",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022200,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "正式起吊前应进行试吊，检查全部机具、地锚受力情况；发现问题应先将工件放回地面，待故障排除后重新试吊；确认一切正常后，方可正式吊装。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007222,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs5",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022201,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "吊装过程中出现故障，起重操作人员应立即向指挥人员报告；没有指挥令，任何人不得擅自离开岗位。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007223,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs6",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022202,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "起吊重物就位前，不得解开吊装索具。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007224,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs7",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022203,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#起重作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 157
caseinfo['name'] = '现场确认-起重作业-双方确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&tabtype=measure&businesstype=SFQE'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "SFQE"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007734",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n3fDbq7cAAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "signandcard",
		"specialworktype": "",
		"value": "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\n3fDbq7cAAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "作业现场应实行视频监控，设定警戒区，禁止无关人员进入警戒区域。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007226,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "qzcs9",
		"dataStatus": 0,
		"worktype": "dz",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022205,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#吊装作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 158
caseinfo['name'] = '现场确认-起重作业-会签-申请人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592879985430"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007535",
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
			"uuid": "1592879985430"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "申请人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 2
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#吊装作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 159
caseinfo['name'] = '现场确认-起重作业-会签-起重操作人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007498",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "起重操作人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 3
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#吊装作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 160
caseinfo['name'] = '现场确认-起重作业-会签-起重指挥、司索人员'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007499",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\n3fwv5jeXhr3q/qAAAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "起重指挥、司索人员",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n3fwv5jeXhr3q/qAAAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 4
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#吊装作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 161
caseinfo['name'] = '现场确认-起重作业-会签-施工单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007501",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\ngg==\n",
			"uuid": ""
		}],
		"name": "施工单位监护人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\ngg==\n",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#起重作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 162
caseinfo['name'] = '现场确认-起重作业-会签-所属单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592880016265"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007500",
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
			"uuid": "1592880016265"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 1,
		"name": "所属单位监护人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#起重作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 163
caseinfo['name'] = '现场确认-起重作业-会签-施工单位负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007502",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "施工单位负责人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 6
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#起重作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 164
caseinfo['name'] = '现场确认-起重作业-会签-基层现场负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592880031092"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007503",
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
			"uuid": "1592880031092"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "基层现场负责人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 7
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#起重作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 165
caseinfo['name'] = '现场确认-起重作业-会签-基层领导'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592880039767"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007534",
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
			"uuid": "1592880039767"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"name": "基层领导",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 8
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#起重作业
workticketidx = workticketid+6
ts = tsi+6
worktaskidx = worktaskid+1
caseinfo['id'] = 166
caseinfo['name'] = '现场确认-起重作业-会签-二级单位领导'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dz&worklevel=gb_dz_workLevel01&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592880046912"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007505",
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
			"uuid": "1592880046912"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"name": "二级单位领导",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 9
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#盲板抽堵
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 167
caseinfo['name'] = '现场确认-盲板抽堵-属地确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=mbcd&tabtype=measure&businesstype=SDQR'%(workticketidx)
data =  {
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
		"uuid": "1592875788897",
		"businesstype": "SDQR"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000007477",
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
			"uuid": "1592875788897",
			"businesstype": "SDQR"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "确认人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "已开展JSA等风险分析，并制定相应作业程序和安全措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007186,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs01",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022177,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已关闭盲板抽堵作业点上下游阀门",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007187,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs02",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022178,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "盲板抽堵作业点介质已排放、泄压、置换",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007188,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs03",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022179,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已向作业人员书面作业交底与培训",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007191,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs06",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022182,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "相关岗位已知晓作业",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007197,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs12",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022188,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "视频监控措施已落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007198,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs13",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022189,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "甲方监护人持证全程监护",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007200,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs15",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022191,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "盲板按编号挂牌",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007201,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs16",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022192,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "同一管道上未同时进行两处或两处以上的作业",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007202,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs17",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022193,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 168
caseinfo['name'] = '现场确认-盲板抽堵-作业确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=mbcd&tabtype=measure&businesstype=ZYDY'%(workticketidx)
data =  {
	"mainAttributeVO": {
		"businesstype": "ZYDY"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007729",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "对于有毒介质，佩戴正压式空气呼吸器，并检查备用呼吸器状况良好",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007189,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs04",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022180,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业现场通风畅通",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007190,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs05",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022181,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "距作业点30米内不得有物料排放、采样、动火等作业",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007192,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs07",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022183,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业人员持证上岗",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007195,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs10",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022186,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 169
caseinfo['name'] = '现场确认-盲板抽堵-双方确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=mbcd&tabtype=measure&businesstype=SFQE'%(workticketidx)
data =  {
	"mainAttributeVO": {
		"businesstype": "SFQE"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007730",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "signandcard",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "对于腐蚀性介质，佩戴防酸碱护镜或面罩等；",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007193,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs08",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022184,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "对于强腐蚀性介质，应穿戴全身性的防腐蚀防护用品，检查备用防护用品状况良好",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007194,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs09",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022185,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "在介质温度较高或较低时，有防烫或防冻措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007196,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs11",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022187,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "对于必须带压（高于规定）等危险性大的作业，制定专项应急预案",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007199,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs14",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022190,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "对于易燃易爆介质，穿防静电工作服和工作鞋，使用防爆灯具和防爆工具，禁止用铁器等黑色金属敲打，并以水雾稀释",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007203,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs18",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022194,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "其他补充安全措施：（ 哈哈）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007204,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "mbcs19",
		"dataStatus": 0,
		"worktype": "mbcd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022195,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 170
caseinfo['name'] = '现场确认-盲板抽堵-会签-生产单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=mbcd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592876070815"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007481",
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
			"uuid": "1592876070815"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"name": "生产单位监护人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 3
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 171
caseinfo['name'] = '现场确认-盲板抽堵-会签-生产单位负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=mbcd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592876089356"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007479",
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
			"uuid": "1592876089356"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"name": "生产单位负责人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 4
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 172
caseinfo['name'] = '现场确认-盲板抽堵-会签-施工单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=mbcd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007478",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\nR04AAAAASUVORK5CYII=\n",
			"uuid": ""
		}],
		"name": "施工单位监护人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nR04AAAAASUVORK5CYII=\n",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 173
caseinfo['name'] = '现场确认-盲板抽堵-会签-作业人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=mbcd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007480",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "作业人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 6
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 174
caseinfo['name'] = '现场确认-盲板抽堵-会签-工艺技术员'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=mbcd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data =  {
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
		"uuid": "1592876109102"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007482",
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
			"uuid": "1592876109102"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"name": "工艺技术员",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 7
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 175
caseinfo['name'] = '现场确认-盲板抽堵-会签-作业单位负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=mbcd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007483",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "作业单位负责人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 8
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#管线/设备打开
workticketidx = workticketid+5
ts = tsi+5
worktaskidx = worktaskid+1
caseinfo['id'] = 176
caseinfo['name'] = '现场确认-盲板抽堵-会签-装置主管'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=mbcd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592876126296"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007484",
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
			"uuid": "1592876126296"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 9,
		"isinputidnumber": 0,
		"name": "装置主管",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 9
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#动土作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 177
caseinfo['name'] = '现场确认-动土作业-属地确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&tabtype=measure&businesstype=SDQR'%(workticketidx)
data = {
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
		"uuid": "1592880910811",
		"businesstype": "SDQR"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000007516",
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
			"uuid": "1592880910811",
			"businesstype": "SDQR"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "确认人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "已开展JSA风险分析，并制定相应作业程序和安全措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007169,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs01",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022126,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业地点处于易燃易爆场所，需要动火时已办理了用火许可证",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007174,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs06",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022131,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "备有可燃气体检测仪、有毒介质检测仪",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007180,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs12",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022137,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "视频监控措施已落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007184,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs16",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022141,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())


#挖掘作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 178
caseinfo['name'] = '现场确认-动土作业-作业确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&tabtype=measure&businesstype=ZYDY'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "ZYDY"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007737",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "已按施工方案图划线和立桩",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007173,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs05",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022130,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业现场围栏、警戒线、警告牌、夜间警示灯已按要求设置",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007176,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs08",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022133,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "已进行放坡处理和固壁支撑",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007177,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs09",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022134,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "人员进出口和撤离安全措施已落实：A梯子；B修坡道",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007178,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs10",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022135,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "道路施工作业已报：交通、消防、安全监督部门、应急中心",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007179,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs11",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022136,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "作业人员已佩戴防护器具",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007182,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs14",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022139,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "动土范围内无障碍物，并已在总图上做标记",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007183,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs15",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022140,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#挖掘作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 179
caseinfo['name'] = '现场确认-动土作业-双方确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&tabtype=measure&businesstype=SFQE'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "SFQE"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007738",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "signandcard",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "地下电力电缆已确认保护措施已落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007170,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs02",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022127,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "地下通讯电（光）缆、局域网络电（光）缆已确认保护措施已落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007171,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs03",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022128,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "地下供排水、消防管线、工艺管线已确认保护措施已落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007172,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs04",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022129,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "动土地点有电线、管道等地下设施，已向作业单位交底并派人监护",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007175,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs07",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022132,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "现场夜间有充足照明",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007181,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs13",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022138,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "其他安全措施：（ 乐乐）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007185,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "dtcs17",
		"dataStatus": 0,
		"worktype": "dt",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SFQE",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022142,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#挖掘作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 180
caseinfo['name'] = '现场确认-动土作业-会签-施工单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007518",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "施工单位监护人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "iVBORw0KGgoAAAANSUhEUgAAAhwAAAGhCAYAAAAqQm1KAAAAAXNSR0IArs4c6QAAAARzQklUCAgI\nCHwIZIgAAAoMSURBVHic7d3Nq51XFQfg3bQxtaXEUVOM2KKiKFYEraJCwQzUzEQbnVSUjoSiUmod\n6EQnVf+DDgRBiuAHKPhROhFRY0sVBQMqYilVKFIIflBtahPi4ILpzbtOcu+5797rnPU+D2SyR79B\nuPzYa+33tAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAChu1prf2+tfTM7CABQ052ttYuX/YMU12QHAKCbqGD4u0+KQ9kBAOji9uwAAEB9l49SLrbW\n/pqaCAAo5d4WF47rM0MBALVEZePp1EQAQClPtLhwAADM4hUtLhsPZYaC1jyPAqhk1U2Gv/Wk8ywW\noIZPrTg/MTQFAFBaNEr5T2oiAKCU37a4cBzODAUA1HFDi8vG9zNDAQC1nGuewQIAHb2zxWXjVGYo\niHgqBbC9opuMi80LRDaQ/5QA2+m+FefHhqYAAEqLRinPpCYCAEp5uFkUBQA6i8rGj1ITAQClnGlu\nNwCAjg63uGw8mBkKAKjlbHO7AQB0dKzFZePuzFCwVz78BbAdzrfWrg3O/R1nK/jwF8Dme0OLy8bb\nRgeBdWnGAJsv2tO40Fq7bnQQWJcbDoDNdmLF+fGhKQCA0qJF0edSEwEApdzV4sLx8sxQAEAtUdl4\nKjURAFDKqeYjXwBAZ1HZeCw1EQBQyqrdDQCA2bjdAAC6crsBAHTndgMA6OpEc7sBAHQWlY3fpCYC\nAEp5ZYsLhx/ZBABm8682LRvPpiYCAEq5rsW3GzdlhgIAajnTpmXjQmoiAKCc6HbjzamJAIBSHm6e\nwgIAnUVl42OpiQCAUvwEPQDQXVQ2HkpNBACUckNzuwEAdPbnNi0bZ1MTAQDlRLcbx1ITAQClfLEZ\npwAAnUVl49OpiQCAUm5tbjcAgM6eadOy8fPURABAOdHtxpHURABAKZ9pxikAQGdR2fhcaiIAoJQj\nze0GANDZT9q0bPwjNREAUE50u/H61EQAQCknm3EKANDZ821aNr6VmggGuyY7AMACRLcZh1acQ0mH\nsgMAFHfvinNlAwCYTbS78YXURJDASAWgr+gmw99eFsdIBaCfrwRnF4anAABKi8YpH09NBACUcm3z\n7Q34PyMVgD6+EZw9NzwFAFBadLtxIjURAFDKy5pxCgDQ2dfbtGw8nZoIACgnut24MzURJPPxGYD5\n+dgXXMYrFYB5fSk4e354CgCgtGiccndqItgArvgA5mWcAgEjFYD53JMdAACo74U2Had8PjURbAjX\nfADzMU6BFYxUAObxjuwAAEB9p9t0nPK11EQAQDnRc9ijqYlgg5gtAszD/gZcgR0OgIO7Pzj75/AU\nAEBp59p0nPKJzECwaVz3ARyccQpchZEKwMG8KjsAAFDf99p0nPKD1EQAQDnRc9jXpSaCDWTGCHAw\n9jdgD+xwAKzvZHAWFRAAgLU93qbjlK+mJgIAyon2N25MTQQbypwRYH32N2CP7HAArOf9wZn9DQBg\nVo+16Tjly6mJAIByov2NI6mJYIOZNQKsx/4G7IMdDoD9e19wdn54CgCgtNNtOk55MDURAFCO/Q3Y\nJ/NGgP2zvwH7ZIcDYH9enR0AtpHCAbA/9wVn3x2eAgAo7cU23d94V2oi2AJmjgD7Y38D1mCkAgB0\np3AA7N2Hg7Ozw1MAAKX9ok33Nx5ITQQAlBN98Ov61ESwJSw6AeydhVFYkx0OgL05mh0AtpnCAbA3\nnwzOfjg8BQBQ2p/adH/jg6mJYIuYPQLsjf0NOAAjFQCgO4UD4OoOZweAbadwAFzdPcHZL4enAABK\ne6JNF0ajEgIAsLboC6PGLLAPNqwBrs4LFTggOxwAQHcKB8CVfTQ4++PwFABAaY+06f7GZ1MTAQDl\nRAujx1MTwRay9ARwZRZGYQZ2OACA7hQOgNVuzA4AVSgcAKt9JDg7PTwFFKBwAKx2Kjj79vAUAEBp\n0QuVW1ITwZayaQ2wmhcqMBMjFQCgO4UDIOaFCsxI4QCIRQujPxueAopQOABiHwrOvjM8BQBQ2vk2\nfaFya2oi2GK2rQFiXqjAjIxUAIDuFA4AoDuFA2Aq2tW4MDwFFKJwAEx9IDj78fAUUIjCATB1Mjh7\nZHgKAKC0c236JPa2zECw7TzxApjyJBZmZqQCAHSncAAA3SkcALsdzw4AFSkcALu9NzjzQgUOSOEA\n2C0qHD8dHQIAqO3JNn0Se0dqIijAMy+A3TyJhQ6MVACA7hQOAKA7hQMA6E7hALjktuDshdEhoCKF\nA+CS6Enso8NTQEEKB8AlvsEBAHT3lzb9BsdbUxNBEd6WA1ziGxzQiZEKANCdwgEAdKdwAADdKRwA\nO44GZ9FOB7AGhQNgx3uCs8eHp4CiFA6AHVHhOD08BRSlcADseHdwpnAAALN6sU0/+nVzaiIoxAdt\nAHb46Bd0ZKQCAHSncAAA3SkcAEB3CgdAa7cEZ+eHp4DCFA6A1t4enHkSCzNSOABauyM4+9XwFFCY\nwgEQ33D8engKAKC0Z9v0o1+vSU0ExfioDYCPfkF3RioAQHcKBwDQncIBAHSncAAA3SkcwNK9Njj7\n2/AUUJzCASzd7cHZmeEpoDiFA1i6qHD8bngKKE7hAJbuLcGZwgEzUziApTNSgQF8SQ9Yuugro4dW\nnANrcsMBMKVswMwUDgCgO4UDAOhO4QAAulM4AIDuFA5gyW4Kzv47PAUsgMIBLNmbgrM/DE8BC6Bw\nAEv2xuDs98NTwAIoHMCSueGAQRQOYMmiwuGGAwCY1ZNt56uiL/0XlRDggPyWCrBkfkcFBjFSAdhN\n2YAOFA4AoDuFAwDoTuEAALpTOACA7hQOYKm80oOBFA5gqaLvbTw1PAUshMIBLJXPmsNACgewVNEP\ntykc0InCASyV31GBgRQOYKmMVACA7v7dpj/cdjQ1EQBQzqNtWjgAAGb30rLxQHIWAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nAAAAAAAAAAAAAAAAABL8DxJcSpkHx+cyAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 3
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#挖掘作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 181
caseinfo['name'] = '现场确认-动土作业-会签-属地单位监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592881050924"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007519",
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
			"uuid": "1592881050924"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 1,
		"name": "属地单位监护人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 4
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#挖掘作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 182
caseinfo['name'] = '现场确认-动土作业-会签-水、电、气等相关单位'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007520",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "水、电、气等相关单位",
		"audittype": "card,signandcard",
		"specialworktype": "",
		"value": "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\nTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 6
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#挖掘作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 183
caseinfo['name'] = '现场确认-动土作业-会签-施工单位负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007521",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 2,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "施工单位负责人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 7
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#动土作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 184
caseinfo['name'] = '现场确认-动土作业-会签-属地单位项目负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592881168202"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007739",
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
			"uuid": "1592881168202"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"name": "属地单位项目负责人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 8
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#动土作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 185
caseinfo['name'] = '现场确认-动土作业-会签-安全环保处'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007877",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "安全环保处",
		"audittype": "sign,signandcard",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 9
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#动土作业
workticketidx = workticketid+2
ts = tsi+2
worktaskidx = worktaskid+1
caseinfo['id'] = 186
caseinfo['name'] = '现场确认-动土作业-会签-属地单位工程管理部'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=dt&worklevel=hse_worklevel_dt01&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592881185149"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007523",
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
			"uuid": "1592881185149"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 4,
		"isinputidnumber": 0,
		"name": "属地单位工程管理部",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 9
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 193
caseinfo['name'] = '现场确认-临时用电-用电设备-用电设备新增'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/afreshInsertLSYD.json?workticketid=%d'%(workticketidx)
data = {
	"data": [{
		"vo": {
			"elecequiplistid": "",
			"equipmentname": "用电设备",
			"equipnum": "",
			"elecload": "",
			"workticketid": ""
		}
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 194
caseinfo['name'] = '现场确认-临时用电-属地确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=lsyd&tabtype=measure&businesstype=SDQR'%(workticketidx)
data = {
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
		"uuid": "1592880395028",
		"businesstype": "SDQR"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"groupType": "4",
		"code": "2000000007507",
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
			"uuid": "1592880395028",
			"businesstype": "SDQR"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"name": "确认人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "开展JSA风险分析，并制定相应作业程序和安全措施",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007137,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs01",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "SDQR",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022113,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 195
caseinfo['name'] = '现场确认-临时用电-作业确认'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/measureAudit.json?workticketid=%d&workType=lsyd&tabtype=measure&businesstype=ZYDY'%(workticketidx)
data = {
	"mainAttributeVO": {
		"businesstype": "ZYDY"
	},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"groupType": "4",
		"code": "2000000007735",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 1,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n/g/fKmdNcVkv6gAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "确认人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\n/g/fKmdNcVkv6gAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 1
	}],
	"voList": [{
		"measuredesc": "安装临时线路人员持有电工作业操作证。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007205,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs02",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022114,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "在防爆场所使用的临时电源、电气元件和线路达到相应的防爆等级要求并有措施。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007206,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs03",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022115,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "生产区内爆炸和火灾危险场所的三相临时用电应采用五线制。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007207,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs04",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022116,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "临时用电架空线最大弧垂与地面距离装置内不低于2.5米，道路不低于5米。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007208,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs05",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022117,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "临时用电线路架空进线采用绝缘铜芯线，不得采用裸线，不得在树上或脚手架上架设。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007209,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs06",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022118,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "暗管埋设及地下电缆线路应设有“走向标志”和安全标志，电缆埋深大于0.7米，穿越公路应加设防护套管。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007210,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs07",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022119,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "现场临时用电配电盘、箱应有防雨措施，盘、箱门必须能牢靠关闭",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007211,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs08",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022120,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "临时用电设施安有漏电保护器，移动工具、手持工具应“一机一闸一保护”。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007212,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs09",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022121,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "行灯电压不超过36伏，在特别潮湿场所或塔、罐等金属设备内，不得超过12伏\n用电设备和线路的负荷、容量符合要求。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007213,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs10",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022122,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "视频监控措施已落实",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007214,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs11",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022123,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "用电设备和线路的负荷、容量符合要求。",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007215,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs12",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022124,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}, {
		"measuredesc": "其他补充措施（ 哈哈）",
		"df": 0,
		"mesuresource": "qy",
		"ismust": 1,
		"ischecked": "true",
		"ismustphoto": 0,
		"tableName": "hse_work_task_measure",
		"tenantid": 2000000001003,
		"audittype": "",
		"ismustconfirm": 0,
		"signSrc": "",
		"riskrepositoryid": 2000000007216,
		"isselect": 0,
		"ver": 1,
		"created_dt": now,
		"measurecode": "ydcs13",
		"dataStatus": 0,
		"worktype": "lsyd",
		"isshowphoto": 0,
		"person_name": "",
		"prepareperson": "2000000012062",
		"created_by": 2000000012062,
		"measuretype": "ZYDY",
		"updated_dt": now,
		"worktaskmeasureid": 2000000022125,
		"updated_by": 2000000012062,
		"preparepersonname": "长岭石化管理员",
		"workticketid": workticketidx,
		"worktaskid": worktaskidx,
		"isconfirm": "1"
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 196
caseinfo['name'] = '现场确认-临时用电-会签-用电人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=lsyd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007508",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\nS2k5BNtHAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "用电人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nS2k5BNtHAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 2
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 197
caseinfo['name'] = '现场确认-临时用电-会签-用电负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=lsyd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007527",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\nAAAAAMB0+x/fNOMYRL7e/QAAAABJRU5ErkJggg==\n",
			"uuid": ""
		}],
		"name": "用电负责人",
		"audittype": "sign",
		"specialworktype": "",
		"value": "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\nAAAAAMB0+x/fNOMYRL7e/QAAAABJRU5ErkJggg==\n",
		"isbrushposition": 1,
		"disporder": 2
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 198
caseinfo['name'] = '现场确认-临时用电-会签-监护人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=lsyd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007509",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 1,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 1,
		"electronicSignature": [{
			"imgStr": "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\nAl8csoO+AS5iAAAAAElFTkSuQmCC\n",
			"uuid": ""
		}],
		"name": "监护人",
		"audittype": "signandcard",
		"specialworktype": "",
		"value": "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\nAl8csoO+AS5iAAAAAElFTkSuQmCC\n",
		"isbrushposition": 1,
		"disporder": 3
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 199
caseinfo['name'] = '现场确认-临时用电-会签-临时用电单位'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=lsyd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
	"mainAttributeVO": {},
	"auditPlainLineList": [{
		"actiontype": "sign",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007510",
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"electronicSignature": [{
			"imgStr": "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\n",
			"uuid": ""
		}],
		"name": "临时用电单位",
		"audittype": "sign,passward",
		"specialworktype": "",
		"value": "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\n",
		"isbrushposition": 1,
		"disporder": 4
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 200
caseinfo['name'] = '现场确认-临时用电-会签-供电主管部门'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=lsyd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592880585932"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007511",
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
			"uuid": "1592880585932"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"name": "供电主管部门",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 5
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 201
caseinfo['name'] = '现场确认-临时用电-会签-供电执行单位负责人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=lsyd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592880598009"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007512",
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
			"uuid": "1592880598009"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 0,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 3,
		"isinputidnumber": 0,
		"name": "供电执行单位负责人",
		"audittype": "card,face",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 6
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())

#临时用电
workticketidx = workticketid+1
ts = tsi+1
worktaskidx = worktaskid+1
caseinfo['id'] = 202
caseinfo['name'] = '现场确认-临时用电-会签-送电人'
url = 'http://192.168.6.156/m/hse_m/HSE_WORK_TICKET_M/signAudit.json?workticketid=%d&workType=lsyd&worklevel=&datatype=sign&actionCode=sign'%(workticketidx)
data = {
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
		"uuid": "1592880608896"
	},
	"auditPlainLineList": [{
		"actiontype": "card",
		"isexmaineable": 1,
		"groupType": "4",
		"code": "2000000007513",
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
			"uuid": "1592880608896"
		}],
		"idnumber": "",
		"dataStatus": 0,
		"ismustaudit": 1,
		"force_photo": 0,
		"isEnd": 1,
		"ismulti": 0,
		"isShow": 1,
		"auditorder": 7,
		"isinputidnumber": 0,
		"name": "送电人",
		"audittype": "card",
		"specialworktype": "",
		"value": "",
		"isbrushposition": 1,
		"disporder": 7
	}]
}
caseinfo['url'] = url
caseinfo['data'] =data
testsuitm39.append(caseinfo.copy())