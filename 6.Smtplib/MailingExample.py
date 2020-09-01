import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = 'mynewmailthis@gmail.com'
toaddr = 'mynewmailthis@gmail.com'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ashok check test sub 1"
t1="college report"
t2="global report"
body1 = "<html><head><title>Excel</title></head><body></body></html>"
body2="<html><head><title>Excel</title></head><body></body></html>"
msg.attach(MIMEText(t1, 'text'))
msg.attach(MIMEText(body1, 'html'))
msg.attach(MIMEText(t2, 'text'))
msg.attach(MIMEText(body2, 'html'))

# filename = "clicksql.py"
# attachment = open(filename, "rb")
#
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#
# msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, 'newmailcreated')
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()