import numpy as np
from bokeh.layouts import column  # type: ignore[import-not-found]
from bokeh.models import Slider  # type: ignore[import-not-found]
from bokeh.plotting import curdoc, figure  # type: ignore[import-not-found]

# Sample data
x = np.linspace(0, 10, 500)
y = np.sin(x)

# Plot
p = figure(height=400, width=600, title="Interactive Sine Wave")
r = p.line(x, y, line_width=2, line_color="navy")

# Slider
slider = Slider(start=0.1, end=10, value=1, step=0.1, title="Frequency")


# Callback
def update(attr, old, new):
    y_new = np.sin(slider.value * x)
    r.data_source.data["y"] = y_new


slider.on_change("value", update)

# Layout
layout = column(slider, p)
curdoc().add_root(layout)
