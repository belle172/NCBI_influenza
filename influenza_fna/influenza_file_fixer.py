# fasta file fixer 
# this is for when a downloaded fasta file has sequences spread out over many lines, 
# instead of the whole sequence on one line 

# influenza.txt is the file from 
# https://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/influenza.fna 
file_name = 'influenza.txt' 

file = open(file_name) # read in the fasta file 

# open the new fasta file to write the joined sequence lines in 
new_file = 'influenza_fixed.fasta' 
out_file = open(new_file, 'w') 

first_line = True 

for line in file: # read in the data 
    if line[0] == '>': # header line 
        if first_line == False: 
            out_file.write('\n') 
        out_file.write(line) 
        first_line = False 
    else: # sequence line 
        out_file.write(line[:-1]) 

file.close() 
out_file.close() 

