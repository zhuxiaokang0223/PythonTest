# -*- coding: utf-8 -*-

# 使用Pyhive连接Hive

from pyhive import hive

conn = hive.connect(host="HiveServer2服务iP", port=10000,database="my_ums")

cursor = conn.cursor()
cursor.execute("SELECT * FROM t_my_group LIMIT 2")
for result in cursor.fetchall():
    print(result)
