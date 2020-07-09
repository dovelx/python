# -*- coding: utf-8 -*-
import xlrd
import sys
import os
from globalpkg.log import logger
import imp

imp.reload(sys)


def test_case_in_excel(test_case_file):
    test_case_file = os.path.join(os.getcwd(), test_case_file)      # 获取测试用例的路径
    if not os.path.exists(test_case_file):
        logger.info('测试用例excel文件不存在或路径有误！')
        sys.exit()      # 找不到指定测试文件，就退出程序 os.system("exit")是用来退出cmd的
    test_case = xlrd.open_workbook(test_case_file,encoding_override="utf-8")      # 读取excel文件
    table = test_case.sheets()[1]       # 获取第2个sheet，下表从0开始

    '''读取表格中的用例，其实就像一个二维数组'''
    for i in range(1, table.nrows):
        api_id = str(int(table.cell_value(i, 0))).replace("\n", "").replace("\r", "")
        caseid = str(int(table.cell_value(i, 1))).replace("\n", "").replace("\r", "")
        casename = table.cell_value(i, 2).replace("\n", "").replace("\r", "")
        result = table.cell_value(i, 3).replace("\n", "").replace("\r", "")
        url = table.cell_value(i, 4).replace("\n", "").replace("\r", "")
        data = table.cell_value(i, 5).replace("\n", "").replace("\r", "")
        #data = table.cell_value(i, 5)
        print(data)
        sign = table.cell_value(i, 6).replace("\n", "").replace("\r", "")
        flag = table.cell_value(i, 7).replace("\n", "").replace("\r", "")
        isactive = table.cell_value(i, 8).replace("\n", "").replace("\r", "")
        exresult = table.cell_value(i, 9).replace("\n", "").replace("\r", "")

        #print(api_id,caseid,casename,url)

        testsuit = []
        caseinfo = {}
        caseinfo['id'] = 1
        caseinfo['name'] = ''
        caseinfo['result'] = ""
        caseinfo['url'] = ''
        caseinfo['data'] = {}
        caseinfo['sign'] = ''
        caseinfo['flag'] = ''
        caseinfo['isactive'] = ''
        caseinfo['exresult'] = {}

        caseinfo['id'] = caseid
        caseinfo['name'] = casename
        caseinfo['result'] = ""
        caseinfo['url'] = url
        caseinfo['data'] = data
        #caseinfo['data'] =  caseinfo['data'].replace("\\","")
        #caseinfo['data'] = caseinfo['data'].decode('utf-8')
        caseinfo['sign'] = sign
        caseinfo['flag'] = flag
        caseinfo['isactive'] = isactive
        caseinfo['exresult'] = exresult

        testsuit.append(caseinfo.copy())


        # try:
        #     # 调用接口请求方法
        #     status, res = interface_test(api_id, api_name, api_host, api_url, api_method, api_data_type, api_request_data, api_check_point)
        #     if status != 200:
        #         # append()只接受一个参数,所以四个参数要用一个括号括起来
        #         # 请求失败，则向error_case中增加一条记录
        #         error_case.append((api_id + " " + api_name, str(status), api_host + api_url))
        # except Exception as e:
        #     Logger().error(e)
        #     Logger().info("第{}个接口请求失败，请检查接口是否异常.".format(api_id))
        #     # 访问异常，则向error_case中增加一条记录
        #     error_case.append((api_id + " " + api_name, "请求失败", api_host + api_url))
    #return error_case
    #logger.info("%s",testsuit)
    #testsuit = testsuit.decode('utf-8')
    return testsuit

if __name__ == '__main__':
    a= test_case_in_excel("test_case_file.xlsx")
    print("\n\n",a)
    #print("\n\n", a[0].replace("\\\\","\\"))

