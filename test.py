import pymysql
 
con = pymysql.connect(host="db1", user="root", password="example",
                       db='employees', charset='utf8')
 
 
cur = con.cursor()
 
sql="select count(*) from employees"
num = cur.execute(sql)
print(num)
 
for i in cur:
    print(i)
