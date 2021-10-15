import pandas as pd

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from bokeh.models import Select, ColumnDataSource, Dropdown, DatetimeTickFormatter



# create a plot and style its properties
# response_times_overall = pd.read_csv("./data/response_by_month.csv")
# response_times_by_zip = pd.read_csv("./data/response_by_zip.csv")
response_times_overall = pd.read_pickle(f'data/response_times_overall.pkl')
response_times_by_zip = pd.read_pickle(f'data/response_times_by_zip.pkl')
response_times_by_zip['closed month'] = pd.to_datetime(response_times_by_zip['closed month'])
response_times_overall['closed month'] = pd.to_datetime(response_times_overall['closed month'])
zip_codes = sorted(response_times_by_zip['incident zip'].unique())

# Define menus
menu_1 = Dropdown(label='ZIP code 1', menu=zip_codes)
menu_2 = Dropdown(label='ZIP code 2', menu=zip_codes)

# Initial plot
zip_code_1 = response_times_by_zip[response_times_by_zip['incident zip'] == zip_codes[0]]
zip_code_2 = response_times_by_zip[response_times_by_zip['incident zip'] == zip_codes[1]]
source_1 = ColumnDataSource(zip_code_1)
source_2 = ColumnDataSource(zip_code_2)
source_overall = ColumnDataSource(response_times_overall)

# Define plot
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

# Define callbacks when menus are clicked
def callback_1(event):
  source_1.data = response_times_by_zip[response_times_by_zip['incident zip'] == event.item]

def callback_2(event):
  source_2.data = response_times_by_zip[response_times_by_zip['incident zip'] == event.item]

menu_1.on_click(callback_1)
menu_2.on_click(callback_2)

graph.xaxis.axis_label = 'Closed month'
graph.yaxis.axis_label = 'Average response time (hours)'

# Arrange plots and widgets in layouts
layout = column(menu_1, menu_2, graph)
curdoc().add_root(layout)
