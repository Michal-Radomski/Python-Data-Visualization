# Plotting percentage of women who received an engineering degree over years

# importing bokeh and pandas
import pandas  # type: ignore[import-not-found]
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# prepare some data
# df = pandas.read_csv("https://pythonizing.github.io/data/bachelors.csv")
df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

# prepare the output file
output_file("script_06.html")

# create a figure object
f = figure()

# create line plot
f.line(x, y)

# write the plot in the figure object
show(f)
