# this script takes an input file of sequences and a metadata criteria and creates 
# a file of the sequences with the specified metadata, and a file of the sequences 
# without the metadata 
input_file = open('human_not_MN.txt') 
output = open('human_not_MN_USA.txt', 'w') # file for genomes we are interested in 
output_2 = open('human_not_MN_not_USA.txt', 'w') 

for line in input_file: # read in the data 
    if 'USA' in line: 
        output.write(line) 

    else: # sequence line 
        output_2.write(line) 

input_file.close() 
output.close() 
output_2.close() 

