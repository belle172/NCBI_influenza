# -*- coding: utf-8 -*- 
''' 
Created Dec 12 2022 
Python 3.10 
@author: Jasper Bellefeuille - belle172@umn.edu 
Repository: NCBI_influenza/folder_reader.py

This script reads in two folders of fasta formatted files, where each file is the genes of an 
organism, and all the files are of the same species. The script creates files of each gene across 
all inputted organisms. 

Input files = all genes per individual, output files = all individuals per gene 
Files in the first input folder each contain a reference genome 
Files in the second input folder each contain a genome to be aligned against the reference genomes 

Script requirements: 
    each sequence is preceeded by a header line, starting with '>segment ' 
    All files have the same number of genes (or sequences followed by header lines) 
''' 

import os 
import glob 

def read_fasta_file(file): # read the fasta file sequences 
    sequences = {} 
    ids = []
    filename = glob.glob(file) 
    with open(filename) as f: 
        lines = f.read().splitlines()
    curr = None 
    for index, line in enumerate(lines): 
        if index % 2 == 0:
            curr = line[1:]
            ids.append(curr) 
        else:
            sequences[curr] = line
    return ids, sequences 

ref_folder_name = 'human_influenza_ref_genomes' # change if needed to folder of refs 
genomes_folder_name = 'influenza_MN_genomes'    # change if needed to folder name 

# file paths as string variables 
working_directory = os.getcwd() 
ref_folder_path = working_directory + '\\' + ref_folder_name 
genomes_folder_path = working_directory + '\\' + genomes_folder_name 
# os.mkdir(working_directory + '\\proteins') # TODO: make this into a try except block 
new_files_path = working_directory + '\\proteins\\' 

# os.listdir() gives the names of all the files in the inputted path as a list 
ref_files_list = os.listdir(ref_folder_path) 
genomes_files_list = os.listdir(genomes_folder_path) 

for filename in ref_files_list: # for each file in the list of reference genomes 
    regions_count = 0 
    new_ref_folder_path = new_files_path + filename 
    region_folder = new_ref_folder_path + '\\region_' 

    file_path = ref_folder_path + '\\' + filename 
    # os.mkdir(new_files_path + '\\' + filename) 
    ref_file = open(file_path) 

    for ref_line in ref_file: # read in the data 

        # for each header line in each reference genome file 
        if ref_line[0] == '>': # header line 
            header = ref_line.split('segment ') 
            header = header[1].split(',') 

            regions_count += 1 # we are in a new header line / region 
            region_filename = region_folder + str(regions_count) + '.txt' 
            output_file = open(region_filename, 'w') 

            # write the header line for the reference protein 
            ref_header = ref_line[:-1] + ', REFERENCE PROTEIN SEQUENCE\n' 
            output_file.write(ref_header) 

            # write the reference protein sequence to the new file 
            output_file.write(ref_file.readline()) 

            # write the sequences of that segment from all the other genomes 
            for genome_to_align in genomes_files_list: # for each genome file 
                current_genome = genomes_folder_name + '\\' + genome_to_align 
                genome_file = open(current_genome) 

                for genome_line in genome_file: # read in the data 
                    if genome_line[0] == '>': # header line 

                        # get the line for the specific segment we are in 
                        genome_header = genome_line.split('segment ') 
                        genome_segment = genome_header[1].split(' ') 
                        if header[0] == genome_segment[0]: 
                            output_file.write(genome_line) 
                            output_file.write(genome_file.readline()) 

                genome_file.close() 

            # done write all of this segment, for this reference file 
            output_file.close() 

    ref_file.close() 
# end of for loop going through each file in the folder of reference genomes 

