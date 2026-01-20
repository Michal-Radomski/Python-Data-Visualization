# Plotting flower species

# Importing libraries
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.models import Title  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]
from bokeh.sampledata.iris import flowers  # type: ignore[import-not-found]

# Define the output file path
output_file("iris.html")

# Create the figure object
f = figure(title="Iris Morphology", width=1200, height=700)

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
f.axis.major_label_text_color = "orange"

# Save and show the figure
show(f)
