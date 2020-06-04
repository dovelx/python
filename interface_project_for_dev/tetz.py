import http.cookiejar, urllib.request
from globalpkg.mydb import MyDB
from globalpkg.log import LogSignleton
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://192.168.6.27:6030/portals")
for item in cookie:
    print(item.name+"="+item.value)
print (cookie)
print (handler)
#print(response.read().decode('utf-8'))