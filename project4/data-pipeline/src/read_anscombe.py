# use pandas to read the anscombe dataset
# use seaborn to plot the anscombe dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
def load_data(file_path):
    data = pd.read_json(file_path)
    return data


# load anscombe.csv file
file_path = "./data/anscombe.json"
data = load_data(file_path)
print(data.head())

# plot the anscombe dataset
sns.set_theme(style="whitegrid")
sns.set(style="ticks")
sns.load_dataset("anscombe")

sns.lmplot(
    x="X",
    y="Y",
    col="Series",
    hue="Series",
    data=data,
    col_wrap=2,
    ci=None,
    palette="muted",
    height=4,
    scatter_kws={"s": 50, "alpha": 1},
)

# what is kde in displot?
# kde: bool, default=False
# Whether to plot a gaussian kernel density estimate.
# This is useful when you have a large number of data points and the density of the data is not clear.
# It can be thought of as a smoothed version of the histogram.

sns.displot(data, x="X", col="Series", kde=True)

sns.color_palette("pastel")

# create a visualization of the anscombe dataset
plt.show()
