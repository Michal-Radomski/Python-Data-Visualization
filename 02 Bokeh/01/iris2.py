# Importing libraries
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.models import ColumnDataSource  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]
from bokeh.sampledata.iris import flowers  # type: ignore[import-not-found]

colormap = {"setosa": "red", "versicolor": "green", "virginica": "blue"}
flowers["color"] = [colormap[x] for x in flowers["species"]]
flowers["size"] = flowers["sepal_width"] * 4

setosa = ColumnDataSource(flowers[flowers["species"] == "setosa"])
versicolor = ColumnDataSource(flowers[flowers["species"] == "versicolor"])
virginica = ColumnDataSource(flowers[flowers["species"] == "virginica"])

# Define the output file path
output_file("iris2.html")

# Create the figure object
f = figure()

# Adding glyphs
f.circle(
    x="petal_length",
    y="petal_width",
    size="size",
    fill_alpha=0.2,
    color="color",
    legend_label="Setosa",
    source=setosa,
)

f.circle(
    x="petal_length",
    y="petal_width",
    size="size",
    fill_alpha=0.2,
    color="color",
    legend_label="Versicolor",
    source=versicolor,
)

f.circle(
    x="petal_length",
    y="petal_width",
    size="size",
    fill_alpha=0.2,
    color="color",
    legend_label="Virginica",
    source=virginica,
)

# Save and show the figure
show(f)
