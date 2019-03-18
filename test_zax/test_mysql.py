import pymysql

#连接数据库
db = pymysql.connect("10.72.12.44","root","root","avg_0")
#使用cursor方法获取游标
cursor = db.cursor()
#查询语句
sql = "SELECT * FROM avg_game_topic_comment_0"
try:
    #执行sql语句
    cursor.execute(sql)
    #获取查询记录
    res = cursor.fetchone()
    print(res)

except:
    print("error")
db.close()