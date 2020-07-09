import requests

url = "http://192.168.6.156/hse/HSE_TICKET_MBCD/cardSave?parentEntityId=&parentFuncCode=&topFuncCode=HSE_TICKET_MBCD&0.2025916230224747&contentType=json&ajax=true&tid=2000000001003"

payload = "{\"tableName\":\"hse_ticket_mbcd\",\"columnValues\":null,\"dataStatus\":0,\"ver\":1,\"created_by\":null,\"created_dt\":\"2020-07-01 18:02:35\",\"updated_by\":null,\"updated_dt\":\"2020-07-01 18:02:35\",\"df\":\"0\",\"tenantid\":2000000001003,\"ts\":null,\"blind_type\":\"flat\",\"workstatus\":\"jia\",\"normalproductionstatus\":\"chou\",\"commenceperiodstatus\":\"jia\",\"downmaintenancestatus\":\"jia\",\"mbcdnumber\":\"ç²æ¿ç¼å·ç²æ¿ç¼å·\",\"territorialunitid\":2000000005066,\"territorialunitname\":\"ç¼æ²¹ä¸é¨\",\"territorialunitcode\":\"000000010300\",\"device\":\"è£ç½®åç§°\",\"worksite\":\"å®è£/æé¤ä½ç½®\",\"blindplate_material\":\"ç²æ¿æè´¨\",\"pressure\":\"å·¥ä½åå\",\"temperature\":\"å·¥ä½æ¸©åº¦\",\"medium\":\"å·¥ä½ä»è´¨\",\"pidnumber\":\"å¾å·\",\"blindattaches\":\"[{\\\"dfs_file_name\\\":\\\"å¾®ä¿¡å¾ç_20200617160345.jpg\\\",\\\"tableName\\\":\\\"sy_attach_dfs\\\",\\\"dfs_id\\\":2000000012452,\\\"dataStatus\\\":0,\\\"ver\\\":1,\\\"created_by\\\":null,\\\"created_dt\\\":\\\"2020-07-01 18:03:35\\\",\\\"updated_by\\\":null,\\\"updated_dt\\\":\\\"2020-07-01 18:03:35\\\",\\\"df\\\":0,\\\"tenantid\\\":2000000001003,\\\"ts\\\":null,\\\"dfs_file_group_name\\\":\\\"group1\\\",\\\"dfs_file_key\\\":\\\"M00/00/28/wKgGnF78X3eAPyASAAExXFSqfEE865.jpg\\\",\\\"dfs_file_size\\\":78172,\\\"dfs_preview_url\\\":\\\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF78X3eAPyASAAExXFSqfEE865.jpg\\\",\\\"dfs_thumbnail_url\\\":\\\"http://192.168.6.156:8888//group1//M00/00/28/wKgGnF78X3eAWOeLAAIKVnDfoY0767.png\\\"}]\",\"design_pressure\":\"è®¾è®¡åå\",\"dn\":\"20\"}"
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'csrf': 'ce99098e0f9d4b459f7280d8d19ed693',
  'X-Requested-With': 'XMLHttpRequest',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
  'Content-Type': 'text/plain',
  'Cookie': 'JSESSIONID=B0DB71A3E8DD570C2CA0EC1151603A28WQrnN5'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
