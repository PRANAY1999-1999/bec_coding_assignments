#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)
if (length(args) != 1) {
  stop("Usage: Rscript join_list_of_files.R <file_with_list_of_file_names>")
}

library(tidyverse)

# Read the list of file names
file_list <- readLines(args[1])

# Read and standardize column names in all files
data_frames <- lapply(file_list, function(file) {
  df <- readr::read_tsv(file, col_names = TRUE)
  colnames(df)[1] <- "KeyColumn"  # Rename the first column to a common name
  return(df)
})

# Perform inner join on the standardized column
merged_data <- purrr::reduce(data_frames, dplyr::inner_join, by = "KeyColumn")

# Write the result to stdout
write_tsv(merged_data, stdout())


