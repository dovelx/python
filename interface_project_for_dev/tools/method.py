import requests
import json

def p(caseinfo,url,headers,cookies,data):
    rs = requests.post(url, json=data, headers=headers, cookies=cookies)
    # 返回值转码
    data = rs.content.decode('utf-8')
    # json化
    data = json.loads(data)
    # 获取接口返回状态
    sta = data['status']
    if sta == 3200:
        #print("作业预约成功", sta)
        caseinfo['result'] = 1
        return sta
    else:
        caseinfo['result'] = 0
        return data
def pa(caseinfo,headers,cookies):
    rs = requests.post(url=caseinfo['url'], json=caseinfo['data'], headers=headers, cookies=cookies)
    # 返回值转码
    data = rs.content.decode('utf-8')
    # json化
    data = json.loads(data)
    # 获取接口返回状态
    sta = data['status']
    if sta == 3200:
        #print("作业预约成功", sta)
        caseinfo['result'] = "pass"
        return caseinfo['result']
    else:
        caseinfo['result'] = "fail"
        return data


def pm(caseinfo,mheaders):

    rs = requests.post(url = caseinfo['url'],json=caseinfo['data'],headers=mheaders)
    # 返回值转码
    data = rs.content.decode('utf-8')
    #json格式化
    data = json.loads(data)
    # 获取接口返回状态
    sta = data['status']
    if sta == 3200:
        # print("作业预约成功", sta)
        caseinfo['result'] = "pass"
        return caseinfo['result']
    else:
        caseinfo['result'] = "fail"
        return data
