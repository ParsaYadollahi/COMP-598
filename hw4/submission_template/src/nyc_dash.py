import pandas as pd

from bokeh.layouts import column
from bokeh.models import Button
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from bokeh.models import Select, ColumnDataSource, Dropdown, DatetimeTickFormatter



# create a plot and style its properties
response_times_overall = pd.read_pickle(f'data/response_times_overall.pkl')
response_times_by_zip = pd.read_pickle(f'data/response_times_by_zip.pkl')
response_times_by_zip['closed month'] = pd.to_datetime(response_times_by_zip['closed month'])
response_times_overall['closed month'] = pd.to_datetime(response_times_overall['closed month'])
zip_codes = sorted(response_times_by_zip['incident zip'].unique())

# Define menus
dropdown1 = Dropdown(label='Incident zip 1', menu=zip_codes)
dropdown2 = Dropdown(label='Incident zip 2', menu=zip_codes)

# Initial plot
zip_code_1 = response_times_by_zip[response_times_by_zip['incident zip'] == zip_codes[0]]
zip_code_2 = response_times_by_zip[response_times_by_zip['incident zip'] == zip_codes[1]]
source_1 = ColumnDataSource(zip_code_1)
source_2 = ColumnDataSource(zip_code_2)
source_overall = ColumnDataSource(response_times_overall)

# Define plot
graph = figure(plot_width=1600, plot_height=700, x_axis_type='datetime')
graph.xaxis[0].ticker.desired_num_ticks = 12
graph.xaxis.formatter=DatetimeTickFormatter(
  hours=["%B"],
  days=["%B"],
  months=["%B"],
  years=["%B"]
)

graph.line(x='closed month', y='response time', source=source_1, color="red", legend_label='Incident zip 1')
graph.line(x='closed month', y='response time', source=source_2, color="blue", legend_label='Incident zip 2')
graph.line(x='closed month', y='response time', source=source_overall, color="green", legend_label='Incident overall')

# Define callbacks when menus are clicked
def incident_zip_callback_1(event):
  source_1.data = response_times_by_zip[response_times_by_zip['incident zip'] == event.item]

def incident_zip_callback_2(event):
  source_2.data = response_times_by_zip[response_times_by_zip['incident zip'] == event.item]

dropdown1.on_click(incident_zip_callback_1)
dropdown2.on_click(incident_zip_callback_2)

graph.xaxis.axis_label = 'Close Month'
graph.yaxis.axis_label = 'Response time (h)'

# Arrange plots and widgets in layouts
layout = column(dropdown1, dropdown2, graph)
curdoc().add_root(layout)
