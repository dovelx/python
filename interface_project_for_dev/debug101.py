
import  requests
import json
from runners import pc_login

cookies = pc_login.cookies
#预约列表接口地址
url1 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/getMetaData?0.3897117454385264&contentType=json&ajax=true&tid=1'
url1 = 'http://192.168.6.27:6030/hse/HSE_WORK_APPOINT/getMetaData?0.3897117454385264&contentType=json&ajax=true&tid=1'
#请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '6363382b59f6435eb243fab57ea5a5e0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }

#请求接口
rs=requests.get(url1, headers = headers,cookies=cookies)
if rs.status_code == 200:
    #返回值转码
    data = rs.content.decode('utf-8')
    #json格式化
    data = json.loads(data)
    #获取接口返回状态
    status= data['status']
    if status == 3200:
        print("获取列表成功", status)
        #获取本次作业预约的work_appoint_id
        data = data['data']['voset']['voList']
        #print(data)
        temp = []
        for a in data:
            #print("\n\n",a)
            if a['workname']  == "Created_by_Python_QY9tc3":
                temp.append(a['work_appoint_id'])
        work_appoint_id = temp[0]
        #当前最大work_appoint_id加1
        work_appoint_idx =work_appoint_id+1
        print("work_appoint_idx",work_appoint_idx)
    else:
          print("fail")