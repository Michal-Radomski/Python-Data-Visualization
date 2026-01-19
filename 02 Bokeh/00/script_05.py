# Making a basic Bokeh line graph

# importing bokeh and pandas
import pandas  # type: ignore[import-not-found]
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# prepare some data
df = pandas.read_csv("data.csv")
# print(df)
x = df["x"]
y = df["y"]

# prepare the output file
output_file("script_05.html")

# create a figure object
f = figure()

# create line plot
f.line(x, y)

# write the plot in the figure object
show(f)
