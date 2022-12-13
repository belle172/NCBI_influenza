# -*- coding: utf-8 -*- 
# Written by Eric Docka for CSCI 5481 hw3 
# then co opted by jasper for our project. all i did was moderately fail at making it 
# run faster and other comment / whitespace things 

# this script takes in a fasta file and creates the file genetic-distances.txt 
import numpy as np 
import pandas as pd 

fna = "refGen2Seg5_fixed.fasta" # input fasta file (.fna or .fasta or .txt) 
file_csv = "genetic-distances.txt" 

f = open(fna, 'r') # read the fasta file 'fna' 
seq_list = [] # seq_list stores the sequence of each seq_id 
seq_id = [] # extract the taxon id for each sequence and stores it into seq_id 
for line in f: 
    if line[0] == '>':
        seq_id += [ line[1:].strip() ] 
    else: 
        seq_list += [ line.strip() ] 

f.close() 

miss = 0 # count of positive score for mismatches 
denom = len(seq_list[0]) # length of strand to divide miss score by 
num_seqs = len(seq_list) 

# create the initial distance matrix for the tips called score_mat 
score_mat = np.zeros( (num_seqs, num_seqs), dtype = np.int64 )
score_mat = score_mat.astype(float) 

# Entries in each nucleotide strand are compared. Gaps are considered matches 
for i in range(num_seqs): 
    if i != num_seqs: 
        for j in range(num_seqs): 
            miss = 0
            for k in range(len(seq_list[i])): 
                if seq_list[i][k] != seq_list[j][k]:
                     miss += 1 
            score_mat[i][j] = miss / denom 

txt_rows = [[]] * num_seqs 
txt_row = [] 

# create a list of lists, each nested list in txt_rows represents a row 
# in the distance matrix ordered from the first sequence in seq_list to the last. 
for i in range(num_seqs): 
    for j in range(num_seqs): 
        txt_row = txt_row + [score_mat[i][j]]
    txt_rows[i] = txt_row
    txt_row = []

tax_dict = {} # populate dictionary tax_dict with rows from the distance matrix, 

# assigning the appropriate taxon IDs to the distance row they are associated with 
for i in range(num_seqs): 
    tax_dict[seq_id[i]] = txt_rows[i] # The keys are taxon IDs and the values are lists 

# Uses the panda library to generate a tab-delimited genetic-distances file 
df = pd.DataFrame.from_dict(tax_dict , columns = seq_id , orient = 'index')
df.to_csv(file_csv, sep = '\t') 

