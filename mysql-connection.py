import pymysql.cursors
conn = pymysql.connect(host='127.0.0.1', port=3307, user='user', password='password', database='db')
sql = 'show tables'
cursor = conn.cursor()
cursor.execute(sql)
res = cursor.fetchall()

print(res)
conn.close()