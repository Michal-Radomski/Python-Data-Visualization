from bokeh.layouts import gridplot  # type: ignore[import-not-found]
from bokeh.models.annotations import (  # type: ignore[import-not-found]
    BoxAnnotation,
    Span,
)
from bokeh.plotting import figure, output_file, show  # type: ignore[import-not-found]

# Prepare the output file
output_file("script_02.html")

x1, y1 = list(range(0, 10)), list(range(10, 20))
x2, y2 = list(range(20, 30)), list(range(30, 40))
x3, y3 = list(range(40, 50)), list(range(50, 60))

# Create a new plot
f1 = figure(width=250, height=250, title="Circles")
f1.circle(x1, y1, size=10, color="navy", alpha=0.5)

# Create another one
f2 = figure(width=250, height=250, title="Triangles")
f2.triangle(x2, y2, size=10, color="firebrick", alpha=0.5)

# Create and another
f3 = figure(width=250, height=250, title="Squares")
f3.square(x3, y3, size=10, color="olive", alpha=0.5)

# Create a span annotation
span_4 = Span(location=4, dimension="height", line_color="green", line_width=2)
f1.add_layout(span_4)

# Create a box annotation
box_2_6 = BoxAnnotation(left=2, right=6, fill_color="firebrick", fill_alpha=0.3)
f1.add_layout(box_2_6)

# Put all the plots in a grid layout
f = gridplot([[f1, f2], [None, f3]])

# Show the results
show(f)
