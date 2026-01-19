from bokeh.io import output_file  # type: ignore[import-not-found]
from bokeh.plotting import figure, show  # type: ignore[import-not-found]

p = figure(width=500, height=400, title="Circle and Triangle")
p.circle(x=[1, 2, 3], y=[1, 3, 2], size=20, color="blue", legend_label="Circle")
p.triangle(
    x=[1.5, 2.5, 3.5], y=[2, 1.5, 2.5], size=25, color="red", legend_label="Triangle"
)

# prepare the output file
output_file("script_04.html")

show(p)
