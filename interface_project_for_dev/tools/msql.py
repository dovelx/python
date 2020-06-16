#m
import os

from pyh import *
from globalpkg.log import logger
from globalpkg.global_var import testdb_test
from globalpkg.global_var import case_step_report_tb
from globalpkg.global_var import testcase_report_tb
from globalpkg.global_var import executed_history_id
#from cmain import executed_history_id
from globalpkg.global_var import other_tools


sql_query_work_appointid = 'SELECT worktaskid from hse_work_task WHERE workname like "name";'
def sql_query_worktaskid(name):
    hse_work_task = "hse_work_task"
    logger.info('正在查询测试用例总数')
    query = 'SELECT worktaskid FROM ' + hse_work_task + ' WHERE workname = %s'
    data = (name,)
    result = testdb_test.select_one_record(query, data)
    worktaskid = result[0][0]
    logger.info("===关闭数据库=============")
    testdb_test.close()
    return worktaskid