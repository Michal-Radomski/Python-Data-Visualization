# Import libraries
from random import randrange

from bokeh.io import curdoc  # type: ignore[import-not-found]
from bokeh.models import ColumnDataSource  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# Create figure
f = figure(x_range=(0, 11), y_range=(0, 11))

# Create columndatasource
source = ColumnDataSource(data=dict(x=[], y=[]))

# Create glyphs
f.circle(x="x", y="y", size=8, fill_color="olive", line_color="yellow", source=source)
f.line(x="x", y="y", color="red", source=source)


# Create periodic function
def update():
    new_data = dict(x=[randrange(1, 10)], y=[randrange(1, 10)])
    source.stream(new_data, rollover=15)
    print(source.data)


# Add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update, 1000)
