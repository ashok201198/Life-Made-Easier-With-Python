from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import click
import smtplib
import pymysql as db

def for_head(lists,table_desc):
    msg = "<html>" \
          "<head><title>Data</title></head>" \
          "<body>" \
          "<b>%s<b>"%(table_desc)
    msg+="<table border='1' cellpadding='5'>"
    msg += "<tr>"
    for i in lists:
        msg += "<th>%s</th>" % (i.lower().capitalize())
    msg += "</tr>"
    return msg

def for_data(msg,lists):
    for i in lists:
        msg += "<tr>"
        for j in i:
            msg += "<td>%s</td>" % (str(j).lower().capitalize())
        msg += "</tr>"
    return msg


def for_append(msg):
    return msg+"</table></body><br/><br/></html>"

def data_import(conn,college):
    cur1 = conn.cursor()
    q1 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'marks' ORDER BY ORDINAL_POSITION"
    q2 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'student' ORDER BY ORDINAL_POSITION"
    list1 = []
    cur1.execute(q2)
    for i in cur1.fetchall():
        for j in i:
            list1.append(j)
    cur1.execute(q1)
    for i in cur1.fetchall():
        for j in i:
            list1.append(j)
    list1.remove('NAME2')
    msg = for_head(list1, "College Data")
    query = "select name1,college,email,db_name,transform,from_custom_base26,get_pig_latin,top_chars,total from student,marks where student.db_name=marks.name2 and college='%s'" % (
        college)
    cur1.execute(query)
    html1 = for_append(for_data(msg, cur1.fetchall()))
    list2 = ['college', 'count', 'min', 'avg', 'max']
    msg = for_head(list2, 'College Overview')
    query = "select college,count(*),min(total),avg(total),max(total) from student,marks where student.db_name=marks.name2 and college='%s'" % (
        college)
    cur1.execute(query)
    html2 = for_append(for_data(msg, cur1.fetchall()))
    cur2=conn.cursor()
    msg = for_head(list2[1:], "Global Data")
    query = "select count(*),min(total),avg(total),max(total) from student,marks where student.db_name=marks.name2"
    cur2.execute(query)
    msg = for_data(msg, cur2.fetchall())
    html3 = for_append(msg)
    return html1,html2,html3

@click.command("generate")
@click.option("--sendto",default="mynewmailthis@gmail.com",help="can specify the email to whom the report is to be sent")
@click.argument("college",nargs=1)
def generate(college,sendto):
    conn = db.connect(host="localhost", user="root", passwd="Ashok.123")
    conn.select_db('summerdata')
    html1,html2,html3=data_import(conn,college)
    fromaddr = 'mynewmailthis@gmail.com'
    toaddr=sendto
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Students Performance of %s"%(college)

    msg.attach(MIMEText(html1, 'html'))
    msg.attach(MIMEText(html2, 'html'))
    msg.attach(MIMEText(html3, 'html'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, 'newmailcreated')
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        click.echo("Sent Successfully")
    except Exception as e:
        click.echo(e)

generate()