import sys
import pandas as pd

#sample lines from stdin
# command : :.r! cat data/first_hundred_numbers.tsv | head -6
#75
#85
#44
#63
#27
#83


data = []
for line in sys.stdin:

    data.extend(line.strip().split('\t'))

data_series=pd.Series(data).astype(float)
binned_data, bin_edges = pd.qcut(data_series, q=int(sys.argv[1]), retbins=True)

labels = ['Q' + str(i+1) + ' (' + str(round(bin_edges[i], 2)) + ' - ' + str(round(bin_edges[i+1], 2)) + ')' for i in range(len(bin_edges) - 1)]
simple_labels = ['Q' + str(i+1) for i in range(len(bin_edges) - 1)]

binned_data_with_labels = pd.qcut(data_series, q=4, labels=labels)
df = pd.DataFrame({
    'Original Values': data_series,
    'Simple Binned Labels': pd.qcut(data_series, q=int(sys.argv[1]), labels=simple_labels),  # Simple Q1, Q2, Q3, Q4
    'Binned Labels with Range': binned_data_with_labels  # With bin ranges
})


# Save DataFrame to TSV file
df.to_csv(sys.stdout, sep='\t', index=False)
