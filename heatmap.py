import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.colors import LinearSegmentedColormap
import sys

data = pd.read_csv(sys.argv[1], sep="\t")

# Create the heatmap
plt.figure(figsize=(8,10))  # Adjust figure size as needed
# Define custom colormap
cmap = LinearSegmentedColormap.from_list(
    "custom_cmap", [(0, "white"), (0.25, "red"), (0.5, "grey"), (0.75, "yellow"), (1, "green")]
)

# Create the heatmap
plt.imshow(data, cmap=cmap, interpolation='nearest', aspect='auto')

plt.gca().invert_yaxis()

plt.ylabel("CTCF ChlP peaks with motif")
plt.title("<80 bp")

plt.savefig("outputs/big_matrix_plot_using_matplotlib.jpeg")
