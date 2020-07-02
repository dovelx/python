# 临时cookies
cookies = {'JSESSIONID': '2A090340302246169D9635FDD868C70DBJXfAD'}

from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,FirefoxOptions
import time
def login1():
    opt = FirefoxOptions()            # 创建Chrome参数对象
    opt.headless = True              # 把Chrome设置成可视化无界面模式，windows/Linux 皆可
    driver = Firefox(options=opt)     # 创建Chrome无界面对象
    #selenium登录测试长庆
    #driver = webdriver.Firefox()

    driver.get("http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false")

    driver.find_element(By.ID, "username").send_keys("test")
    driver.find_element(By.ID, "pwd1").send_keys("1")
    driver.find_element(By.CSS_SELECTOR, ".justUse").click()

    time.sleep(5)
    #获取JSESSIONID
    c= driver.get_cookies()
    #print (c)
    #print (c[0])
    for a in c:
        #print (a)
        if a['name'] == 'JSESSIONID':
            b=a
            #print (b)
    cookies={'JSESSIONID': b['value']}

    #cookies={'JSESSIONID': '3BAB7DF0381948EA376F907859D5321C'}
    driver.close()
    driver.quit()
    return cookies

#cookies= login()
def login():
    import requests
    import re
    from tools import tool
    import json

    url = 'http://192.168.6.27:6030/portals'
    headers ={
	"Host": "192.168.6.27:6030",
	"Connection": "keep-alive",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
	"Cookie": "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports"
}
    session = requests.Session()
    res = session.get(url=url, headers=headers, allow_redirects=False)
    #print(res.headers)
    a = res.headers['location']
    #print(a)
    cookies = res.headers['Set-Cookie']
    #print(cookies)
    searchObj = re.search("JSESSIONID=(.+?);", cookies, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        cookies = searchObj.group(1)
        print("cookies found!!", cookies)
    b = {}
    ## "Cookie": "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports; JSESSIONID=DB953EF04912C23352F4D00D89084B6E"
    b['Cookie'] = "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports; JSESSIONID=" + cookies
    #print(b)

    #2
    #url = 'http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false'
    url = a
    headers = {
        "Host": "192.168.6.27:6030",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Purpose": "prefetch",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "Cookie": "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; CASPRIVACY=""; TGC=""; JSESSIONID=cookies; module=passports"
    }
    headers['Cookie'] = b['Cookie']
    #print("headers",headers)

    session = requests.Session()
    res = session.get(url=url, headers=headers, allow_redirects=False)
    # print(res.headers['location'])
    #print("now",res.headers)
    cookies = res.headers['Set-Cookie']
    # print(cookies)
    searchObj = re.search("JSESSIONID=(.+?);", cookies, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        cookies = searchObj.group(1)
        print("cookies2 found!!", cookies)
    b = {}
    ## "Cookie": "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports; JSESSIONID=DB953EF04912C23352F4D00D89084B6E"
    b['Cookie'] = "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports; JSESSIONID=" + cookies
    # print(b)
    # print(res.content)
    resb = res.content.decode('utf-8')
    #print("rrrr",resb)
    searchObj = re.search("name=\"lt\" value=\"(.+?)\" />", resb, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        it = searchObj.group(1)
        print("it found!!", it)
    else:
        print("it not found!!")

    searchObj = re.search("name=\"execution\" value=\"(.+?)\" />", resb, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        execution = searchObj.group(1)
        #print("execution found!!", execution)

    # url = "http://192.168.6.27:6030/login"
    # res = session.get(url=url, headers=headers, allow_redirects=False)
    # print(res.headers)
    # print(res.content)
    url = 'http://192.168.6.27:6030/preLogin/getPubKey'
    res = session.get(url=url, headers=headers, allow_redirects=False)
    #print("head",res.headers)
    cookies = res.headers['Set-Cookie']
    # print(cookies)
    searchObj = re.search("JSESSIONID=(.+?);", cookies, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        cookies = searchObj.group(1)
        print("cookies3 found!!", cookies)
    b = {}
    ## "Cookie": "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports; JSESSIONID=DB953EF04912C23352F4D00D89084B6E"
    b['Cookie'] = "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports; JSESSIONID=" + cookies
    #print(res.content)
    eq = res.content.decode('utf-8')
    eq = json.loads(eq)
    #print(eq)

    USER_NAME = "test"
    password = "1"
    # loginStoken = eq['data']['loginStoken']
    encryptType = eq['data']['encryptType']
    modulus = eq['data']['modulus']
    publicExponent = eq['data']['publicExponent']
    pwd = tool.getEntryPwd(encryptType, password, modulus, publicExponent)
    #print("pwd",pwd)

    #http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false
    url = a
    #print("url",url)
    headers = {
        "Host": "192.168.6.27:6030",
        "Connection": "keep-alive",
        "Content-Length": "6248",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "http://192.168.6.27:6030",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"Referer": "http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27%3A6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
		"Cookie": "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; module=passports; JSESSIONID=DB953EF04912C23352F4D00D89084B6E"
}
    headers['Cookie'] = b['Cookie']
    #print("headers",headers)
    # data = "rememberMe=false&lt=LT-360-oR77gDeNaxkPLfZQEfkf4e76WBuDhS-passport.51gxc.com&execution=b4beb94a-066b-4f36-b49c-d20d6e11ef47_ZXlKaGJHY2lPaUpJVXpVeE1pSjkuVFN0TVJ6Vk5ja2syUTBSRmRtdEpUbHBLYnpCRk1ISkJZVlZPYW1wVk5GbFVNV1ZJVVZaTlNYZzBLMUZzVkhoTlpERlhOa0ZaYm1oRmNVUnZVR2szWVVkYVJETmhhbU0xYkRoM09HWmFRbGQ1VUdGaFNWbHJjbVZyUzBOMmFEUTNXRWxPWmxwclpWTkxSR0ZSYVdwTlpFVXJOV3hXZURaclFrOHlTMlp5TkRNdmQzVXlVbFpLT1hGcFlYQXhOemgyVFhwU1R6WTVaa0ZWYWxWS09GbFZTVWRrUVd4dVlXdFhUaXRJU0U1bWRHcEZkVFpPZUhrNEx6ZFVaV05tUXpWQlUyWjVURlo0Y1hkV1lYRkNURzV0WlRZME1IUmtNemhVZVUxRVRYUkhXVEJ4TkZGVWNHZFZWalZpVDI1QlpWZE5ZMmRPYWt4Nk5VdHROakUxU0VGTmFITjBkM2RFYmxrek1IQkllbEZNU2poWFJYbFRSVEZCUkdOMEwyZHZWbUp3Ym1aak5FMVpURXN6YlRSWU9VeHhaMHBJVGtOUmVUUjVVa1Z4VURaT2FFUjFXRTh2VUdaU1oyMVhVVUpTUWtwelpXd3hRM2R0WTJWbE1EYzBZMGhLVURaQmRHNVJPVE41VVRWQ1EwWTFZMjVaZG1SV1pXczJibXhXWjA4M1ZHeGhaV2Q0Y3paalYxWlZhR2xSUjAxQlNXTmFOSE4wT1UxTU5qTmlUbFJKUzBob05TOXBNR3BHUTBGNVlrbFhRVTVsV1ZSSFlYWkNTV2x5YWxoaGR6bEtXR28zVnpOWll6aGhhVFZJU21FclZWcEdkVk53YW1Fdk1XcG5iVTFtWm5adWMyOVZkRVp6VUZCVU15dEpLMUpOSzBodVdXNW5SMFpUTVZWcU9FOWhSVFl2WnpWdWRFcDFlVVZMV1RjMlMxUjNjbGRoZDNoeFN6RndXVWwwWVdWRFl6WndUWGhEYkdNNFVVcDJNR2xzTkRkME1GTTRUMDAzYzJOUFIwNUtRVEl2VWpObVVHVllValJIT0ZadFNuRkdVQ3RzYTFseVNWVTJTVTR2Wm5FNGFqVXdMelpHVWsxWGEwbHdVMlpoSzBGellXeHpWM2hQU1VkUWVHVlhWMlZSTVU1RGNGbEdPVWRLTDFWa1dqTmtjMmhoVVV0aE5VWndlbW8zUlM4MWEwOTRkVWhTYTNFMlMwNURSMjVpWVM5alYwbEVia2w1V1VGdU1UTnNNVzVMUjNBM1VXVlFMMElyZUhGVWJIaGxRems1UjJob1pFOUNZelp4YmxObVJuUlNRMUIxV21OcEwzcFJObVV5VldRdlEydFJNekZoUlU5bVVUUkJka3h2YjBSclp6UTNaSGRtYzFneVZHd3pTV0Z2VUZsRVZXWk9USFFyVm10b1dWSXlUa1Z0VFVKNU5rODJSMjV6Ymtvek9DOXBjV0pRUTB0RVVVbGlkWE5GUjBJMlpGVjVSbmcyZHpZclNIQkhPU3M0T1doUU1saG5VMGxXYjJwallqZDZkMjFWSzBaRWFuRTJVMWd4ZDNCSlNYZDNNWHB4WVhCSlptOUZWbEZOY1VoeVZDOUJkakp2ZFZKNVpURm1hM0ZIU1ZKbmFXWnRSMnBDVFU1aGFqbE9XbE41ZDBaSFZHMWxWMnBQU0RBemVXUXdTVFJMZW1SamF6ZFdhVkpDTW1kM01WSllhR3RKUldoMkt6SlRUMU5vVlZSdGRWUkRSWEpyZVdSS1VYRlZiM2c1VUZwdFJEZDNaRmxaTm1GMlNtSTJiaXMwZVRka2RFcDBiakJuYWs0MGN5dFROR051YkZaNU55dDVURUV3UVRGR2MwMWthVUpYZWtvdmExUjBRVTVQVWxGSlpHNVVSV0kwWWxWTFNWZ3laM04yTDBaV2EzSnBTMjV1YjBsdU9VMW9hRzFEVDJWbmJsTm9TMk5XWlZScGNuaHZkVlkyV1VVeGNGRlRaVVpxYXpoYU5GQnJhRFJ1VUZGbVduRkRNV0l4UWs0d2RVWnpUemgzYjNnd1pFSk9OMlJ2UkZsRlRIRlljbTR2U1dadVkyOUxWakp5UjFCNVUwTk5kV2hNVVc5c2RucDFhVnA1U2s5c2FteHFVVXhCVXpKMFF6ZEJNVVp3YVVjMGFrSlJjMnhESzJwdFdWcGxNRlVyV0dKSlZVUmlTbE5xV0ZOM1JtWllPRFJwTDJRMlYyTnVhMGxzVWtGMGMySjVUamhyWmxoTVJYbzNjek15WjNkS2J6UXlVazlxTlUxaFlUQjFkSFZoVW1wVU0yTTVkREJ2VmprNWRYTlFSR3BKTWxJNVZHOXhTVzVUYWpWRVZsVkZjMWN4Ums5VWRVMTRNa3MyZG1jeWIwNHdlSFppV0d3d1FXeDNNME1yT1ZwUFZWUTNNRlZRU0U1eWVHNDBWVGxpU1VGdlpESXZaV0ZyVjJoaU1ETnZLemR1UVVSd1QwVXdkWFJKTkRocVUycFdkRVpYV0hKSVpUTnNiM0U0TkVabFlXZENOeXR5TTJOa1F6bHlNMWRPUmt4R2RWaE9SM0ZIVVRkSmFuZzBVRGxXYmxwWmRGWk1ZMmw1YlZsVFNVcE5kVlpRVTBFeU1rMU9iM1JJZW1kMlVVSjRUMk5vV2xSUVN5OUJORU5VYnpWbE1VOXlhR2xqY0ZGVVNGWXhRakZ2ZFVoM2NIbDZkVXhZWnpkS2FXcGhjRmhsVjNocWNraDNVV1pYZFhSeFozRnBWRWxMU25ORFMwMDFVMlppZVZJNFpXRlFMMnRWTWpSc1oxZE9VM1lyY0ZwUFJuTmpjV2RJZURocFVYWkNZM1JaUm5KRlptdEVhRVowVUZselZ6VlBZa2Q0ZGtKSEt6VkliMXA0UVV3eFVIVkdNMmxoVVZjclFXRk1UVFF4Vm1sQlFtSkhSVTQ1WkU1blpsWXZVMkpEVmtKR1NsSmxaMUJIVEVGTlN5dFVTbVIzUVZWUU1FeEdTakEzZDB0NlZIZzVaSFpCTVhoMFZrWm5PVGhyY2xNdk5FUmhZbWs0TXpBclpWaHlObEpEUlhoV04wb3dkWEpNV2xCeWRUVkZWMDkyVkU1TFYyRmtaVlpDVkRRd2FETXZMMEYyYmk5S1NITlhiRVpWYXprd2JreFVjRlZZZDBJeE5WaFhOMW93VnpKbVptNXZUbkF4T0UxRWVHOVpZekV6Vm5CSWJXdFZPVVZYTTNGUVZVUjFOakZaVFVKemFEaGhUV3BtV1RCblZsa3ZVbkI1UVZKaWRHd3JZMGhPTldjNVVqSm1kQzlDVEd4RldsUkNWV0YxUnpscVNYbFZha1V6U0VwS2Rtb3hRbGxMWTBaTFZERnhZMUJGVUVJMVVtaHRlaXMyTkdvMFRVVjBiVXgyV1ROdVExaFJSRzRyVnpWSFRDczNNVUo1V2t4T1kxVm9aRGRvZW5wQmRqQm9TRTlSVDJSMkwwTllhM1kxY1ZWdGRtZzJkVzh6ZDBaamVtVnFLemR2U21WMlNtTlhVV3h0VUhGcWNteDJPV2x5V1RodlowbHFOa0U0UVhZNFdWbFBkVGROU0hRNU1XWk9UWGxUTmtkRGMyZHFXWGhSWlhJMGEyUkRUQ3RtU21nd1ZXNWpRVmx5Tmk5SWR6bHRVM1pCWjJOWVpVbHFZazFtYVdsUFYyUlFhVkppUW1aRWFqRTFSM2x0YlVzdlZESmpVbkF4T0UxRmNWQkJNVVkxVXpKb2VsWkpjamRNUm10b2EwcHNTbEZWUkM5UFRXRkhibmhwTkV0UVVWSkZNVVpNVml0MlNqazFiVmRGZVZoT1MxY3JNRTlVWm1oWFpWWkhkelUxUkhjclJFVnJRa3RuTWxOd1JFaGhVVGQ2WjFOS01sZ3lXR0ZxVnpoS09VVTNWVzVOVUhWeVdDdE1SekF3VXpSMGJuZE5WbGhXU2pFcmVuUnZRWGs1ZFd0aU9HTnllRnB2YWpJMksybGhNVXhqZVZWSVNsSTBSRTF6WVZkNlRHaFJNRTAzVTB0bE9IQkJSVkZrZDBFeGJqVk1lamhUWW5adGNHbGhVbkpoWW1ocFIzZEplSHBsV1RsR1RFSnlkVVZxY0V4UWVqQjNiR0U1TVVSNFVVZ3lkVzlTYzBST2JrTXpSQzlhWVhWa2JVTXZla0pJTldNdlYwVlViVlYzUkRacWFqRlNMeTlKYkVWUmVVRlZjM1JzWldkcmVFMTNTWFZaYUROMFVqWTJWRVJtUkc1SlJEQTJOMFpJUkVGM0wzQnpRMHRaUVdGS1psbHlaR3BQTXpodGJXeGtaRE15VmtOU1dpOXVSRGRtWTJacWJGRm9WRUo0TjBKcGJHTkxVVXhIYVV0T1IxbHhZVXQwZUhBNFNreENMemhUVm1JMVVsRk1SRGhqVkV4b1NIRnhNRFJ2Y0RaUVEwUlZkbXN3ZERSelVHeHBiVXh4TTFReGRXUkJRa1VyVUM5eVZuVjRVVGNyV0ZocE9GTlRkRmtyUTFZNU9XZDJNM055WVhoQldGVkxhRTUxV0RnNGFUUnlMMlZNZGxWUlYzSm5SVkJMWW1vNU1VazNMME5zY2taQ1IzazRjbVE1UWpWMk9GSXpaM1I0V201R1NtOVZNbHBtTTFkSWRrZElTMlFyU0dkb0syeHNXRXBHZW1wbFJWWldVbkZaTDNGMU1FeFVWVmRLWkU1QlpWTTVZbUl4UVhkelJGSkhia2syV1ZSWVRVOUJhbTlRWWs1aGFIZDVkMkVyUjNwNlEzSnlUa00yVDNCRU5HMDRRbWhoU2tWVGRuWkJkWGg0T0hSRFYyMW5ia2hWU201MlYwZzNlbEptY205b1VFVnpaa1oyV2xGdE4zaFlSM1pwZWxwbVltbE1NVUZYTkdSTGNtVXhWbE5EV25ONFZVNTZjMU5PUTBRMlUxcGFVbmQzTTNSdVUzVm1RWFUwT0ZVeFYzcE5jbkVyVkVaR1NFaERNSFp1VkROSWJFNUdWMlkwYTNOWmVteElNbWRHYVZRM1VrVlNWVlYzYTFGNmNFOHdZWGRNUmtGWVFsSjFOekUxZWtWWlptRlhWaTlPWlVkNE1YbGpNSEJYSzJwYUszQndVbmhIU2tjMWJtNXRVVUpvWWxneVlVMUpiMFo0YkVOaEsyUndUazlhYUROcGJXbE1SRXBITVhCbU5qYzROamRxY1hWV1NrbGxkQzkySzBSa2VIUlRUa3d2Tm1wRFpsRnBSR2RrWlhkbU1rUXljbTU2WXpRemVuVk5OWFV6S3pWUmJHcFpWMVZ1YTFRMGJqaEpOMHB0VFRaTU16QjFXRnA0ZVRoSloxVm5NWFl4TWxZMk9FUkljSEZ5TnlzM1ZuSjVUa1pLUWsxR1JXaGFlbWxRTkhCUk1FNXRlRVpDYVRoSlRHNXlWMFpaYm5sb1JYWmtkRkkxUlhwak4ydFJkRnAzWWpSclZHOURlR1l3VFdkTVRrZEdhM1psYjFaS2RWVnRUWFp5Y214UmRucHhkRFJwWjFCUVNtSnBWRU5hVDJwTVJYUjFWMlF3TUZGbmFsTlNURk5KWjJGclVXUnlSVk54VVN0Qk9XbFBlRWRpTVZNMFkzUnhUR1l5UVdZelYyWjVSM1YyTURjemJVdDFUR3BWVEVsME0wZHZWREkzVDFrOS5hVlRFWVdhRTBCcmlnR1AtZXFSamZRYVdvcmYzUEd2YXdJQ1M4Wm9aQl9yR3hCTjBEcmphSXBNdGR6QkYzR2hiWmlBdFJKNVZwLXp5TFdlbXc4cDBaUQ%3D%3D&_eventId=submit&module=UNKNOWN&password=7d3e02c8cf40a7ad7da9cd69d7dd3690981541d4c54b1db65474c55b3a6fc1d4d2b05fb4be2e3c02f10ad2d1bd22b17a6f6abdf0e21d29c5fce824bcb7b4328468ab32dd900f123149d7236eda055dd6a609b2e84c7d7a0cafd76d6d5ed325d481f39b34cb0075bed6b9c4d8078f07b6643f0f41e179d930cc6795741a46d0ff&username=test&captcha=
    data = "rememberMe=false&lt="+it+"&execution="+execution+"&_eventId=submit&module=UNKNOWN&password="+pwd+"&username=test&captcha="
    #print("data",data)
    res = session.post(url=url, headers=headers, data=data, allow_redirects=False)
    #print("tttttt",res.headers)
    #print(res.content)
    cookies = res.headers['Set-Cookie']
    #print(cookies)
    searchObj = re.search("TGC=(.+?);", cookies, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        TGC = searchObj.group(1)
        print("TGC found!!", TGC)

    headers = {
        "Host": "192.168.6.27:6030",
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Referer": "http://192.168.6.27:6030/passports/login?service=http%3A%2F%2F192.168.6.27:6030%2Fportals%2Fcas&tenantCode=cqsh&trial=false",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
        "Cookie": "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; CASPRIVACY=""; JSESSIONID=2E78CF235BDA10B18D0598E61DF752961Clnjz; module=passports; TGC=eyJhbGciOiJIUzUxMiJ9.WlhsS2FHSkhZMmxQYVVwcllWaEphVXhEU214aWJVMXBUMmxLUWsxVVNUUlJNRXBFVEZWb1ZFMXFWVEpKYmpBdUxrRjNUSFJOYmxrMVRGZFpOMlpEZGw5bFpVMU5TV2N1VnpOeFUwWklVV2REV1VrMFowMDFVRTlmZFhKclIzUm9SbFJuWmpsWExVSkRObVZZWkVaUFIwSktjbWh6VFMxNU1GcDBaRGx2YVROSVNGVnNWM0J4ZGtGSFkwNVpRbU5IVlRGblkweFFjVjltWTFGSlZpMWpielZIZFZSRVFVbEdkbTFvTTNkMVVHNTRXSGRPTkdGZlJFeGZOMnR4Wmswd2VFRlhZMjV1VUdGeGNtaHdObWRDWWpWUWRIVk1ZbTkyT0hNMFpGZE1Oemt5T0RneVlrNWtTVmQyYUdwVFVEWTFOVXRHYmxCYWIyZExhVVpxWTFwU04xQm9ORXRyYXpOeVFVWktNQzFCVFVSNU1WUjVWSFpmV2tKSE9XWlZUR2RhUjJScVkyYzVZVkpSVjNSUVV6Tm5XV1oyYW1jelZYUkxNRFJ5TFVveFZGUnhOamhqZWpCTGJXSjJNVUZTYnpsdFNVbGlkSHBGYTFkR1ZpMHdPWGN1Ym00NFFXMVVjelYxVG1kUlJXUkJNRXRVWDJWc1FRPT0.QfsbdSVn5WUO2VN8dk4AFnInusPAwufsucTQ-Nx7_eBwUQtMO5zNpoHefssNbQ-rcsyVAUF-HersY0xt6R7dKA"
    }

    b = {}
    b['Cookie'] = "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; CASPRIVACY=""; JSESSIONID=" + cookies + "; module=passports; TGC=" + TGC
    #print(b)
    headers['Cookie'] = b['Cookie']
    #print(headers)

    iturl = res.headers['Location']
    res = session.get(url=iturl, headers=headers, allow_redirects=False)
    #print(res.headers)
    a = res.headers['location']
    #print("url===", a)

    cookies = res.headers['Set-Cookie']
    #print(cookies)
    searchObj = re.search("JSESSIONID=(.+?);", cookies, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        cookies = searchObj.group(1)
        print("cookies4 found!!", cookies)
    b = {}
    b['Cookie'] = "TENANTCODE=cqsh; tenantCode=cqsh; prjidentify=cqsh; CASPRIVACY=""; JSESSIONID=" + cookies + "; module=passports; TGC=" + TGC
    #print(b)
    headers['Cookie'] = b['Cookie']
    # print(headers)

    # url = a
    # res = session.get(url = iturl,headers = headers,allow_redirects  =False)
    # print("\n\n",res.headers)
    # print("rs",res.content)

    cookies = {'JSESSIONID': cookies}
    url = 'http://192.168.6.27:6030/portals/cqsh'
    rs = requests.get(url=url, cookies=cookies)

    data = rs.content.decode('utf-8')

    searchObj = re.search("window.csrf = '(.+?)';", data, re.M | re.I)
    if searchObj:
        # print("searchObj.group() : ", searchObj.group())
        # print("searchObj.group(1) : ", searchObj.group(1))
        csrf = searchObj.group(1)
        print("csrf found!!", csrf)

    else:

        print("Csrf Not found!!")
    return cookies


if __name__ == '__main__':
    a = login()
    #print(a[0])