
import requests
import execjs
import os
import json

def getEntryPwd(encryptType,pwd,modulus,publicExponent):
    # 返回加密后的密码
    path=os.path.abspath(os.path.dirname(__file__))
    file=os.path.join(path,'./hdEncrypt_merge.js')
    #logging.debug("path:%s"%path)
    data=open(file,'r',encoding= 'utf8').read()
    jss=execjs.compile(data)
    #logging.debug(jss)
    return  jss.call("login",encryptType,pwd,modulus,publicExponent)

url = "http://192.168.6.27:6030/m/passport/login/getEncryptType.json"
url1 ="http://192.168.6.27:6030/m/passport/login/login.json"

headers ={
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
    'Connnection':'Keep-Alive'
    }
sr = requests.get(url,headers=headers)

eq = sr.json()

USER_NAME = "test"
password ="1"
loginStoken=eq['data']['loginStoken']
encryptType=eq['data']['encryptType']
modulus = eq['data']['pubKeyVO']['modulus']
publicExponent = eq['data']['pubKeyVO']['publicExponent']
pwd = getEntryPwd(encryptType,password,modulus,publicExponent)
print (eq)
print (eq['status'])
print(loginStoken)
print(encryptType)
print( pwd)
#print(eq['data']['pubKeyVO'])
headers={
    'Accept': 'application/json',
     'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.12.0',
    'Connnection': 'Keep-Alive'
    }

data={"appVersion":"01.20.0530","loginStoken":loginStoken,"password":pwd,"username":"test",'tenantid':0}
#data = base64.b64encode(json.dumps(data))
rs= requests.post(url=url1,json =data,headers = headers)

cookies = requests.utils.dict_from_cookiejar(rs.cookies)

#返回值转码
data = rs.content.decode('utf-8')
#json化
data = json.loads(data)
loginStoken = data['data']['st']
print(data)
print(loginStoken)
#encryptType = eq['data']['encryptType']
#print (encryptType)

#cookies={'JSESSIONID': '0F5ED4C32181CF4F223E2984DFCE086A0afqB2'}
url = "http://192.168.6.27:6030/m/hse_m/HSE_WORK_TICKET_XKZ_MCQ_M/cardSave.json?level=1"
headers = {
            "Accept":"application/json",
"Accept-Encoding": "gzip",
"user-agent":"ONEPLUS A6010(Android/10) (com.hayden.hap.fv/1.0.2) Weex/0.16.0 1080x2134",
"Content-Type": "application/json;charset=UTF-8",
    "st":loginStoken,
    "tid":"1"

}