import requests
from tools import tool
import json

def mlogin (host,username,password):
    host = "192.168.6.27:6030"
    #移动端登录
    url = "http://192.168.6.156/m/passport/login/getEncryptType.json"
    #url = "http://192.168.6.27:6030/m/passport/login/getEncryptType.json"
    headers ={
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.0',
        'Connnection':'Keep-Alive'
        }
    sr = requests.get(url,headers=headers)

    eq = sr.json()


    url1 ="http://192.168.6.156/m/passport/login/login.json"
    #url1 ="http://192.168.6.27:6030/m/passport/login/login.json"
    USER_NAME = username
    USER_NAME = "clshadmin"
    password ="1"
    loginStoken=eq['data']['loginStoken']
    encryptType=eq['data']['encryptType']
    modulus = eq['data']['pubKeyVO']['modulus']
    publicExponent = eq['data']['pubKeyVO']['publicExponent']
    pwd = tool.getEntryPwd(encryptType,password,modulus,publicExponent)

    headers={
        'Accept': 'application/json',
         'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.12.0',
        'Connnection': 'Keep-Alive'
        }

    data={"appVersion":"01.20.0619","loginStoken":loginStoken,"password":pwd,"username":USER_NAME,'tenantid':0}

    rs= requests.post(url=url1,json =data,headers = headers)

    cookies = requests.utils.dict_from_cookiejar(rs.cookies)

    #返回值转码
    data = rs.content.decode('utf-8')
    #json化
    data = json.loads(data)
    loginStoken = data['data']['st']
    #print(data)
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "user-agent": "ONEPLUS A6010(Android/10) (com.hayden.hap.fv/1.0.2) Weex/0.16.0 1080x2134",
        "Content-Type": "application/json;charset=UTF-8",
        "st": loginStoken,
        "tid": "2000000001003"

    }
    return  headers


