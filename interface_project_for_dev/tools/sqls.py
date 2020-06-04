
#操作hse_work_ticket表，获取workticketid获取
ticket = 'select workticketid from hse_work_ticket order by workticketid desc limit 1'
ts = 'select ts from hse_work_ticket order by ts desc limit 1'
worktaskid = 'select worktaskid from hse_work_ticket ORDER BY worktaskid desc limit 1'
appoint_id ='SELECT work_appoint_id from hse_safety_task ORDER BY  work_appoint_id desc LIMIT 1'

