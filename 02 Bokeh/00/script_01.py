from bokeh.io import output_file  # type: ignore[import-not-found]
from bokeh.plotting import figure, show  # type: ignore[import-not-found]

# Sample data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# Output to HTML file
output_file("script_01.html", title="Simple Bokeh Scatter Plot")

# Create figure
p = figure(
    title="Scatter Plot Example",
    x_axis_label="X Values",
    y_axis_label="Y Values",
    height=400,
    width=500,
)

# Add scatter glyphs
p.circle(x, y, size=10, color="blue", alpha=0.7)

show(p)
