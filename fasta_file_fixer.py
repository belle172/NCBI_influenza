# fasta file fixer 
# this function is for when a downloaded fasta file has sequences spread out over 
# many lines, instead of the whole sequence being on one line 
import os 

# change if needed to folder containing fasta files  
folder_name = 'human_influenza_ref_genomes' 
# folder_name = 'refGen_fasta' 

working_directory = os.getcwd() 
folder_path = working_directory + '\\' + folder_name 
files_list = os.listdir(folder_path) 

# folder to put new files in 
# os.mkdir(working_directory + '\\fixed_fastas') 
new_folder = working_directory + '\\fixed_fastas' 

for filename in files_list: # for each file in the folder 
    first_line = True # first line of this file 

    file_path = folder_path + '\\' + filename 
    file = open(file_path) # read in the fasta file 

    # open the new fasta file to write the joined sequence lines in 
    new = filename.split('.') # don't include file type in new file name 
    new_file = new_folder + '\\' + new[0] + '_fixed.fasta' 
    out_file = open(new_file, 'w') 

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

