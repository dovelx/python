import requests

url = 'http://192.168.6.27:6030/preLogin/getPubKey'
result = requests.Session()
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
response = result.get(url, headers=header, allow_redirects=False)

location = response.headers['Location']
print(location)
print(response.cookies)
headers={

     'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Origin':'http://192.168.6.27:6030'
    }
# 注意有些header返回的Location中的url是不带host部分的，需要注意一下