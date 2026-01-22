# Importing libraries
from bokeh.io import curdoc  # type: ignore[import-not-found]
from bokeh.layouts import layout  # type: ignore[import-not-found]
from bokeh.models import ColumnDataSource, Range1d  # type: ignore[import-not-found]
from bokeh.models.annotations import LabelSet  # type: ignore[import-not-found]
from bokeh.models.widgets import Select, Slider  # type: ignore[import-not-found]
from bokeh.plotting import figure  # type: ignore[import-not-found]

# crate columndatasource
source_original = ColumnDataSource(
    dict(
        average_grades=[7, 8, 10],
        exam_grades=[6, 9, 8],
        student_names=["Student_1", "Student_2", "Student_3"],
    )
)

source = ColumnDataSource(
    dict(
        average_grades=[7, 8, 10],
        exam_grades=[6, 9, 8],
        student_names=["Student_1", "Student_2", "Student_3"],
    )
)

# Create the figure
f = figure(x_range=Range1d(start=0, end=12), y_range=Range1d(start=0, end=12))

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


# Create filtering function
def filter_grades(attr, old, new):
    source.data = {
        key: [
            value
            for i, value in enumerate(source_original.data[key])
            if source_original.data["exam_grades"][i] >= slider.value
        ]
        for key in source_original.data
    }
    print(slider.value)


# Create label function
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

slider = Slider(
    start=min(source_original.data["exam_grades"]) - 1,
    end=max(source_original.data["exam_grades"]) + 1,
    value=8,
    step=0.1,
    title="Exam Grade: ",
)
slider.on_change("value", filter_grades)

# Create layout and add to curdoc
lay_out = layout([[select], [slider]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
