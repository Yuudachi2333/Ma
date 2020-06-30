import pymysql

class Use_msyql:
    def __init__(self,user="root",password="",port=3306,host="127.0.0.1",db='company'):
        self.user = user
        self.password = password
        self.prot = port
        self.host = host
        self.db = db
        self.connect = pymysql.connect(user = self.user,password=self.password,port=self.prot,
                                       host=self.host,db=self.db)
        self.cur = self.connect.cursor()







    def mysql_select(self,sql):
        self.cur.execute(sql)


    def custom_select(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()


    def getone(self,table):
        '''
        查询数据表第一行数据
        :param table:
        :return:
        '''
        sql = "select * from {}".format(table)
        self.mysql_select(sql)
        data = self.cur.fetchone()
        return data

    def getmany(self,row,table):
        '''
        查询数据表指定行数数据
        :param row:
        :param table:
        :return:
        '''
        sql = "select * from {}".format(table)
        self.mysql_select(sql)
        data = self.cur.fetchmany(row)
        return data

    def getall(self,table):
        '''
        查询数据表所以数据
        :param table:
        :return:
        '''
        try:
            sql = "select * from {}".format(table)
            self.mysql_select(sql)
            data = self.cur.fetchall()
            return data
        except :
            return "获取所以数据出错"

    def mysql_delete(self,opinion,table,sid,num):
        '''
         删除数据表数据
        :param opinion:  条件大于，等于
        :param table: 要删除的数据表
        :param sid: 删除的数据表主键id
        :param num: 删除的数据表主键对应的值
        :return:
        '''

        if opinion == "等于":
            sql = "delete from {} where {}={}".format(table,sid,num)
            self.cur.execute(sql)
        elif opinion == "大于" :
            sql = "delete from {} where {}>{}".format(table, sid, num)
            self.cur.execute(sql)
        self.connect.commit()

    def mysql_insert(self,table,sql= None,data=None):
        '''
        插入数据
        :param table: 表的名称
        :param sql:  执行的sq语句
        :param data: 插入的数据
        :return:
        '''
        if sql is None and data is None:
            sql= "insert into {} values (%s,%s,%s)".format(table)
            insert_data = ("17","name","locate")
            self.cur.execute(sql,insert_data)
            self.connect.commit()
        else:
            self.cur.execute(sql,data)
            self.connect.commit()



if __name__ == '__main__':
    mysql = Use_msyql(db="company2")
    sql = "select * from dept"
    print(mysql.getone(sql))
    print(mysql.getmany(sql,3))
    print(mysql.getall("job"))
    mysql.mysql_delete(opinion ="大于",table="dept",sid="deptno",num=12)
    sql = 'insert into dept values (%s,%s,%s)'
    data = (19,"name1","locate1")
    mysql.mysql_insert("dept",sql,data)
    sql = 'SELECT * from emp,dept where emp.deptno=dept.deptno'
    data = mysql.custom_select(sql)
    for i in data:
        print(i)
