import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

labels = ["events", "ads", "wom"]
values = [3900, 1938, 1131]
colors = ["yellow", "black", "green"]

pyplot.pie(values,
    labels =labels,
    colors =colors
)

pyplot.axis("equal")

pyplot.show()
