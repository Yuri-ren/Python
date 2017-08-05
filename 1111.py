#coding: utf-8

from echarts import Echart,Legend,Bar,Axis
import datetime

start_day=datetime.date.today()-datetime.timedelta(days=1)
end_day=datetime.date.today()-datetime.timedelta(days=7)

day=str(end_day)+"到"+str(start_day)

date_list=['2017-07-29', '2017-07-30', '2017-07-31', '2017-08-01', '2017-08-02', '2017-08-03', '2017-08-04']
domain_list=['pl8.live.panda.tv', 'pl7.live.panda.tv']
band_list1=[22296.378565813324, 22798.786958239965, 18836.00344704, 20950.709171999984, 22132.00082202666, 26718.32377615999, 26766.375197813308]
band_list2=[3023.488939999995, 1852.0315420533348, 1597.4116898133348, 1737.9599384799994, 1549.2366309600034, 2268.1028273066668, 2449.951201013336]

# chart = Echart('大客户海外带宽趋势', day)
# chart.use(Bar('China', band_list1))
# chart.use(Legend(['GDP']))
# chart.use(Axis('category', 'bottom', data=date_list))

# chart.plot()

###封装成一个函数 生成echarts出来
def GetEcharts():
	option = {
	    'title': {
	        'text': '大客户海外带宽趋势'
	    },
	    'tooltip' : {
	        'trigger': 'axis',
	        'axisPointer': {
	            'type': 'cross',
	            'label': {
	                'backgroundColor': '#6a7985'
	            }
	        }
	    },
	    'legend': {
	        'data':['邮件营销','联盟广告','视频广告','直接访问','搜索引擎']
	    },
	    'grid': {
	        'left': '3%',
	        'right': '4%',
	        'bottom': '3%',
	        'containLabel': 'true'
	    },
	    'xAxis' : [
	        {
	            'type' : 'category',
	            'boundaryGap' : 'false',
	            'data' : ['周一','周二','周三','周四','周五','周六','周日']
	        }
	    ],
	    'yAxis' : [
	        {
	            'type' : 'value'
	        }
	    ],
	    'series' : [
	        {
	            'name':'邮件营销',
	            'type':'line',
	            'stack': '总量',
	            'areaStyle': {'normal': {}},
	            'data':[120, 132, 101, 134, 90, 230, 210]
	        },
	        {
	            'name':'联盟广告',
	            'type':'line',
	            'stack': '总量',
	            'areaStyle': {'normal': {}},
	            'data':[220, 182, 191, 234, 290, 330, 310]
	        },
	        {
	            'name':'视频广告',
	            'type':'line',
	            'stack': '总量',
	            'areaStyle': {'normal': {}},
	            'data':[150, 232, 201, 154, 190, 330, 410]
	        },
	        {
	            'name':'直接访问',
	            'type':'line',
	            'stack': '总量',
	            'areaStyle': {'normal': {}},
	            'data':[320, 332, 301, 334, 390, 330, 320]
	        },
	        {
	            'name':'搜索引擎',
	            'type':'line',
	            'stack': '总量',
	            'label': {
	                'normal': {
	                    'show': 'true',
	                    'position': 'top'
	                }
	            },
	            'areaStyle': {'normal': {}},
	            'data':[820, 932, 901, 934, 1290, 1330, 1320]
	        }
	    ]
	}
	return option

print GetEcharts()
