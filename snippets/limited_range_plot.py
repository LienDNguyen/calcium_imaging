#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# this snippet takes about 2 mins to complete
# since the data file is pretty large (too many rows)
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_with_range(df, x, y, hue, limit, title):
    """
    this function plots a data frame within
    a certain range of x values
    ----------------------
    arguments:
        df    = data frame that holds the data to plot
        x     = `df' column to plot on the x axis
        y     = `df' column to plot on the y axis
        hue   = `df' column to use for grouping
        limit = tuple that determines the min
                and max values of the x axis
        title = title of the plot
    """
    sns.lineplot(x=x, y=y, hue=hue, data=df)
    plt.xlim(limit[0], limit[1])
    plt.title(title)
    plt.show("hold")  # only necessary if run from cmd prompt


# import data from ./assets folder
print("importing data...")
df = pd.read_excel("../assets/CTRL_E120Q.xlsx")

# use the newly defined function for plotting the data
print("plotting data...")
plot_with_range(
    df=df,
    x="Time (s)",
    y="F/Fo",
    hue="Genotype",
    limit=(0, 200),
    title="Plot with Limited x Axis")

# save the plot to the ./assets folder
print("saving plot...")
plt.savefig("limited_range_plot.png", bbox_inches='tight')
