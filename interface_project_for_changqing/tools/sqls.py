#pc
#操作hse_work_ticket表，获取workticketid获取
#ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
#SELECT workticketid FROM `hap_hse_cqsh`.`hse_work_ticket` WHERE worktype = 'shex' ORDER BY `created_dt` DESC LIMIT 1
ticket = "SELECT workticketid FROM `hap_hse_cqsh`.`hse_work_ticket` WHERE worktype = 'shex' ORDER BY `created_dt` DESC LIMIT 1"
ticket_1 = "SELECT workticketid FROM `hap_hse_cqsh`.`hse_work_ticket` WHERE worktype = 'xkz' ORDER BY `created_dt` DESC LIMIT 1"
ts = 'select ts from hse_work_ticket order by ts desc limit 1'
#连续号-作业任务添加ID
worktaskid1 = 'select worktaskid from hse_work_ticket ORDER BY created_dt desc limit 1'
#断号
worktaskid = 'select worktaskid from hse_work_task ORDER BY created_dt desc limit 1;'
#worktaskid = 'select worktaskid from hse_work_ticket ORDER BY workticketid desc limit 1;'
appoint_id ='SELECT work_appoint_id from hse_safety_task ORDER BY  work_appoint_id desc LIMIT 1'
sql_query_work_jsaid='SELECT jsaid from hse_safety_analysis ORDER BY  jsaid desc LIMIT 1'
sql_query_work_safeclarid='SELECT safeclarid from hse_safety_disclosure ORDER BY  safeclarid desc LIMIT 1'
sql_query_work_appointid ='SELECT work_appoint_id from hse_work_appoint ORDER BY  created_dt desc LIMIT 1'
