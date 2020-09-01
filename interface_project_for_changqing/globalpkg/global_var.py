#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = ''

import time
import sys
import random
import datetime
import string

from globalpkg.log import logger
from globalpkg.mydb import MyDB
#from globalpkg.mytestlink import TestLink
from globalpkg.othertools import OtherTools
from tools import sqls
from tools.gethost import pro

projectname = pro()
'''
__all__=['global_headers', 'global_name','global_time', 'global_ctime',
         'global_dtime','saofudb','testdb','mytestlink',
        'other_tools','executed_history_id', 'testcase_report_tb', 'case_step_report_tb',
         'global_cookies','global_shop_Id','global_componentAppId','global_appId'
         ]
#作业预约作业任务名称随机数生成函数
def ranstr(num):
    salt = ''.join(random.sample(string.ascii_letters+string.digits,num))
    return  salt
name = "Created_by_Python_"+ranstr(6)
#获取当前时间，为作业预约提供时间变量
now = datetime.datetime.now()
now1 = now + datetime.timedelta(minutes=5)
now2 = now + datetime.timedelta(minutes=10)
fnow1 = now1.strftime("%Y-%m-%d %H:%M:%S")
fnow2 = now2.strftime("%Y-%m-%d %H:%M:%S")
now =now.strftime("%Y-%m-%d %H:%M:%S")
'''
'''
# 根据自己的实际需要进行合理的调整
if sys.argv[1] == '1':
    logger.info('当前运行环境：测试环境')
    logger.info('正在初始化数据库[名称：SAOFUDB1]对象')
    saofudb = MyDB('./config/dbconfig.conf', 'SAOFUDB1')
elif sys.argv[1] == '2':
    logger.info('已选择运行环境：预发布环境')
    logger.info('正在初始化数据库[名称：SAOFUDB2]对象')
    saofudb = MyDB('./config/dbconfig.conf', 'SAOFUDB2')
'''
logger.info('正在初始化数据库[名称：TESTDB]对象')
testdb = MyDB('./config/dbconfig.conf', 'TESTDB')
#长庆项目库
logger.info('正在初始化数据库[名称：%s]对象',projectname)
testdb_test = MyDB('./config/dbconfig.conf', projectname)

#操作hse_work_ticket表，获取workticketid获取
sql_query_ticket_1 = sqls.ticket_1
sql_query_ticket = sqls.ticket
sql_query_ts = sqls.ts
sql_query_worktaskid = sqls.worktaskid
sql_query_worktaskid1 = sqls.worktaskid1
sql_query_work_appoint_id =sqls.appoint_id
sql_query_work_jsaid = sqls.sql_query_work_jsaid
sql_query_work_safeclarid = sqls.sql_query_work_safeclarid
sql_query_work_appointid = sqls.sql_query_work_appointid
logger.info('开始数据库查询')

temp = testdb_test.select_one_record(sql_query_ticket)
workticketid = temp[0]
#作业票数据库当前ID-workticketid
workticketid = workticketid[0]
print("workticketid",workticketid)

temp = testdb_test.select_one_record(sql_query_ticket_1)
workticketid_1 = temp[0]
#作业票数据库当前ID-workticketid
workticketid_1 = workticketid_1[0]
print("workticketid_1",workticketid_1)

temp = testdb_test.select_one_record(sql_query_ts)
#获取TS
ts = temp[0][0]
#print(ts)
ts = ts.decode('utf-8')
#TS ID
tsi = int(ts)
print("TS",ts)
#预约worktaskid
temp = testdb_test.select_one_record(sql_query_worktaskid)
worktaskid = temp[0]
#worktaskid
worktaskid = worktaskid[0]
print("worktaskid",worktaskid)

#作业任务提交worktaskid
temp = testdb_test.select_one_record(sql_query_worktaskid1)
worktaskid1 = temp[0]
#worktaskid
worktaskid1 = worktaskid1[0]
print("worktaskid1",worktaskid1)

temp = testdb_test.select_one_record(sql_query_work_appoint_id)
print("temp",temp)
sql_query_work_appoint_id = temp[0]
print("sql_query_work_appoint_id---",sql_query_work_appoint_id)
#worktaskid
work_appoint_id = sql_query_work_appoint_id[0]
print("sql_query_work_appoint_id",work_appoint_id)

temp = testdb_test.select_one_record(sql_query_work_jsaid)
#print(temp)
jsaid = temp[0]
#jsaid
jsaid = jsaid[0]
print("jsaid",jsaid)

temp = testdb_test.select_one_record(sql_query_work_safeclarid)
#print(temp)
safeclarid = temp[0]
#jsaid
safeclarid = safeclarid[0]
print("safeclarid",safeclarid)

temp = testdb_test.select_one_record(sql_query_work_appointid)
#print(temp)
sql_query_work_appointid = temp[0]
#jsaid
sql_query_work_appointid = sql_query_work_appointid[0]
print("sql_query_work_appointid",sql_query_work_appointid)
# logger.info("===关闭数据库=============")
# testdb_test.close()
'''
logger.info('正在获取testlink')
mytestlink = TestLink().get_testlink()
'''

other_tools = OtherTools()

executed_history_id = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 流水记录编号
# testcase_report_tb = 'testcase_report_tb' + str(executed_history_id)
# case_step_report_tb = 'case_step_report_tb' + str(executed_history_id)
testcase_report_tb = 'testcase_report_tb'
case_step_report_tb = 'case_step_report_tb'
'''
# 请求都携带的公用请求头、请求参数
if sys.argv[1] == '1': # 测试环境的全局变量
    global_headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'csrf': '6363382b59f6435eb243fab57ea5a5e0',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Content-Type': 'text/plain'
    }
# 's.test.saofu.cn': {'Cookie':".TEST.SAOFU.CN_SHAREJSESSIONID=9414b4c5-3413-40e1-bdf1-22a4ca6a915a"}}
    global_name = name
    global_time = now
    global_ctime = fnow1
    global_dtime = fnow2
    global_cookies = {'JSESSIONID': '633592C748EC9383220497909B5548D3noFXQx'}
    #<<class 'http.cookiejar.CookieJar'>[<Cookie JSESSIONID=1BA2A137D43FD085F06F6691E539E549 for 192.168.6.27/>, <Cookie TENANTCODE=cqsh for 192.168.6.27/>, <Cookie module=passports for 192.168.6.27/>]>
    global_shop_Id = '42'
    global_componentAppId = 'wx3f310afa2e1d86ba'
    global_appId = 'wxe78eb2fe5839397a'

elif sys.argv[1] == '2': # 预发布环境的全局变量
    global_headers = {'saofu.client.test.saofu.cn': {},'m.test.saofu.cn': {'Cookie': '10549840601068216320=ous64uC-ghJ9oTcASOu3Lucm-yxQ'},
                      's.test.saofu.cn': {'Cookie': "  .TEST.SAOFU.CN_SHAREJSESSIONID=4c709cfd-7a22-41b7-89c5-c20d13937884;"}}
    global_serial = '10549840601068216320'
    global_openId = 'ous64uC-ghJ9oTcASOu3Lucm-yxQ'
    global_product_version = '3.2.12C'
    global_protocol_version = '4.0'
    global_customer_Id = '166891'
    global_shop_Id = '42'
    global_componentAppId = 'wx3f310afa2e1d86ba'
    global_appId = 'wxe78eb2fe5839397a'
# 自己自由扩展和更改
'''