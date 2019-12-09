# -*- coding: utf-8 -*-
import pymysql,sys,pymysql.cursors,datetime,time

class DBHelper:
    def __init__(self, ip='127.0.0.1', port=3306, db_name='dbname', user='root', password='root',return_dic=False):
        try:
            if return_dic:
                self.conn = pymysql.connect(ip, port=port, user=user, passwd=password, db=db_name, charset='utf8',cursorclass=pymysql.cursors.DictCursor)
            else:
                self.conn = pymysql.connect(ip, port=port, user=user, passwd=password, db=db_name, charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
            print("connect database failed")
            sys.exit(-1)

    def get_table_info(self, command):
        try:
            effect_row = self.cursor.execute(command)
            table_info = self.cursor.fetchall()
        except Exception as e:
            print(command)
            print(e)
            print(u"read table failed")
            return None
        return table_info

    def get_table_info_many(self, command):
        list_one = []
        try:
            effect_row = self.cursor.execute(command)
            while True:
                row = self.cursor.fetchone()
                if not row:
                    break
                list_one.append(row)
        except Exception as e:
            print(e)
            print(u"read table failed")
            return None
        # print(u"there total %s rows data。" % effect_row)
        return list_one

    def update_table(self,command):
        try:
            self.cursor.execute(command)
            self.conn.commit()
        except:
            self.conn.rollback()


if __name__=='__main__':
    db=DBHelper(ip='localhost', port=3306, db_name='baidupan', user='root', password='root')
    data=db.get_table_info_many("SELECT * FROM `pan` WHERE context LIKE '%韩漫%'")
    print(len(data))
    print(data)