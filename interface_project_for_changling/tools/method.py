import requests
import json
from tools import assert0

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
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json化
        data = json.loads(data)
        # 获取接口返回状态
        #print("data",data)
        sta = data['status']
        #if caseinfo['id'] == 100:
        #    insert = data['data']['insert__']
        if sta == 3200:
            if caseinfo['exresult'] != "":
                #print("预期结果不为空，开始比对预期结果")

                response_to_check = str(data)
                expected_result = caseinfo['exresult']
                for item in expected_result['条件']:
                    pattern_str = item['模式']

                    # logger.info('要匹配的模式（正则表达式）为：%s' % pattern_str)
                    a=assert0.assertRegex(response_to_check, pattern_str, msg=item['消息'])
                    if a==1:
                        caseinfo['result'] = "pass"
                        return caseinfo['result']
                        break
                    else:
                        caseinfo['result'] = "fail"
                        return "：失败，预期与实际结果不符"
            else:
                #print("预期结果为空，不做比对")
                caseinfo['result'] = "pass"

                return caseinfo['result']

        else:
            caseinfo['result'] = "fail"
            return data
    else:
        return rs.status_code
def pa(caseinfo,headers,cookies):
    rs = requests.post(url=caseinfo['url'], json=caseinfo['data'], headers=headers, cookies=cookies)
    if rs.status_code == 200:
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
    else:
        caseinfo['result'] = "fail"
        return rs.status_code

def pm(caseinfo,mheaders):

    rs = requests.post(url = caseinfo['url'],json=caseinfo['data'],headers=mheaders)
    if rs.status_code ==200:
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
        return rs.status_code


def gm(caseinfo,headers):
    rs = requests.get(url=caseinfo['url'], headers=headers)
    if rs.status_code == 200:
        # 返回值转码
        data = rs.content.decode('utf-8')
        # json化
        data = json.loads(data)
        # 获取接口返回状态
        #print("data",data)
        sta = data['status']
        #if caseinfo['id'] == 100:
        #    insert = data['data']['insert__']
        if sta == 3200:
            if caseinfo['exresult'] != "":
                #print("预期结果不为空，开始比对预期结果")

                response_to_check = str(data)
                expected_result = caseinfo['exresult']
                for item in expected_result['条件']:
                    pattern_str = item['模式']

                    # logger.info('要匹配的模式（正则表达式）为：%s' % pattern_str)
                    a=assert0.assertRegex(response_to_check, pattern_str, msg=item['消息'])
                    if a==1:
                        caseinfo['result'] = "pass"
                        return caseinfo['result']
                        break
                    else:
                        caseinfo['result'] = "fail"
                        return "：失败，预期与实际结果不符"
            else:
                #print("预期结果为空，不做比对")
                caseinfo['result'] = "pass"

                return caseinfo['result']

        else:
            caseinfo['result'] = "fail"
            return data
    else:
        return rs.status_code