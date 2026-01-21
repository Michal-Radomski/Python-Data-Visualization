# Importing libraries
from bokeh.io import output_file, show  # type: ignore[import-not-found]
from bokeh.models import ColumnDataSource  # type: ignore[import-not-found]
from bokeh.models.annotations import Label, LabelSet  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# Prepare the output
output_file("script_03.html")

# Create ColumnDataSource
source = ColumnDataSource(
    dict(
        average_grades=["B+", "A", "D-"],
        exam_grades=["A+", "C", "D"],
        student_names=["Student_1", "Student_2", "Student_3"],
    )
)

# Create the figure
f = figure(
    x_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
    y_range=["F", "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+"],
)

# Add description label
description = Label(
    x=7,
    y=1,
    text="This graph shows average grades and exam grades for 3rd grade students",
)
f.add_layout(description)

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

show(f)
