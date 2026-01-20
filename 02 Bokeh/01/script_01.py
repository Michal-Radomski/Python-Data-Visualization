from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# prepare the output
output_file("script_01.html")

# create the figure
f = figure(
    x_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
    y_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
)

# create glyphs
f.circle(x=["A", "B"], y=["C", "D"], size=8)

show(f)
