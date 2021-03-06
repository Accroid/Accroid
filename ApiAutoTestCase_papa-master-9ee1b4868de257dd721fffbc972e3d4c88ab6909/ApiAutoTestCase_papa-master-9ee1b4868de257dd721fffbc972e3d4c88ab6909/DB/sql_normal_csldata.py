# _*_ coding:utf-8 _*_
import pymysql,re
# Python操作mysql数据库：pymysql模块
# http://blog.sina.com.cn/s/blog_45ac0d0a010180aw.html
db_info = {'user': 'csldata',
            'pwd': 'csldata@2017',
            'host': '192.168.0.52',
            'db': 'csldata',
            'port': 3306,
            'charset':'utf8'}

class mysql_connect:
    def __init__(self, db_info):
        self.db_user = db_info['user']
        self.db_pw = db_info['pwd']
        self.db_host = db_info['host']
        self.db = db_info['db']
        self.port = db_info['port']
        self.charset = db_info['charset']
        self.conn = pymysql.connect(host=self.db_host,user=self.db_user, passwd=self.db_pw,  db=self.db,port=self.port,charset=self.charset)
        self.cursor = self.conn.cursor()

    def fetchone(self):
        return self.cursor.fetchall()[0]

    def sql_exec(self, sql_com, need_return=0):
        if need_return == 1:
            try:
                self.cursor.execute(sql_com)
                return self.cursor
                # return result
            except pymysql.Error as err:
                pass
                # print ("Error: {}".format(err.message))
                # sys.exit()
            finally:
                self.conn.commit()
        elif need_return == 0:
            try:
                self.cursor.execute(sql_com)
            except pymysql.Error as err:
                pass
            finally:
                self.conn.commit()

    def sql_assign_exec(self, sql_com):
        value = 'not find'
        for i in self.sql_exec(sql_com,1):
            value=i[0]
        return value

    # 一般的sql语句处理
    def sql_exec_normal(self, sql_com):
        self.cursor.execute(sql_com)
        return self.cursor.fetchone()[0]
#获取单条sql的全部结果
    def sql_exec_normal_all(self, sql_com):
        self.cursor.execute(sql_com)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
