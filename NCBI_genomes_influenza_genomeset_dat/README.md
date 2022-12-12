#### This folder, NCBI_genomes_influenza_genomeset_dat, contains the file from https://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/genomeset.dat renamed as genomeset_dat.txt 

#### The folder genomeset_dat contains all the same data as the genomeset_dat.txt file, just split up into multiple .txt files and folders by metadata. This is the structure used for the makeup of the files, with '=' indicating that both sides have the same summation of data. 

NCBI_genomes_influenza_genomeset_dat/ 

    README.md [this file] 

    genomeset_dat.txt = human_influenza.txt + non_human.txt 
    genomeset_dat.txt = [human_MN.txt + human_not_MN.txt] + non_human.txt 
    genomeset_dat.txt = [ human_MN.txt + [human_not_MN_not_USA.txt + human_not_MN_USA.txt] ] + non_human.txt 

These files contain header information for assembled genomes. 