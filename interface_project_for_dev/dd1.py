from sendmail import MyMail

mymail = MyMail('./config/mail.conf')
mymail.connect()
mymail.login()
mail_content = 'Hi，附件为接口测试报告，烦请查阅'
mail_tiltle = '【测试报告】接口测试报告' +"hi"
#logger.info(html_report.get_filename())
html_report = "E:\\report\\report_for_no_htmldoc_generated.html"
html_report1 = "E:\\report\\report_for_no_htmldoc_generated1.html"
#attachments = set([html_report],[html_report1])
attachments = [html_report,html_report1]
#attachments = set([html_report1],)
mymail.send_mail(mail_tiltle, mail_content, attachments)
mymail.quit()