import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
data=pandas.read_csv("reviews.csv",parse_dates=['Timestamp'])
data['Week']= data['Timestamp'].dt.strftime('%Y-%U')
data_weekavg=data.groupby(['Week']).mean()

chart_def= """
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: ''
  },
  subtitle: {
    text: ''
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Date'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: 0 to 80 km.'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average-Rating'
    },
    labels: {
      format: '{value}'
    },
    accessibility: {
      rangeDescription: 'Range: -90°C to 20°C.'
    },
    lineWidth: 2
  },
  legend: {
    enabled: false
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x}: {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'Average-Rating',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}"""
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analyis of Course reviews",classes="text-h3 text-center")
    p1 = jp.QDiv(a=wp , text="The graphs represents course review analysis",classes= "text-h6 text-center")

    hc = jp.HighCharts(a=wp , options=chart_def)
    hc.options.xAxis.categories = list(data_weekavg.index)
    hc.options.series[0].data = list(data_weekavg['Rating'])
    return wp
jp.justpy(app)