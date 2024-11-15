import sys
import pandas as pd

sel_df=pd.read_csv(sys.argv[1],sep='\t',names=['qur'])
big_data_df=pd.read_csv(sys.stdin,sep='\t',header='infer')


#:.r! zcat q1_data_tsv.gz | head -6 (command used to print lines from stdin as comment)
#:set nowrap

#transcript_id(s)	gene_id	length	effective_length	expected_count	TPM	FPKM	posterior_mean_count	posterior_standard_deviation_of_count	pme_TPM	pme_FPKM	TPM_ci_lower_bound	TPM_ci_upper_bound	TPM_coefficient_of_quartile_variation	FPKM_ci_lower_bound	FPKM_ci_upper_bound	FPKM_coefficient_of_quartile_variation
#10904	10904	93.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
#12954	12954	94.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
#12956	12956	72.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
#12958	12958	82.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0
#12960	12960	73.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0.00	0	0	0	0	0	0

sample_df=pd.DataFrame(columns=big_data_df.columns)

for index,rows in sel_df.iterrows():
    query=rows['qur']
    
    # iterate through big_data to check for matching with query(axis=1 is row wise)

    matching_rows = big_data_df[big_data_df.isin([query]).any(axis=1)]

    # concatanating matching rows to new sample dataframe
   
    sample_df = pd.concat([sample_df, matching_rows], ignore_index=True)

#saving sample dataframe to desired output file

sample_df.to_csv(sys.stdout, sep='\t', header=True, index=False)
