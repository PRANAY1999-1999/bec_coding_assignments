# bec_coding_assignments

## clone this repository
`git clone https://github.com/manojmahan/bec-513-coding-questions.git`

## question 1
 python code runs through query select from query and find the line matching through big file


 `zcat data/q1_data.tsv.gz | awk 'NR==1||/ENSG/'  | python question1.py data/to_select.tsv  > outputs/q1.tsv`

 ## question 2

 Rcsript will read data from stdin and plot graph for various clusters using ggplot
`cat data/q2_data.tsv | Rscript question2.R "outputs/different_clusters.png" "Relative from center [bp]" "Enrichment over Mean" "MNase fragment profile" `

## question 3

code reading from input file and forming inner join using column 1.here 1st column is key and file are joined by this .

`Rscript join_list_of_files.R data/list_q3.tsv outputs/join_output.tsv`

## question 4

python code will split data and quantiles were assigned with name and range

`cat data/first_hundred_numbers.tsv | python group_in_quantiles.py 4 > outputs/question4.tsv`

## question 5

matrix was formed by removing 1st column which is id string

`zcat data/big_data.tsv.gz | cut --complement -f1 > data/full_data.tsv`

gnu plot script was runned using following command

`gnuplot -e "output='outputs/big_matrix.eps' ; input='data/full_data.tsv' "  gnuplot.gp`

eps file converted to pdf

`ps2pdf outputs/big_matrix.eps outputs/big_matrix.pdf`

gnu plot was not giving results so i plotted with python code

`python plot.py 'data/full_data.tsv'`
