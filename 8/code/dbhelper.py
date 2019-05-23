"""
db.field('sname,ssex,sclass).where(ssex='男').orderby('sname desc).select()
db.where(ssex='男').orderby('sname desc).field('sname,ssex,sclass).select()

"""
import pymysql
import settings
class Dbhelper:
    def __init__(self,table):
        self.table = table  # 表名
        self.conn = pymysql.Connect(**settings.parameters) #连接数据库
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)  #游标
        self.params = self.__init_param()   #初始化字典参数
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def __init_param(self):
         return  {
                'fields': '*',
                'table': self.table,
                'limit': '',
                'where': '',
                'groupby': '',
                'having': '',
                'orderby': ''
            }
    # 条件之间是逻辑与的关系
    def where(self,**kwargs):
        """
        where:" where uid=1"
        :param args: {'uid':2,username:'tom',password:'dddddd}
                     {'uid__nin':2}  uid  gt  2
        :return:
        """
        if len(kwargs) <= 0:
            return self
        self.__add_quote(kwargs)
        ops = {  #运算符对照表
            'gt':'>',
            'ge':'>=',
            'lt':'<',
            'le':'<=',
            'ne':'!=',
            'in':'in',
            'nin':'not in'

        }
        # print(kwargs)
        for key in kwargs:
            keys = key.split('__')
            if len(keys)>1: #运算符不是等号
                op = keys[1]  #运算符
                if self.params['where']:
                    self.params['where'] += " and " + keys[0] + ops[op] + kwargs[key]
                else:
                    self.params['where'] = " where " + keys[0] + ops[op] + kwargs[key]
            else:
                if self.params['where']:
                    self.params['where'] += " and " + keys[0] + '=' + kwargs[key]
                else:
                    self.params['where'] = " where " + keys[0] + '=' + kwargs[key]


        # if self.params['where']:  # where有值
        #     self.params['where'] += " and " + " and ".join([key +"="+ value for key,value in kwargs.items()])
        # else:  # where没有值
        #     self.params['where'] = " where " +" and ".join([key +"="+ value for key,value in kwargs.items()])
        print(self.params)
        return self
    def __add_quote(self,data):
        """

        :param data: 参数字典
        :return:
        """
        for key in data:
            if isinstance(data[key],str): # 是字符串两边添加单引号
                data[key] = "'" + pymysql.escape_string(data[key]) + "'"
            else: # 不是字符串，转换为字符串
                data[key] = str(data[key])
        return self
    # 条件之间是逻辑或的关系
    def whereor(self,*args):
        print('where')
        self.params['where'] = 'Where ssex="男"'
        return self
    def orderby(self,*args):
        if len(args) <=0:
            return self
        self.params['orderby'] = ' order by ' + ','.join(args)
        return self
    def limit(self,*args):
        if len(args)<=0:
            return self
        my_args = [ str(value) for value in args]
        self.params['limit'] = " limit " + ','.join(my_args)
        return  self
    def groupby(self,*args):
        if len(args) <=0:
            return self
        self.params['groupby'] = " group by " +",".join(args)
        return self
    def having(self,**kwargs):
        if len(kwargs) <= 0:
            return self
        self.__add_quote(kwargs)
        # print(kwargs)
        if self.params['having']:  # having有值
            self.params['having'] += " and " + " and ".join([key +"="+ value for key,value in kwargs.items()])
        else:  # where没有值
            self.params['having'] = " having " +" and ".join([key +"="+ value for key,value in kwargs.items()])
        # print(self.params)
        return self
    def  fields(self,value):
        """

        :param value: 形如：'sid,name,sex'
        :return:
        """
        value = value.strip()
        if not value:
            return self
        self.params['fields'] = str(value)
        return self
    def insert(self,data):
        """

        :param data: {'name':'tom','sex':'男'}
        :return:
        """
        pass
        sql = "INSERT INTO {table} ({fields}) VALUES({values})"

    def select(self):
        sql = "SELECT {fields} FROM {table} {where}  {groupby} {having} {orderby} {limit}"
        sql = sql.format(**self.params)
        print(sql)
        return self.query(sql)
    def query(self,sql):
        self.params = self.__init_param() # 参数字典初始化
        try:
            res = self.cursor.execute(sql)
            if res > 0:
                return  self.cursor.fetchall()
            else:
                return None
        except Exception as e:
            print(e)
            return None
        return None
if __name__ == "__main__":
    db = Dbhelper('student')
    # print(db.select())
    # db.where(username='tom',password='123').where(uid=2)
    # db.orderby('username asc','uid desc').select()
    # db.limit(5)
    # data = db.limit(0,1).select()
    # db.limit('2')
    # data = db.fields('sex ,count(*) ').groupby('sex').select()
    # print(data)
    data = db.where(sid__ne=2).orderby('sid desc').select()  #{'sid__ne':2}
    print(data)