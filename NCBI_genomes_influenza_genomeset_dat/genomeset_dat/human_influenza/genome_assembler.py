# this script takes a file of header information, and just makes another file of 
# header information, with the lines split into each genome 

# The genomeset.dat file contains information for sequences of viruses with a 
# complete set of segments in full-length (or nearly full-length). Those of the same 
# virus are grouped together (using an internal group ID that is shown in the last 
# column of the file) and separated by an empty line from those of other viruses. 
# the file is a tab-delimitated tables with the following fields: 
# 0. GenBank accession number   1. Host     2. Genome segment number or protein name 
# 3. Subtype    4. Country    5. Year/month/date    6. Sequence length    
# 7. Virus name  8. Age  9. Gender

# open the file containing only the metadata you are interested in from genomeset.dat 
seqs_file = open('human_MN.txt') 

output_file = open('MN_genome_headers.txt', 'w') 

viruses = [] 
count = 0 

for line in seqs_file: # read in the data 

    # get the tab deliminated values from the current line in the header file 
    line_list = line.split('\t') 
    curr_virus = line_list[7] 
    curr_virus = curr_virus.split(' ') 
    curr_virus = curr_virus[-1] 

    if curr_virus not in viruses: 
        count += 1 
        viruses.append(curr_virus) 

        # first header line 
        header = '>' + curr_virus + '\t' + line_list[3] + '\t' + line_list[5] + '\t' 
        header += str(count) + '\n' 
        output_file.write(header) 

        # write the genBank number for the first 7 segments 
        while int(line_list[2]) != 8: 
            # segment header line 
            header = line_list[0] + '\tsegment ' + line_list[2] + '\tlength ' 
            header += line_list[6] + '\n' 
            output_file.write(header) 

            line = seqs_file.readline() 
            line_list = line.split('\t') 

        # write the last segment 
        header = line_list[0] + '\tsegment ' + line_list[2] + '\tlength ' 
        header += line_list[6] + '\n' 
        output_file.write(header) 

seqs_file.close() 
output_file.close() 

