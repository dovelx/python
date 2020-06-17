import requests
import json

def gh(caseinfo,headers,cookies):
    rs = requests.get(url=caseinfo['url'], headers=headers, cookies=cookies)
    # 返回值转码
    data = rs.content.decode('utf-8')
    # json化
    #data = json.loads(data)
    # 获取接口返回状态
    sta = rs.status_code
    if sta == 200:
        #print("作业预约成功", sta)
        caseinfo['result'] = "pass"
        return caseinfo['result']
    else:
        caseinfo['result'] = "fail"
        return data
def g(caseinfo,headers,cookies):
    rs = requests.get(url=caseinfo['url'], headers=headers, cookies=cookies)
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
def pa(caseinfo,headers,cookies):
    rs = requests.post(url=caseinfo['url'], json=caseinfo['data'], headers=headers, cookies=cookies)
    #print("rs",rs.content)
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

def gm(caseinfo,headers):
    rs = requests.get(url=caseinfo['url'], headers=headers)
    # 返回值转码
    data = rs.content.decode('utf-8')
    # json化
    data = json.loads(data)
    # 获取接口返回状态
    print("data",data)
    sta = data['status']
    #if caseinfo['id'] == 100:
    #    insert = data['data']['insert__']
    if sta == 3200:
        #print("作业预约成功", sta)
        caseinfo['result'] = "pass"
    #    return caseinfo['result'],insert

    else:
        caseinfo['result'] = "fail"
        return data