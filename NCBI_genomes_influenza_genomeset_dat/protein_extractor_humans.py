# this script takes an input file of sequences and a metadata criteria and creates 
# a file of the sequences with the specified metadata, and a file of the sequences 
# without the metadata 
input_file = open('genomeset_dat.txt') 
output = open('Human_influenza.txt', 'w') # file for genomes we are interested in 
output_2 = open('non_human.txt', 'w') 
genome_line = False 

for line in input_file: # read in the data 
    if 'Human' in line: 
        output.write(line) 

    else: # sequence line 
        output_2.write(line) 

input_file.close() 
output.close() 
output_2.close() 

