
#sample lines from stdin
# command :.r! cat data/q2_data.tsv | head -6
#-1118	1.27553239271999	Cl1
#-1117	1.27696343296042	Cl1
#-1116	1.27829211888462	Cl1
#-1115	1.27953030556019	Cl1
#-1114	1.28067189848055	Cl1
#-1113	1.28170721322425	Cl1


# Load the ggplot2 library
library(ggplot2)

# Retrieve command-line arguments
args <- commandArgs(trailingOnly=TRUE)
output_file <- args[1]          # e.g., "different_clusters.png"
x_label <- args[2]              # e.g., "Relative from center [bp]"
y_label <-  args[3]              # e.g., "Enrichment over Mean"
plot_title <-  args[4]           # e.g., "MNase fragment profile"

# Read data from standard input
data <- read.table(file("stdin"), header=FALSE, sep="\t", col.names=c("X", "Y", "Category"))

# Create the plot
plot <- ggplot(data, aes(x=X, y=Y, color=Category, group=Category)) +
  geom_line() +
  labs(title=plot_title, x=x_label, y=y_label) +
  theme_minimal() +
  theme(legend.title=element_blank())

# Save the plot to output file
ggsave(filename=output_file, plot=plot, width=8, height=6, dpi=300)
