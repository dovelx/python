from mobile import mydb
from globalpkg.global_var import logger

testdb = mydb.MyDB('./config/dbconfig.conf', 'CHANGQING')
'''
sql_update = 'UPDATE ' + case_step_report_tb + ' SET runresult=\"%s\",reason=\"%s\", protocol_method=\"%s\", runtime=\"%s\"' \
                                               ' WHERE executed_history_id = %s AND testcase_id = %s AND step_id = %s' \
                                               ' AND project=\'%s\' AND testplan=\'%s\''
data = ('Block', '%s' % e, protocol_method, run_time, str(case_executed_history_id), self.testcase_id, step_id,
        self.testproject, testplan)
'''
sql_query_ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
sql_query_ts = 'select ts from hse_work_ticket order by ts desc limit 1'
sql_query_worktaskid = 'select worktaskid from hse_work_ticket ORDER BY worktaskid desc limit 1;'
logger.info('正在更新步骤执行结果')
#testdb.execute_update(sql_update, data)
temp = testdb.select_one_record(sql_query_ticket)
#temp = temp.decode('utf-8')
workticketid = temp[0]
workticketid = workticketid[0]
print(workticketid)

temp = testdb.select_one_record(sql_query_ts)

print(temp)
ts = temp[0][0]
print(ts)
ts = ts.decode('utf-8')
ts = int(ts)
print(ts)
temp = testdb.select_one_record(sql_query_worktaskid)
worktaskid = temp[0]
worktaskid = worktaskid[0]
print(worktaskid)
testdb.close()