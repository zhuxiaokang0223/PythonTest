# 在线绘制
'''
import plotly.plotly as py
from plotly.graph_objs import *

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.plot(data, filename = 'basic-line')

'''

# 离线绘制
'''
import plotly as py
from plotly.graph_objs import *

py.offline.plot({
    "data": [Scatter(x=[2015, 2016, 2017, 2018], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world"),
})
'''

import plotly as py
from plotly.graph_objs import *

user_count = Scatter(x=[2015, 2016, 2017, 2018],
                 y=[4, 3, 2, 1],
                 name="用户趋势图")

data = [user_count]

layout = Layout(title="用户趋势图",
                xaxis=dict(title="日期"),
                yaxis=dict(title="用户数量"))

fig = Figure(data=data, layout=layout)

py.offline.plot(figure_or_data=fig)

