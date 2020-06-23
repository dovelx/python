#pc
#操作hse_work_ticket表，获取workticketid获取
ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
ts = 'select ts from hse_work_ticket order by ts desc limit 1'
worktaskid = 'select worktaskid from hse_work_task ORDER BY created_dt desc limit 1'
worktaskid1 = 'select worktaskid from hse_work_ticket ORDER BY worktaskid desc limit 1'
appoint_id ='SELECT work_appoint_id from hse_safety_task ORDER BY  work_appoint_id desc LIMIT 1'
sql_query_work_jsaid='SELECT jsaid from hse_safety_analysis ORDER BY  jsaid desc LIMIT 1'
sql_query_work_safeclarid='SELECT safeclarid from hse_safety_disclosure ORDER BY  safeclarid desc LIMIT 1'
sql_query_work_appointid ='SELECT work_appoint_id from hse_work_appoint ORDER BY  work_appoint_id desc LIMIT 1'
