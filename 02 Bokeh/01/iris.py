# Plotting flower species

# Importing libraries
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.models import (  # type: ignore[import-not-found]
    HoverTool,
    PanTool,
    Range1d,
    ResetTool,
    Title,
    WheelZoomTool,
)
from bokeh.plotting import figure  # type: ignore[import-not-found]
from bokeh.sampledata.iris import flowers  # type: ignore[import-not-found]

# Define the output file path
output_file("iris.html")

# Create the figure object
f = figure(title="Iris Morphology", width=1200, height=700)

# Style the tools
tools = [PanTool(), ResetTool(), WheelZoomTool()]
f.add_tools()
hover = HoverTool(tooltips=[("Species", "@species"), ("Sepal Width", "@sepal_width")])
f.add_tools(hover)
# f.toolbar_location = "above"
# f.toolbar.logo = None


# Add axis labels
f.xaxis.axis_label = "Petal Length (cm)"
f.yaxis.axis_label = "Petal Width (cm)"
f.background_fill_color = "olive"
f.background_fill_alpha = 0.3

# Color by species
colormap = {"setosa": "red", "versicolor": "green", "virginica": "blue"}
colors = [colormap[species] for species in flowers["species"]]

# Add glyphs with styling
f.circle(
    x=flowers["petal_length"],
    y=flowers["petal_width"],
    color=colors,
    fill_alpha=0.6,
    size=8,
)

# Title
f.title.text = "Iris Morphology"
f.title.text_font_size = "40px"  # Adjust size
f.title.text_color = "navy"  # Change color
f.title.text_font_style = "bold"  # Bold, italic, etc.
f.title.align = "center"  # left, center, right
f.title.background_fill_color = "lightgray"  # Optional background
f.title.text_font = "times"

# Subtitle
f.add_layout(Title(text="Subtitle", text_font_style="italic"), "above")

# Style the axes
f.xaxis.minor_tick_line_color = "blue"
f.yaxis.major_label_orientation = "vertical"
f.xaxis.visible = True
f.xaxis.minor_tick_in = -6
f.xaxis.axis_label = "Petal Length"
f.yaxis.axis_label = "Petal Width"
f.axis.axis_label_text_color = "blue"
f.axis.major_label_text_color = "orangered"

# Axes geometry
f.x_range = Range1d(start=0, end=10)
f.y_range = Range1d(start=0, end=5)
f.xaxis.bounds = (2, 6)
f.xaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.desired_num_ticks = 2
f.yaxis[0].ticker.num_minor_ticks = 10

# Style the grid
f.xgrid.grid_line_color = None
f.ygrid.grid_line_alpha = 0.6
f.grid.grid_line_dash = [5, 3]


# Adding glyphs
flowers["color"] = [colormap[x] for x in flowers["species"]]

f.circle(
    x=flowers["petal_length"][flowers["species"] == "setosa"],
    y=flowers["petal_width"][flowers["species"] == "setosa"],
    size=flowers["sepal_width"][flowers["species"] == "setosa"] * 4,
    fill_alpha=0.2,
    color=flowers["color"][flowers["species"] == "setosa"],
    legend_label="Setosa",
)

f.circle(
    x=flowers["petal_length"][flowers["species"] == "versicolor"],
    y=flowers["petal_width"][flowers["species"] == "versicolor"],
    size=flowers["sepal_width"][flowers["species"] == "versicolor"] * 4,
    fill_alpha=0.2,
    color=flowers["color"][flowers["species"] == "versicolor"],
    legend_label="Versicolor",
)

f.circle(
    x=flowers["petal_length"][flowers["species"] == "virginica"],
    y=flowers["petal_width"][flowers["species"] == "virginica"],
    size=flowers["sepal_width"][flowers["species"] == "virginica"] * 4,
    fill_alpha=0.2,
    color=flowers["color"][flowers["species"] == "virginica"],
    legend_label="Virginica",
)

# Style the legend
f.legend.location = (575, 555)
f.legend.location = "top_left"
# f.legend.background_fill_alpha = 0
f.legend.border_line_color = None
f.legend.margin = 10
f.legend.padding = 18
f.legend.label_text_color = "olive"
f.legend.label_text_font = "times"

# Save and show the figure
show(f)
