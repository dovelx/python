import requests
import execjs
import os

cookies={"TENANTCODE":"cqsh","tenantCode":"cqsh","prjidentify":"cqsh","CASPRIVACY":"","TGC":"","module":"passports","JSESSIONID":"4241502E5012B2108D885C94B8C6DFCF"}
def getEntryPwd(encryptType,pwd,modulus,publicExponent):
    # 返回加密后的密码
    path=os.path.abspath(os.path.dirname(__file__))
    file=os.path.join(path,'./hdEncrypt_merge.js')
    #logging.debug("path:%s"%path)
    data=open(file,'r',encoding= 'utf8').read()
    jss=execjs.compile(data)
    #logging.debug(jss)
    return  jss.call("login",encryptType,pwd,modulus,publicExponent)
#url1 ='http://192.168.6.27:6030/logout'
url2 = "http://192.168.6.27:6030/preLogin/getPubKey"
#url3 ="http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false"
header = {
    'Host' : 'xxxxx',
    'Accept' : 'xxxx',
    'User-Agen': 'xxxx' # 这个最重要，建议手动设置（有时候没有设置，造成获取数据失败，本人被坑过......）
}
headers ={

    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
#sr = requests.get(url1,headers=headers)
#cookies = requests.utils.dict_from_cookiejar(sr.cookies)
#print(cookies)
#sr = requests.get(url2,headers=headers,cookies =cookies,allow_redirects=False)
s = requests.Session()
response = s.get(url2,headers=headers,cookies=cookies)
#location = response.headers['Location']
#print(location)
#resume_url = sr.headers['location']
#print(resume_url)
headers = response.headers
eq = response.json()

print(eq)
print("first headers",headers)
USER_NAME = "test"
password ="1"

#loginStoken=eq['data']['loginStoken']
encryptType=eq['data']['encryptType']
modulus = eq['data']['modulus']
publicExponent = eq['data']['publicExponent']
pwd = getEntryPwd(encryptType,password,modulus,publicExponent)

print ("pwd:",pwd)
#print (eq['status'])
#print(loginStoken)
print(encryptType)
#print( pwd)

#print(eq['data']['pubKeyVO'])
headers={
    'Upgrade-Insecure-Requests': "1",
     'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Origin':'http://192.168.6.27:6030'
    }

#data={"appVersion":"01.20.0521","loginStoken":loginStoken,"password":pwd,"username":"test",'tenantid':0}
data={"_eventId":"submit","captcha":"","execution":"342a5e6d-8fd3-4925-bf81-05368d2cccf2_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVmxCdFdtWjNhbHBtVTFsc1ExbHdVa3RMVVVJMlMwaHhlVWRaUzBsUkswOXZRMHA1TURCblRWbHZUbkYxTHl0T1ltZFNhbFl2ZEZZMVYweGxkMUZTSzFoYVprZGtUREowZHprM04zQkdRVFo0UTBWWWNUWm1OSEZrYkdSSFFVNDFWMkV2UVZGVVluSlhZalpKTldsTWNVOVhWbWwzYVRnNUwzRlZTVmsyWmpSV1p5ODBWWGROYW1OeVUzbDBPVVpTYnk5SU9DdEdOWEl5VmpoQ1kyNTBRVmg2T0RkS2NXSnFhVkp6Y1doWWRYTmtVVVp2UnpWVlUycDBVVGRNYldadWRsRmFWbEpDUjJkVVlUSmFVVUY0YUZndldXdHBlVlZDYmxscFVIaFhRVTVGYlVveU4zaFRjbUpGWVZoeFFtOTZhWEZ1T0ZacU1WUnpkVWhpZURkdFJVczVkM1Z3TTFGNk9FeExVMU5KZUdwUGNrOHdNbXRwVWpCUlkwRmFURE0zUVVZMU16aHhjVEZyVW14VGRHTlFkSEZCV21wb04xYzBZVU5SVGt4VmFtVlJTUzlOUWxGeE16Tm9ibEIxUkVSa0t6WlRUMDl3VVhWelVtb3pXblJ3YjJkTlR6UmxORkJSTWpSYWVITTVUblZNVmpGNE1EaFFiM1ZzU0VFclZDczBVRGh3TDNoRVJIVkJhRkJVVW5GM1VraGlNbWRtYkZwWWRWRlNhelZ2Y1dVMlVUbG1hSFJoSzNKM2MxTTRRMFZoWXpSRmVVNDFNeXN4Y0dRMGQyOTZjMG95TkZSQ1VrSkdUalZFZWk4MVpHWkJkSFkzVTBkbFYxZHNlazgzVkRJd1FuRmlaak15Y2xwUWJtdEhibk5SVG1WQmExWXdNbEZvUWtRd2JXSnNibUZpTkdOUVdUVXllVkowU25GdGRHTjFMMGx3UmlzMlEzTXZNMDF3Vmt4S1pIRjJPRUo2VDNndmQxbFlVa0Z0Y1V0V2NVOVFVMmRzVFM5amQzZHZjbUpJU3paRk1YbHljM2NyVFhkV1YyVkxjVGhTVldzMldYSlNjVFEwZFVaa1JsaFpTRGhtVmtJdlVsWXdUaTlSVlhoVFNUbHRaWEJQYW5CME16ZFpVSGd5U1U5Q1RteE9iWGRXUXpWM2IybzRjVXcwTlZNMVNFdzJhM3B2Tm1WcGRWWllNbWczWmxsemQxQkRNRlU1YjNCMlUybEhWV0U0VVZOcVUwbE1abU5uVDJsNk1WQnJabTlCVUdabWMxQk5jV05aWVRCeE5tUm9ZVVpzTW5kbk5XdERiM1pSY3pVNFVtczFWMlptZEc5MFZVVllTRmgzYmtKSVZVVjZTbGRFUlVoWmRXNUZjMFk1Y2xkVE0xbFlPRmd5VldZeFV6SnVhRVU1V21Wb2VGTnFUQ3REVjNoSlR6WkdVMDQyZUdKTFVucElaSGQ1U0hWamFVSjZhMU53VTB4aGFrVXphbFpKUjNrMWMxQlJWa2szYzJzME1VcHhXa2xsVUdKelQwcDZNU3RCTmtsUE9EZHRkbEl3UVdGd1MwUk5aMngxVldVemRVSndRWGh6YldzMlNXZzRkblZ1U0Vwbk1qWnRSVXhsVjJsTWJuaHZOVzlQTUcwNU5UZG9kR2N5UVM5M1FtMVBTRUZOYjNGelVtZzRWRVZwYTIwME5rRnRiMUZyY0RSbGRrcFlLMFJ3ZDI5TU5EVXdUbW80Vm5KVmJXb3ZZbE5ZT0djdlN6YzNiVXgyWXpOb1oybExZekJhYWpaaE1XdHJNbWRoUW5ad09GUlhSMHhQYzJwQ1NGZElWbU5xUms1M05rUmlPVXBvYmtFMVZsa3laR0owZVd0U1dqWlNiR2d4WlRRMVVGVjJZa3BWTm5kc1pFUk1MMjl5ZGtoNGQzUTBkMVZpVVdGWFFVOUtPRzF0Um01NFFXWnpPVlpMWVVoeFRHRkZVbTR5V1ROWllqTkNWWGR2TXpWb2RHWnpiRk51VTNRek0ySmxVSFV3UnpZeWQxWnZMMFZWZUhwd1UzZHFNMmg1WjFGUWFGVkpOSEp2TjBKdGJHZDJkVTh4WkdkNFREQkRWVTFGTkd0UWNtRm1jV3hHYlVKYVJUQlpVVXhHYXpWaFYxRnFXRGRrWTJSalRFVnhPVUpwVmt0aFQwTnhhVkpCZVZKNU1qRjJOV2hOZDFSMGRGaGpjRVpNYVZJclZERnpiRzFMTm5wM1ZXSldVVTlvV2pKekwzbGpUakZDUlhaWk56ZzBNV3Q0VmxwUmNrVnFNMVV4UzBSd2EwMVVRbW8zTkV4MFEwOHhPV0V6VGtWS2VXTkZVRXcwZUhwWVFVMUJTak1yYW5kc1J6YzVOSGhSUmxkdVRrOU1aeTlKVWpGQ05UTnRURXBSYTFFdlZsZGFaVGhrZHpJek0yOVpXVTUyVERaNVpVeHlhRXBpWnk5SlZrTlRUMGxFZW0xUGVHd3lSVFV4Y1hkRk9HRXlZVXBvZWpoVFFWRlhMMUZNUmpOb2RXcFpWWGRoVFVKeVlVMWxRUzlMVEZJeFpVVTBjMlZCVXpSMU1IcENObUUyUkdwSU5DOXBaWE5xVlcxUGRHWmtTM2x5YWtGdVNWQXdSMGRrVUdoUFVGaGlRVVp2Vm5sTGRGVm1WVXd4TkhNdlRFaExTVVl2ZFdsbVlVUm9WRUZFTjFwNmMxcDBhMXBLUW1sTldIbHpNMU5pV1daYU4zWTFUak5QYlVkV1dpOXJNR2R4YlhWS2NtRlVVbVZYY1VKVWFqWjFjbE5RVkdzMFVWZHFOMmszWlU1R1EzTjVVRlJMWVdSR05sSkpiM2x1YlM5MWVUQTFURVpCYmxWM1RVTlZVa0owZUVsell6Y3ljRXR0WjAxclpXTnhXVlprY3pkak5HaDFZV0ZzYkZwdE5rTkJSek55ZUZBNE4wSkZPVllyY2xOMFIzRXpkVUkzVXpScWRXMXhPV3h3VjFwdVVIZDNUMUJVWVc1c2NFNVVaRWRJTkhoRGVteFFUVEFyYzA5bE5IWTJjMk41ZG5OVFJWUXJaazAxZG5aQlduQXhTbEJLVEdjMU0wRmxlRkpLU2xRMUwwOVpUa2d4UlhKV2RrcHpRalE1Tnl0NldFUllRWEV6WkRjcldXbExUVlJKSzFaNmRXTjBkRXg0TkZnMVIzZGlNSFpyVlVKWFVtUnpkRlJtV0ZRM1IzVXhVelJEY1ZwSUwwRXpSRTg1U2tKa1JFZFRRV052TXpGSGFIVnpibGRaWlZFeE9UWm1PV2MyTlRWamJWRTJaRzFNVFdKeVFVTTJOM1pDWjJOdGJYWlVkVTFOZGtsbU5XazRRMHMxY2xrMGJuSXJaMk41WkVrMmJIWXJkR1pNWTBWMGRGUjNjV3gyUVU1d1kxRkVUVVJyUmt4NWEwaERWVlZDVFZGNmFsZDBaa2s0T1hGT2JUTnlkM2g2WlRGck5HWk1TVlYwVG1sVVQyVmFhRTVOV1RSRmJuWkRiSEUwVVVwQ056aEZXV3hsVFdkQ1IwcHNTa2xWY0hOUlNXbEphRlJuV1ZJNGVtWlJSa2t2VDFwdFUwTXlWRGhCTW14cldHSmpVMUZOVUVabFRXMVRXbko2ZUhoeVkwcFdVWEF4VkdsMVEwMVBlbHAwTldkUk9HZHZVVVE1VFZObVRXRnRRMnhJVG5sYVlYcGtSeTgxTTBZelJYSlFSelZCWkhWUlZTOVZOSE5oZUVWM05qVmtlR2ROU21sc1pWQm9hVmREWTJ0MFdqTm5NbkpMZGtkTFZXZHlOVmRLVlhWUWFXdGpTakp3ZVU5Q2VXSjVkR0U1TXpkb2FTOXliRmRRVG5aNVUwUnllakpHS3pnd1VGYzBOV015VWtkU1FWZzRkVFpuTVROR1REaHVTa1JWUzBWREszZFVlbk5JV0RWdFpWbFVVMnRQZVZkT2NYVmpiVWQwYlZWbFltbERZa1I2Vml0YVYwcGFZVVFyZFdkS1kyMUZUREJpTVVSMlFXVmpRWGsxUXl0TFlVeHNWbTFZYkZkamNuQjVZVGxNWW5WT2EzSnNXak54Y0RSWVJGWlVZMUU0Tnk5eGJtTnpRM2szVUhRMmEzSTBWWGw2Um5rNVl6ZHZRVlpVYTA5UU1HWXpiWEpFTkdNNE5VbDBhSG8zZG1aTU5ITjBka2h2TDNneU0xVkhVamhHTUVwaWMyWlphbWxqT1cxYVVqQldjRkpYWlZjemRIWkZOMFo0VDB0aGFXWXdUa1JRT0hCME9VNXJhVXh6YVRobk1WRlRNM1kxYWxoV2MyMTRiMFl5UjJaQ04yYzVTMHdyYlRoU1ZVRXJaa05DZFRkSFZtVnNZMkpFT0hZMmJXWTFSSGhvYTNOTU5Hb3phRWR4T0M4ME1uZHBSMU5PTHk5dE1XdFhXWGg1VWtSR2QxUjFiM0pyVUdGSVYzRkZUMDRyZFZsYWVYUmpTWHBtT0ZBMlRURnJOelJZVHpaWlZrMU9aMUZGVVVsSGVUWXdSWGxNVEVGSlluVTJUSGQzTVdoQmJIWm5SV0Z1Y2xGVWVUQklaMk13ZEVRMFIwSXdia0UxYm1ndmQyaDFTRlYwUWpkdVJ6TkhWazl1UVRaR01GZ3ZRemRLV1hORlVYSkZiVWxGYlU5cGRGRnVZU3RwT0VoWmVqTTFaa3RSVUcxSmVqTkROSEZESzB3NVRHbEpTak51ZGtGRGFXODJiRzlYWVRKbGVHYzJjbmhRTXpaSU0zTklVM3A0T0VJNVV5dDVTMVJYUnpVMlRVOXNTRkE0UVdRd09VOTZUVk41V0ZoaVFtbHVkVWRSVTNwRWVIYzNOMVIzTVU1RFZtdE5hRnBCWVRkMVR6TlBTRmxDTkV4Nk4yVm5OVWgxUVNzd1QxUk9kbmRHVTFWSlVEY3ZaVUZoYkZsalJXOVhkRTVVVDJWTVNUWkdUR2h5UTBsUFIzVkhhblJxVjFGTE5YaFBSVlZ2YmxkSlpFUlJXRlpaY1dsd1NtZEdTRUYyZDBSRldHazVPRVJvUXpob2NHcFdiamhtWjA5b01EbFZVRFJ5UTFObFlVMUhObWxsTW1obk5uUXZWMmRqY25OUmRWZHFiR05pVlZRNE5uSTVUREZzZW14WE1FaGFXVFZoUzNsRVNrMHZSRGh5Y25oMWNqSXlRWFJ1U0ZOemFHSTJjMDF1TjNKYVF6UjZOemg2T0VkU01rcG9VMG8zWld4UFJIRXJlVXhOYldWSmMxZDNlbkZxWTJsUWVrcEdSRTg1YmpOMmVqQXJUbkJQWlhZd2F6aEJjVzgxTm1sSGNVRmhSRmxaVkZGbVRWbHhhbGQ1YkhCaVkxbEZhM0YwVjNKQ2RHMTVjMDFPY2tWWmVISTNTbUppZFhGa1pXTXhka3RhTmxNNEwwcHNUVlpsU1hjeFJtazNXRkJ3VEdoaVFUZzRVSGcyVm5aNFpteGFkRGxwTDNVclVWZFdSRU51VkROWlZGTjJSa0prVEV0eVEwWmhRbXQ0WjNSb05sTnZhakJ0SzBoMk5IUXdPRUZpY0RSb1JGYzFka2t2U0V0alZEWTBPRmxDVVhBMVkzSnpOak5HVWt0bVVFaENNMnBtVUhjMmRHWkRjemhoVFhBNE5qZFFSVGgzVGtwYVZGWnRTRUZMWm1jOS5BZEhzaUZrOFFBbnNiYmVwWlQtN25zc1BnSnFjMmNVcnR2eEtTblpsME1tMDVBUmtoVDZIUlpXOWs1dUlLODFZLU5VcDJ3OWJ0ajFkXzV0Q0w2aVhoUQ==","lt":"LT-377-NsfaPSdK5EgVsbSk2fBXPaKOrYX9g9-passport.51gxc.com","password":pwd,"module":"UNKNOWN","rememberMe":"false","username":"test"}
#data = {}
#data = base64.b64encode(json.dumps(data))
url = "http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false"
#req = s.post(url=url,data =data,headers = headers,cookies = cookies)
req = requests.post(url=url,data =data,headers = headers)
#location = req.headers['Location']
#print(location)
print(headers)
#print(req.content)
cookies = requests.utils.dict_from_cookiejar(req.cookies)
headers = req.headers

print ("second cookies",cookies)

#  http://192.168.6.27:6030/portals/cas?ticket=ST-282-4JYvQXgOV7DbBGemkGc9-passport.51gxc.com
#url4 = "http://192.168.6.27:6030/portals/cas?ticket=LT-377-NsfaPSdK5EgVsbSk2fBXPaKOrYX9g9-passport.51gxc.com"
#sr = requests.get(url4,headers=headers,cookies =cookies)
# cookies = requests.utils.dict_from_cookiejar(sr.cookies)
# headers = sr.headers
# print (cookies)
# print(headers)
#end