# -*- coding: utf-8 -*-

# 连接impala示例

from impala.dbapi import connect
conn = connect(host='impala服务ip',database='my_ums')
cursor = conn.cursor()
cursor.execute("SELECT * FROM t_my_group LIMIT 2")
results = cursor.fetchall()
for result in results:
    print(result)
