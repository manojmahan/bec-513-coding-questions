import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap

data = pd.read_csv("data/full_data.tsv", sep="\t")

# Create the heatmap
plt.figure(figsize=(2,5))  # Adjust figure size as needed
# Define custom colormap
cmap = LinearSegmentedColormap.from_list(
    "custom_cmap", [(0, "white"), (0.25, "red"), (0.5, "grey"), (0.75, "yellow"), (1, "green")]
)

# Create the heatmap
plt.imshow(data, cmap=cmap, interpolation='nearest', aspect='auto')

plt.gca().invert_yaxis()

plt.savefig("x.jpeg")