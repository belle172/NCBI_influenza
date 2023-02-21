# -*- coding: utf-8 -*- 
# this script takes in a genetic-distances.txt file created by the script eric_hw3.py, 
# and then creates a new file of the genetic distances, in the format of a header line 
# with the genebank id, then the genetic distance matrix, but with each line starting 
# with the genebank id number of the sequence it is being aligned to 
in_file = "genetic-distances.txt" 
f = open(in_file, 'r') 
out_file = open('genetic_distances_phylo.txt', 'w') 

# extract the taxon id for each sequence and stores it into seq_id 
seq_id = f.readline() 
seq_id = seq_id.split('\t') 
lengh = len(seq_id) 

first_line = str(lengh) 
# first_line = seq_id[0] 

out_line = first_line + '\n' 
out_file.write(out_line) 

for line in f: 
    out_file.write(line) 
    
f.close() 
out_file.close() 

