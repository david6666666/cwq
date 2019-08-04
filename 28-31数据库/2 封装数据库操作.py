import pymysql
import datetime

class MysqlHelper(object):
    config={
        'host':'localhost',
        'user':'root',
        'password':'cwqcs007',
        'db':'db_test'
    }
    def __init__(self):
        self.connection = None
        self.cursor = None

    #该函数用来从数据库表中查询一行数据
    def getOne(self,sql,*args):
        try:
            self.connection = pymysql.connect(**MysqlHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql,args)
            return self.cursor.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()

    #该函数用来从数据库表中查询多行数据
    def getList(self,sql,*args):
        try:
            self.connection = pymysql.connect(**MysqlHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql,args)
            return self.cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
    #对数据库进行增删改
    def excuteDML(self,sql,*args):
        try:
            self.connection = pymysql.connect(**MysqlHelper.config)
            self.cursor = self.connection.cursor()
            num = self.cursor.execute(sql,args) #sql语句执行之后影响的函数
            self.connection.commit()
            return num
        except Exception as ex:
            self.connection.rollback()
            print(ex)
        finally:
            self.close()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

if __name__ == '__main__':
    helper = MysqlHelper()
    print(helper.excuteDML('delete from dept where deptno=%s',80))




