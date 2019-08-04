import pymysql
import datetime
connection = None
cursor = None
try:
    # 打开数据库连接 ，connection 自动加入事务处理，开始begin
    connection = pymysql.connect("localhost", "root", "cwqcs007", "db_test")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = connection.cursor()
    sql = 'insert into dept values(%s,%s,%s)'
    try:
        # 使用 execute()  方法执行 SQL 查询
        # cursor.execute("insert into dept values(60,'大头','shandong')")
        # cursor.execute("insert into dept values(%s,'%s','%s')" % (70,'小头','dongbei'))
        cursor.execute(sql,(80,'name1','beijing'))
        connection.commit()

    except Exception as ex:
        connection.rollback()
        print(ex)
except Exception as ex:
    print(ex)
finally:
    # 关闭游标和数据库连接
    if cursor:
        cursor.close()
    if connection:
        connection.close()