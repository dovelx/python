
import requests
import execjs
import os
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

data={"appVersion":"01.20.0521","loginStoken":loginStoken,"password":pwd,"username":"test",'tenantid':0}
#data = base64.b64encode(json.dumps(data))
req = requests.post(url=url1,json =data,headers = headers)

cookies = requests.utils.dict_from_cookiejar(req.cookies)
print (req.content)
print (cookies)
#encryptType = eq['data']['encryptType']
#print (encryptType)