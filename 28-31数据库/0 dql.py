import pymysql
import datetime
db = None
cursor = None
try:
    # 打开数据库连接 ，connection 自动加入事务处理，开始begin
    db = pymysql.connect("localhost", "root", "cwqcs007", "db_test")

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT * from emp")

        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchone()

        print(type(data))
        print(data)
        print(datetime.datetime.strftime(data[4], '%Y/%m/%d'))
    except Exception as ex:
        print(ex)
except Exception as ex:
    print(ex)
finally:
    # 关闭游标和数据库连接
    if cursor:
        cursor.close()
    if db:
        db.close()