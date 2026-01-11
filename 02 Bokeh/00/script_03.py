# Making a basic Bokeh line graph

# importing Bokeh
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

# prepare the output file
output_file("script_03.html")

# create a figure object
f = figure()

# create line plot
f.line(x, y)

# write the plot in the figure object
show(f)
