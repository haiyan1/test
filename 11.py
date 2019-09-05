
#！usr/bin/python
#-*-coding:UTF-8-*-
import pymysql.cursors
import redis

# 连接数据库
connect = pymysql.Connect(
    host='10.8.40.234',
    port=3306,
    user='dguard',
    passwd='ggty2016wh',
    db='dguard',
    charset='utf8'
)

pool = redis.ConnectionPool(host='10.8.40.186',port='6379')   #实现一个连接池
r = redis.Redis(connection_pool=pool)
# 获取游标
cursor = connect.cursor()

sql="select service_tag from t_ca_service  where UI_TYPE_BUSINESS_TYPE='2'"
cursor.execute(sql)
results=cursor.fetchall()
for row in results:
    fsn=row[0]
    print (fsn,'',end='')
    r.lpush('SERVICETAGS', fsn)
print('')
print ('共查询出',cursor.rowcount,'行数据')
connect.close()



