import pandas as pd

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from bokeh.models import Select, ColumnDataSource, Dropdown, DatetimeTickFormatter



# create a plot and style its properties
response_time_by_month = pd.read_csv("./data/response_by_month.csv")
response_time_by_zip = pd.read_csv("./data/response_by_zip.csv")
response_time_by_zip['closed month'] = pd.to_datetime(response_time_by_zip['closed month'])
response_time_by_month['closed month'] = pd.to_datetime(response_time_by_month['closed month'])

zip_codes = sorted(response_time_by_zip['incident zip'].unique())

zip_codes = ["%.1f" % x for x in zip_codes]

menu_1 = Dropdown(label='ZIP 1', menu=zip_codes)
menu_2 = Dropdown(label='ZIP 2', menu=zip_codes)

# print(response_time_by_zip[response_time_by_zip['incident zip'].astype(str).str.contains(zip_codes[0], na = False)])
zip_code_1 = response_time_by_zip[response_time_by_zip['incident zip'].astype(str).str.contains(zip_codes[0], na = False)]
zip_code_2 = response_time_by_zip[response_time_by_zip['incident zip'] == zip_codes[1]]
source_1 = ColumnDataSource(zip_code_1)
source_2 = ColumnDataSource(zip_code_2)
source_overall = ColumnDataSource(response_time_by_month)
print(source_overall)


graph = figure(plot_width=1200, plot_height=500, x_axis_type='datetime')
graph.xaxis[0].ticker.desired_num_ticks = 9
graph.xaxis.formatter=DatetimeTickFormatter(
  hours=["%B"],
  days=["%B"],
  months=["%B"],
  years=["%B"]
)

graph.line(x='closed month', y='response time', source=source_1, color="red", legend_label='ZIP code 1')
graph.line(x='closed month', y='response time', source=source_2, color="blue", legend_label='ZIP code 2')
graph.line(x='closed month', y='response time', source=source_overall, color="green", legend_label='Overall')


def zip1_callback(event):
  source_1.data = response_time_by_zip[response_time_by_zip['incident zip'].astype(str).str.contains(event.item, na = False)]
  print(source_1.data)
  # source_1.data = response_time_by_zip[response_time_by_zip['incident zip'] == event.item]

def zip2_callback(event):
  source_2.data = response_time_by_zip[response_time_by_zip['incident zip'] == event.item]


menu_1.on_click(zip1_callback)
menu_2.on_click(zip2_callback)

graph.xaxis.axis_label = 'Closed month'
graph.yaxis.axis_label = 'Average response time (hours)'

layout = column(menu_1, menu_2, graph)
curdoc().add_root(layout)
