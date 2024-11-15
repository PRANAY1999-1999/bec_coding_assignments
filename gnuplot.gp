# Set terminal to postscript with size and font
set terminal postscript size 6,6 font 'Arial, 15'

# Output file 
set output output

# Set color palette (you can modify it as per your preference)
set palette defined ( 0 'blue', 0.25 'cyan', 0.5 'green', 0.75 'yellow', 1 'red')

# Set title
set title "<80 bp"

# Set labels for axes
set xlabel "Columns"
set ylabel "CTCF ChlP peaks with motif"

unset grid
unset colorbox
set border linewidth 1.5

set view map
set size ratio -0.04

# Plot the matrix (using the gzipped tsv file)
plot input matrix with image
