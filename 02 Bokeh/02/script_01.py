# * Run: python3 -m bokeh serve script_01.py
# Importing libraries
from bokeh.io import curdoc  # type: ignore[import-not-found]
from bokeh.layouts import layout  # type: ignore[import-not-found]
from bokeh.models import ColumnDataSource  # type: ignore[import-not-found]
from bokeh.models.annotations import LabelSet  # type: ignore[import-not-found]
from bokeh.models.widgets import Select  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# Create columndatasource
source = ColumnDataSource(
    dict(
        average_grades=["B+", "A", "D-"],
        exam_grades=["A+", "C", "D"],
        student_names=["Student_1", "Student_2", "Student_3"],
    )
)

# Define the output file path
# output_file("script_01.html")

# Create the figure
f = figure(
    x_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
    y_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
)

# Add labels for glyphs
labels = LabelSet(
    x="average_grades",
    y="exam_grades",
    text="student_names",
    x_offset=5,
    y_offset=5,
    source=source,
)
f.add_layout(labels)

# Create glyphs
f.circle(x="average_grades", y="exam_grades", source=source, size=8)


# Create function
def update_labels(attr, old, new):
    labels.text = select.value


# Create select widget
options = [
    ("average_grades", "Average Grades"),
    ("exam_grades", "Exam Grades"),
    ("student_names", "Student Names"),
]
select = Select(title="Attribute", options=options)
select.on_change("value", update_labels)

# Create layout and add to curdoc
lay_out = layout([[select]])
curdoc().add_root(f)
curdoc().add_root(lay_out)

# show(lay_out)
