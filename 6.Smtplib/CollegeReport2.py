import pymysql as db
import warnings
import click
from openpyxl import *
warnings.filterwarnings("ignore")

conn = db.connect(host="localhost", user="root", passwd="Ashok.123")
conn.select_db('summerdata')
cur1 = conn.cursor()
college='gvp'
j=0
msg="<html>" \
    "<head><title>Excel</title></head>" \
    "<body>"\
    "<b>College Data<b>"\
    "<table>"
# query="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'student' ORDER BY ORDINAL_POSITION"
# cur1.execute(query)
# msg+="<tr>"
# for i in cur1.fetchall():
#     for j in i:
#         msg+="<th>%s</th>"%(j)
#
# query="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'marks' ORDER BY ORDINAL_POSITION"
# cur1.execute(query)
# l=[]
# for i in cur1.fetchall():
#     for j in i:
#         if j not in l:
#             l.append(j)
#             msg+="<th>%s</th>"%(j)
# msg+="</tr>"
#
# query="select * from student,marks where student.db_name=marks.name2 and college='%s'"%(college)
# cur1.execute(query)
# for i in cur1.fetchall():
#     msg+="<tr>"
#     for j in i:
#         msg+="<td>%s</td>"%(j)
#     msg+="</tr>"
# msg+="</table></body></html>"
# print(msg)
# query="select college,count(*),min(total),avg(total),max(total) from student,marks where student.db_name=marks.name2 and college='%s'"%(college)
# cur1.execute(query)
# print(cur1.fetchone())
# query="select college from student group by college"
# cur1.execute(query)
# colleges=[]
# for i in cur1.fetchall():
#     if i !="None":
#         colleges.append(i)
# cur2=conn.cursor()
# msg="<html>" \
#     "<head><title>Excel</title></head>" \
#     "<body>"\
#     "<b>Global Data<b>"\
#     "<table><tr><th>college</th><th>count</th><th>min_total</th><th>avg_total</th><th>max_total</th></tr>"
# for i in colleges:
#     query = "select college,count(*),min(total),avg(total),max(total) from student,marks where student.db_name=marks.name2 and college='%s' and college <>'None'" % (i)
#     cur2.execute(query)
#     # for j in cur2.fetchall():
#     #     print(j)
#     for j in cur2.fetchall():
#         msg+="<tr>"
#         for k in j:
#             msg+="<td>%s</td>"%(k)
#         msg+="</tr>"
# print(msg)
# list1=['name1','college','email','db_name','transform','from_custom_base26','get_pig_latin','top_chars','total',college]
# query = "select %s,%s,%s,%s,%s,%s,%s,%s,%s from student,marks where student.db_name=marks.name2 and college='%s'" % (str(i) for i in list1)
# cur1.execute(query)
# for i in cur1.fetchall():
#     print(i)
q1="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'marks' ORDER BY ORDINAL_POSITION"
q2="SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'student' ORDER BY ORDINAL_POSITION"
list1=[]
cur1.execute(q2)
for i in cur1.fetchall():
    for j in i:
        list1.append(j)
cur1.execute(q1)
for i in cur1.fetchall():
    for j in i:
        list1.append(j)

list1.remove('NAME2')
print(list1)