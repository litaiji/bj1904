"""
db.field('sname,ssex,sclass).where(ssex='男').orderby('sname desc).select()
db.where(ssex='男').orderby('sname desc).field('sname,ssex,sclass).select()

"""
class Dbhelper:
    def __init__(self):
        self.params = {
            'fields':'*',
            'table':'user',
            'limit':'',
            'where':'',
            'groupby':'',
            'having':'',
            'orderby':''
        }
    def where(self,*args):
        print('where')
        self.params['where'] = 'Where ssex="男"'
        return self
    def orderby(self,*args):
        self.params['orderby'] = " order by ssex"
        print('orderby')
        return self
    def select(self):
        sql = "SELECT {fields} FROM {table} {where}  {groupby} {having} {orderby} {limit}"

        sql = sql.format(**self.params)
        print(sql)
if __name__ == "__main__":
    db = Dbhelper()
    db.where().orderby().select()