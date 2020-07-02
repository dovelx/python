import requests
import re
from tools import tool
import json

url = 'http://192.168.6.156/portals'
headers ={
"Host": "192.168.6.156",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Purpose": "prefetch",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
"Cookie": "TENANTCODE=clsh; tenantCode=clsh; prjidentify=clsh; CASPRIVACY=""; TGC=""; JSESSIONID=16AEA3A89531FCED26F7281D443322E9m3EJdy; module=passports"
}

session = requests.Session()
res = session.get(url=url, headers=headers, allow_redirects=False)
print(res.headers)
a = res.headers['location']
print(a)
cookies = res.headers['Set-Cookie']
print(cookies)
searchObj = re.search("JSESSIONID=(.+?);", cookies, re.M | re.I)
if searchObj:
    # print("searchObj.group() : ", searchObj.group())
    # print("searchObj.group(1) : ", searchObj.group(1))
    cookies = searchObj.group(1)
    print("cookies found!!", cookies)
b = {}
b['Cookie'] = "TENANTCODE=clsh; tenantCode=clsh; prjidentify=clsh; CASPRIVACY=""; TGC=""; JSESSIONID="+cookies+"; module=passports"
print(b)
url = a
headers = {
"Host": "192.168.6.156",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Purpose": "prefetch",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
"Cookie": "TENANTCODE=clsh; tenantCode=clsh; prjidentify=clsh; CASPRIVACY=""; TGC=""; JSESSIONID=cookies; module=passports"
}
headers['Cookie'] = b['Cookie']
print(headers)
session = requests.Session()
res =  session.get(url = url ,headers=headers,allow_redirects  =False)
#print(res.headers['location'])
#print(res.headers)
#print(res.content)
resb = res.content.decode('utf-8')
searchObj = re.search("name=\"lt\" value=\"(.+?)\"/>", resb, re.M | re.I)
if searchObj:
    # print("searchObj.group() : ", searchObj.group())
    # print("searchObj.group(1) : ", searchObj.group(1))
    it = searchObj.group(1)
    print("it found!!", it)

searchObj = re.search("name=\"execution\" value=\"(.+?)\"/>", resb, re.M | re.I)
if searchObj:
    # print("searchObj.group() : ", searchObj.group())
    # print("searchObj.group(1) : ", searchObj.group(1))
    execution = searchObj.group(1)
    print("it found!!", execution)

url = "http://192.168.6.156/login"
res =  session.get(url = url ,headers=headers,allow_redirects  =False)
print(res.headers)
#print(res.content)
url = 'http://192.168.6.156/preLogin/getPubKey'
res = session.get(url = url,headers = headers,allow_redirects  =False)
print(res.content)
eq = res.content.decode('utf-8')
eq = json.loads(eq)
print(eq)

USER_NAME = "clshadmin"
password = "1"
#loginStoken = eq['data']['loginStoken']
encryptType = eq['data']['encryptType']
modulus = eq['data']['modulus']
publicExponent = eq['data']['publicExponent']
pwd = tool.getEntryPwd(encryptType, password, modulus, publicExponent)
print(pwd)


url = 'http://192.168.6.156/passports/login?service=http%3A%2F%2F192.168.6.156%2Fportals%2Fcas&tenantCode=clsh&trial=false'
url = a
headers = {
"Host": "192.168.6.156",
"Connection": "keep-alive",
"Content-Length": "6248",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"Origin": "http://192.168.6.156",
"Content-Type": "application/x-www-form-urlencoded",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Referer": "http://192.168.6.156/passports/login?service=http%3A%2F%2F192.168.6.156%2Fportals%2Fcas&tenantCode=clsh&trial=false",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
"Cookie": "TENANTCODE=clsh; tenantCode=clsh; prjidentify=clsh; CASPRIVACY=""; TGC=""; JSESSIONID=16AEA3A89531FCED26F7281D443322E9m3EJdy; module=passports"
}
headers['Cookie'] = b['Cookie']
print(headers)
#data = "username=clshadmin&pwd1=307530f148fa4f0f01ee69721f35408fda163097e64ec836e3a86e387ffa1d5b30a172c3364ee9ae37daacf513ab7e9260751765066a1266a1b8c7a2cfd459c0add917a00fbc3c94e64a85207dd59cb85fb19c50022137ffbeb864750d7171f43a63daef4cec6509ae8bb6efdf3361b5a3dea1a23b6cd7962a722425863e54cf&captcha=&rememberMe=false&lt=LT-8-Hioe1oQUJTh6v33bWIMLoDZZI5tQgm-passport.51gxc.com&execution=39daa5d3-2965-4657-8756-d0803f6f0d6b_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuUzBaNFowUlpaVlZtZDNGb05YbEZVamRqSzNVd01HTnJlSFpqVHpWbmVUaEZibmxHV0RWWk9USlBiRkJEWm5ZNFZVZE1jMk53ZGtGdU4zcFFSamRXYUcxQmFubGxja3R4V0dkaWRHTkxWVUZsY0hkWVJYSnNSVk53ZG1KRk1rMVFjWFpwWW1JcmIwbE9lVElyVmxBMFRUTkJjVmxtVmxKa2RYa3dVVFJtUjBweVdYaGxZekZIYm1OeVMzbEJla2xUVVU1WFltZENlRUV5Wml0dWFFc3ZOek5DS3pWbWVVOTVPR1pzU1d4bGRFNXpObE5aV1ZWblQwNW1aamRzV1hBeFNFZG5iRkF6WXpBeVUwRnRjWFZwTDBOdVJGTkhjRTAzUm5oelowSlBWazVQT0ZWS2NXNXdLMWc0TTJ0a2IzaFpjMGhpWkhGbVZWTndiRU5FVlhrMUx6UktUV1p1Ym5waWJVaG9ORFpOVFZCSlJteE9jSEl5UVhvd1NtUkNhV1l3YWtaR2QyZ3ZkVUZsYVd0M2N6ZGljbmhxWlZBMWQxUkpNWFpSYlZSRU4wNVFVbUZ5U21OblNpOW9jMnBFVUdKMmRGRnFhVmR3YlRKTWFGUXdPVEkwTmxONWVVWlNNM28xU1ZkVGNFMXhhMm94UlZwb2RtUkVSMDB6ZG5wQlZFOW1ha1ZSYWxwNGMxUmpNRzB5TDNob1ducFhNRUkwUkc1SmFtSkJiemxIV2tKeVFqUm1TalJyUjNwc05VSXZaR1psTTJFMmVIVlVaelp5VkhKTmNsSmlVRkV6UVZZdk1sQTBhWGQ0TUZaRmVtWlZaR3AxV20xNE9XcHFlVXBKVWxCRVNXMXpWR2RGTDFoV1ZUUkplVWdyTjNKSFVGZFNja0ZJT1ZKS1NVOW5aRUVyYm5oaVVHaHdLMUF5TlRWU1EybG5aVmMyZEUxU1ZqQktXRUpKUTNwS1owOUpSMlpYY1ZsaVVIcG9RVGRPTW5wWUswcGFaa0l3TVhoVVZsbFFWak51ZUdWS09XUlNTVkZKWnpsM2QwdzFXRzlZYkZnd1RHaEtWRkZCTms1UmFVTlVSRVpJVjBaRFoyWXlVbGxvZFhGWUx5OXRNR3haVlhOSVRXVlBaVFJvUlVvMU1HZFBRV1ZxUVVSVVFtdDZaVU5PWkZKNk4wRkxjMkpJVERRcmNFTnpPR2d4YlRkeGJESm9WRmwwTlcxaFNrWmFkamN6YjNkbmVGQjNTMDVrUWxCMlR6Qk1TR2RrTHpGMGRXMTBWRmRPWlc5UFpIWmxNRlpEVkZwS2F6RnFkM0JwZVhJeFVXRldjMFpTYXpSeWEzUnZaMEZWVG1FMVJVTXhNRGRUVFdkd1lWVkpaVmw2UTFSb2NURnpWMHgxWXpsV1oxazBaRGN4UzJ4Vk5uSkpabVJOTUdsUWFUWmhRV0ZuWldOM2IzaFdjWEp0VXpZNFEwUkpPRzk0UkRKNVNHUkpZV0phTmsxNVRWRkZSVEJ3UW1zMFRVMDVhMlpZWjI1eGFEQm5TV3QyTUc5U2JuSmtkM0EzTTBWd1VtVnBVMEpEU0ZOMldXbFpWVzVJTmxweFYxWnFjbk53V2s1dFFrbFNhbVp2TldvMWRqSnhhVmxKVGt0RFpWRkJNVWxvV1ZwTmF6TjVOV293VjBGck5uWXplVFI2YmxCUWN6ZDNPREpJYm1jMGVWUkVkV2RzT1dsd2QxRnJSRWxtYkdWR05rcHBVa1pWWm1acGVEUkdRMjlVWjBsMGVYaGlRVGRJV1hCTmNEWmtkbU14UlRjNVQwbzRiaXRWUTFRM1RGSTRUQzlqTlVsaFFuRm1aa0Y2WTFSUFJWcFJVamMzWmxOd2VFc3djMVYzT0ZGd1ozbFVWazVCVmtoQmRVWkNXVTVSV0dKWVFqZHdUVWx0VTNGV2EwZEdSSHBXZGxNdlRHbzVZVEU0WlZwWWQybFBkV1pNVEhvMFdEUk5Ua2xhYlc0NFpFRktjRlpIUkhKWFlVZ3hTbmRTU0dKNmQyeExRazFHWjJWMVpGZDJhbVpyY21Oc1dFZDBXbFZwVEhSNGMwOXpZVGd3YlRscGExRlFUMjgxWm5kdlJVOUdkR3R0ZWpsU1VrUnRiRmhVUjA5VGEwNWtkbmxVT0haUmVETXpNQzh2TlVGYVRHVkZiRmsxYWpBelpFRk9ZaXN6UzNabU1HMTZLMVJHUWtJNGFraEVUU3RDV0RnM2QzZEZOV05tU1RSNWNWcEZkVEpaTVV4bU1sVkdUMlpIVFRFd1FWSktZbWxEY1hOaGIzQnBhRkZsUTJoUmNXY3lRVXRWVWpKcFQwSlJjek54VVdjMFJtNWllVzFCYVZCVVRVOU5aR1YyV0doR1EwRlFaRXh6TDIwd1QyMXJUVkJTY21wb1IxcGFkbXhKT0RsaFNWcG9lRVJFWmxCMldUQnZWWGN5YTNNMFRYbDZUVE4zZERNMGFFMVNRV0kxTmpjM2NEWjRVRlJaUzBOWGRIUlljSGxWTlZReVJHWjFSbmd5U2podE1YaGxZa3d4Y1RGc1NrdFVMeXRpYmt0VWR6WTJTbVpYYkRsSlIxcFJkbXR2WWpsdWVXRkVXRnBwV0VKSWVtY3hVV1JFVFhvM1UwSlNRMWRyZDAxUVIxZ3pWbTEzUkZaNGFrTk5lR01yTUVweE9WUkxRMWhUVlZkalkyTTVla05OVlRSaVZqQkhOMFZQZUVJM1dHc3dRa3BUVmpGMFZWSlBWVzVoTjFNemJWQmFVMVpET1RSMU1WSldUMFpYWW1ZMkwwUkNjVmxuVW5SMGIyVndORFpEVFVKcFVsRkJTMnBVT0U5UWVFMVVMMUJOYURrcmVGVXlibTlMVUZvNFpIcFFZMHRLY2xWbGRIbGtaRWhHTlZOa1psaFVUM2RVZW5Sb2NFcHVVbEpoY1ZkYWVEaENVa1V4TVVKS05taHhaVlpWT0dJeVQzbFFjVGhSV0VKNVVscHBjRzl3VEdOMFZFWktjMXBwVkU5NVYxUXJXSGRFY2tOS00wZzBMMkpJU1VsUFRWZHNTVEZVTVRoWlprMDBTR051VVRsR1FYWmFiV2x1V1Zwa1YwUm5jRWhYUmpsb1VuRkRlbk51VFRZcmRsRkxkSEkwZGtwTGJtbHNSekZOUVhKWVVsWmtRbFl2THpSTWRFOVRZbGhEYVdwMldFa3hUa0ZVZW5STldFNVFOREZSZERWUVEzVkxiWEp2VkRSTlEwRnRWVkIwSzJ0SVZVRkNTM2xzYURKUVRWUXlRWG93TURsdVZFNWFOVGxLYjJJck9TOVVPSE5NY2tZM05ISm5UVFZ1YTNScFYyWk5WVVJIZFVoVmRGcDVXVlpNY2t3cmFXczFWMmxYUlVWc2NWbERiVlJsVUhBclNtSm1PRkE0VnpWT1RVa3liekIwVm5kemJUQlhaV04zWm1wT0szZEtTa2R6T1ZSalExSnhlVzExYzNGWlFXWTBhelk0Tm1oRFN5OXdTVUZaUjNGd1oyTkNjR1JzTW1OaFYzbHpkRzVPYTFsWFZuUktjMHBzUkVsT05YbHpkM05hUkU1RE0wWjZjVGh0VjBGalZEQXljMGt6YUc1VVlYWXJiM2R2ZWs4MVVFaHFhMDA0YjJNelpVWTFNbWQwYzNZMlNHMW9hVUpGTDBaV2FrUjZUVTUzV0ZOcmVuTkVNbEF3ZUd4YVIxRllkSFF6UVZweE5GaG1ibFp1YjFCM2JUVkpkMlIzTkRjM09ESXZUSEk0VEc5UWNFMUpZVFowVDFWYVdrNDFjbTVNWlVjNGNFWnlWbE0wZDNCcmJYQnlXalY0Tlc5UFJGTk1kbEYyWjA1MVdHMW1iR1JqUlhack9GRllRa2tyVHpVMU9VRnlOV2RPUzNSSVdtaHBNV1JUUVhWQ1REWjNRbmx4TDNjeFJETlZMM0ZQWjNRMlJubENhSFpJYXpNek9Ga3dURFF5V0hKWVMzSk9WamRIV1ZCb1dVbGhSV0ZOUW14bEsxVTNNMjFVWm1jNVYwTkJOWFV3WkhWeVZsZ3JWbk4zTnpKMmVYQXhTVEZQZGpSeFdtUk5PSE5zT0RKSE4xUlpPRmRySzNrMlprZGhUbnA0TjNoU1IzQlhVbXBOWkhGb1IzSkxZVFpoUjI1Sk4xVlRTMlpIVVhWNGNYaHBWR281VG5WWWQybFNWRUZJVVhwTVZrUkhTbkU0Vm5SeFJGUmtNRkZwZGpCQmQwOVBhRVJYYjJSSlZUVlJialJ5UkM5cWRsTnJVa1pXYlhkdVVGaEdVM0kyZDNWalYzTXdRME5LU1doT1ZrZDZZWEJGT0ZOa1UxVk9NMWw0Y21FeWVETnVVVzFvVTB0eGR6ZHRUa3A2U2xSNE1WSkRTekZQVlZScGFteDRZa2x5VEdKUmJURnlaekI1VURoamJWRTNORll4ZWxnNEwxbG1WR1oyT1VwVlVUSm9VWEF2THpOYWMyaHdSV2xHWW0weGVFVnlLMEk0ZFdKb2RsbEVVbWRNY214Wk5tcGpOMHBQUkdwR1pGWk5kVFk0TnpRemNrcDJNekJGVUhkMGJrMDVNM0pRZDBWMllWRm5VbTE2VlRkTVIxUkhWbTF3VkdGS2NFTXlOMGxVVGxaamR6QXlZbEl5ZW5WQmJtaEpiVWQyZVRGUlMzSTJUbkF5VTBnM2IxVnhUekJNVms1NGJIZDVTbFV2WmxkeFpsa3lVREFyVEd3dlZrVmxXa2wwTldsU1NqTXljMWt4UVhveVUwdFBUVVZaVldWTU9YZFFLell4V0hZNFZtMVpNbGx4VGpaalZ6ZDNPVFE0YldGVkwydGpNRkJhV205NEswNXRhM0J1UjI1U05YZEpVWGRGZDFsdWJtdzBOekl2ZWtwTWFuSnZjM2c0ZFV4R2VIVXlUSFZYZWxReVpXMVBaRVZ0UVVsMVdUTXZjVVptZGxWM1oxRlpWR2RFVUVWcE9UTXpXWGg1YnpZMGJHdzJaeTlzWTFCTlpHVXJPV1ZpZG5ocGNXMTZXbVJwUVhJNU5GWmphRVE1YmtnM00xcERVMG9yUkZGclVYaHpWVVphUlZWcVptUm5VVEZ2U205c05uVjRNakZoVTI1UFpUaFhibGRxZGk5akt5OVFSa1poVVVoSGJtSnNkMlppVUhkeGIwMUZUMGxuWmsxaE1VRnRhMlJMZWxnd1MyOUJUalpYUTFrNVZXdDRjVzlaY1ZwbWNUUnZWRTFsVFM5c1UwZ3llbk5vSzJsa1pVRlZTU3RJUW1Jd1dUSlViMnBEV1dGVlpEbHRXWEI1Tml0ek1pOUdWM0p2TkRSRFZYYzBkVE54UVRWYVozWjVNR2swVWs1cVkwWTFibko0VWtwMFJIcGFielZUVGtsSmRqRlJQVDAucHctY2V0RWZiT012UXU2X3Q0T3ozT29DVXEyZWMyYUtJS1NyNndmYUo1YmVxdDU3VHlDYjV6bnN5U25FLUFLdmZHcm1xWmx1bjRIQ19GekRGRjFIaEE%3D"&_eventId=submit&module=UNKNOWN&password=307530f148fa4f0f01ee69721f35408fda163097e64ec836e3a86e387ffa1d5b30a172c3364ee9ae37daacf513ab7e9260751765066a1266a1b8c7a2cfd459c0add917a00fbc3c94e64a85207dd59cb85fb19c50022137ffbeb864750d7171f43a63daef4cec6509ae8bb6efdf3361b5a3dea1a23b6cd7962a722425863e54cf"
data = "username=clshadmin&pwd1="+pwd+"&captcha=&rememberMe=false&lt="+it+"&execution="+execution+"&_eventId=submit&module=UNKNOWN&password="+pwd
res = session.post(url =url,headers=headers,data=data,allow_redirects = False)
print(res.headers)
cookies = res.headers['Set-Cookie']
print(cookies)
searchObj = re.search("TGC=(.+?);", cookies, re.M | re.I)
if searchObj:
    # print("searchObj.group() : ", searchObj.group())
    # print("searchObj.group(1) : ", searchObj.group(1))
    TGC = searchObj.group(1)
    print("TGC found!!", TGC)

headers = {
"Host": "192.168.6.156",
"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Referer": "http://192.168.6.156/passports/login?service=http%3A%2F%2F192.168.6.156%2Fportals%2Fcas&tenantCode=clsh&trial=false",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
"Cookie": "TENANTCODE=clsh; tenantCode=clsh; prjidentify=clsh; CASPRIVACY=""; JSESSIONID=2E78CF235BDA10B18D0598E61DF752961Clnjz; module=passports; TGC=eyJhbGciOiJIUzUxMiJ9.WlhsS2FHSkhZMmxQYVVwcllWaEphVXhEU214aWJVMXBUMmxLUWsxVVNUUlJNRXBFVEZWb1ZFMXFWVEpKYmpBdUxrRjNUSFJOYmxrMVRGZFpOMlpEZGw5bFpVMU5TV2N1VnpOeFUwWklVV2REV1VrMFowMDFVRTlmZFhKclIzUm9SbFJuWmpsWExVSkRObVZZWkVaUFIwSktjbWh6VFMxNU1GcDBaRGx2YVROSVNGVnNWM0J4ZGtGSFkwNVpRbU5IVlRGblkweFFjVjltWTFGSlZpMWpielZIZFZSRVFVbEdkbTFvTTNkMVVHNTRXSGRPTkdGZlJFeGZOMnR4Wmswd2VFRlhZMjV1VUdGeGNtaHdObWRDWWpWUWRIVk1ZbTkyT0hNMFpGZE1Oemt5T0RneVlrNWtTVmQyYUdwVFVEWTFOVXRHYmxCYWIyZExhVVpxWTFwU04xQm9ORXRyYXpOeVFVWktNQzFCVFVSNU1WUjVWSFpmV2tKSE9XWlZUR2RhUjJScVkyYzVZVkpSVjNSUVV6Tm5XV1oyYW1jelZYUkxNRFJ5TFVveFZGUnhOamhqZWpCTGJXSjJNVUZTYnpsdFNVbGlkSHBGYTFkR1ZpMHdPWGN1Ym00NFFXMVVjelYxVG1kUlJXUkJNRXRVWDJWc1FRPT0.QfsbdSVn5WUO2VN8dk4AFnInusPAwufsucTQ-Nx7_eBwUQtMO5zNpoHefssNbQ-rcsyVAUF-HersY0xt6R7dKA"
}

b = {}
b['Cookie'] = "TENANTCODE=clsh; tenantCode=clsh; prjidentify=clsh; CASPRIVACY=""; JSESSIONID="+cookies+"; module=passports; TGC="+TGC
print(b)
headers['Cookie'] = b['Cookie']
print(headers)

iturl = res.headers['Location']
res = session.get(url = iturl,headers = headers,allow_redirects  =False)
print(res.headers)
a = res.headers['location']
print("url===",a)

cookies = res.headers['Set-Cookie']
print(cookies)
searchObj = re.search("JSESSIONID=(.+?);", cookies, re.M | re.I)
if searchObj:
    # print("searchObj.group() : ", searchObj.group())
    # print("searchObj.group(1) : ", searchObj.group(1))
    cookies = searchObj.group(1)
    print("cookies found!!", cookies)
b = {}
b['Cookie'] = "TENANTCODE=clsh; tenantCode=clsh; prjidentify=clsh; CASPRIVACY=""; JSESSIONID="+cookies+"; module=passports; TGC="+TGC
print(b)
headers['Cookie'] = b['Cookie']
#print(headers)

# url = a
# res = session.get(url = iturl,headers = headers,allow_redirects  =False)
# print("\n\n",res.headers)
# print("rs",res.content)

cookies = {'JSESSIONID':cookies}
url = 'http://192.168.6.156/portals/clsh'
rs = requests.get(url= url ,cookies =cookies)

data = rs.content.decode('utf-8')

searchObj = re.search("window.csrf = '(.+?)';", data, re.M | re.I)
if searchObj:
    #print("searchObj.group() : ", searchObj.group())
    #print("searchObj.group(1) : ", searchObj.group(1))
    csrf = searchObj.group(1)
    print("csrf found!!",csrf)

else:

    print("Csrf Not found!!")
