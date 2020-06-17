from runners import pc_login

list_a = []

list_a = pc_login.login()
cookie = list_a[0]
csrf = list_a[1]
#作业预约请求头
headers={
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': csrf,
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain',
    }