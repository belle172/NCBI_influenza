# this script takes an input file of sequences and a metadata criteria and creates 
# a file of the sequences with the specified metadata 

# This file is found at https://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/influenza.fna 
# and then ran with the script influenza_file_fixer, found here: 
# https://github.com/belle172/NCBI_data/blob/main/influenza_faa/influenza_file_fixer.py 
# to create the file influenza_fixed.fasta 
# seqs_file = open('influenza.txt') 
seqs_file = open('influenza_fixed.fasta') 

output = open('Minnesota_influenza.txt', 'w') # file for genomes we are interested in 
MN_line = False 

for line in seqs_file: # read in the data 
    if line[0] == '>': # header line 
        MN_line = False 

        if 'Minnesota' in line: 
            output.write(line) 
            MN_line = True 

    else: # sequence line 
        if MN_line == True: 
            output.write(line) 

seqs_file.close() 
output.close() 

