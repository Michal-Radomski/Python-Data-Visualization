# Plotting flower species

# Importing libraries
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]
from bokeh.sampledata.iris import flowers  # type: ignore[import-not-found]

# Define the output file path
output_file("iris.html")

# Create the figure object
f = figure(title="Iris Morphology", width=500, height=400)

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

# Save and show the figure
show(f)
