#调用模块
import MySQLdb
#连接数据库
conn=MySQLdb.connect(host="localhost",user="root",passwd="root",db="python",charset='utf8')
#生成模块
cur=conn.cursor()
#执行添加
#cur.execute("INSERT INTO Users(Username,pwd)VALUES('张明','123')")
#执行查询
cur.execute("SELECT * FROM Users")
rows=cur.fetchall() 
#print rows
for row in rows:
	print row