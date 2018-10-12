# -*- coding: utf-8 -*-

from impala.dbapi import connect
from plotly.graph_objs import  *
import plotly as py

# 连接数据源
conn = connect(host='impala服务ip',database='my_ums')
cursor = conn.cursor()
# 查询每日总量
cursor.execute("SELECT `date`, count(1) FROM my_ums_snapshot.t_my_info GROUP BY `date` ORDER BY `date`")
results = cursor.fetchall()

# 用户总量集合
user_count = []
# 日期集合
day = []

for result in results:
    day.append(result[0])
    user_count.append(result[1])

# 配置散点数据
user_count_data = Scatter(x=day,
                 y=user_count,
                 name="用户趋势图")

# 配置要绘制的数据集
data = [user_count_data]

# 配置图层
layout = Layout(title="用户趋势图",
                xaxis=dict(title="日期"),
                yaxis=dict(title="用户数量"))

fig = Figure(data=data, layout=layout)

# 生成离线文件，且不自动打开
py.offline.plot(figure_or_data=fig, filename="D://py/counter1.html", auto_open=False)

