import requests
import json

def gy(caseinfo,headers,cookies):
    rs = requests.get(url=caseinfo['url'], headers=headers, cookies=cookies)
    #请求接口
    #rs=requests.get(url, headers = headers,cookies=cookies)
    if rs.status_code == 200:
        #返回值转码name
        data = rs.content.decode('utf-8')
        #json格式化
        data = json.loads(data)
        #获取接口返回状态
        status= data['status']
        if status == 3200:
            caseinfo['result'] = "pass"
            print("获取预约列表成功", status)
            #获取本次作业预约的work_appoint_id
            data = data['data']['voset']['voList']
            #print(data)
            temp = []
            for a in data:
                #print("\n\n",a)
                if a['workname']  == caseinfo['data']:
                    temp.append(a['work_appoint_id'])
            work_appoint_id = temp[0]
            #当前最大work_appoint_id加1
            #work_appoint_id =work_appoint_id+1
            print("work_appoint_idx",work_appoint_id)
            return caseinfo['result'],work_appoint_id
        else:
            caseinfo['result'] = "fail"
            return 0

def py(caseinfo,headers,cookies):
    rs = requests.post(url=caseinfo['url'], json=caseinfo['data'], headers=headers, cookies=cookies)
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json化
        data = json.loads(data)
        # 获取接口返回状态
        sta = data['status']
        if sta == 3200:
            #print("作业预约成功", sta)
            caseinfo['result'] = "pass"
            return caseinfo['result'],1
        else:
            caseinfo['result'] = "fail"
            return data,1
    else:
        caseinfo['result'] = "fail"
        return rs.status_code


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
    if rs.status_code == 200:
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
    else:
        caseinfo['result'] = "fail"
        return rs.status_code


def pm(caseinfo,mheaders):

    rs = requests.post(url = caseinfo['url'],json=caseinfo['data'],headers=mheaders)
    if rs.status_code == 200:
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
    else:
        caseinfo['result'] = "fail"
        return rs.status_code

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