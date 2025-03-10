The files in this script are to be used with data from https://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/, specifically the file influenza.fna, which can be found here: https://ftp.ncbi.nlm.nih.gov/genomes/INFLUENZA/influenza.fna 

When I downloaded 'influenza.fna' in 2022, each sequence was stored across multiple lines instead of the whole sequence on one line. influenza.fna was also downloaded as influenza.txt, so anywhere you see influenza.txt in this repository, that is the same as the influenza.fna file from NCBI, I am just working with the file in .txt format. This leads to the the first of my script files: 
  influenza_file_fixer.py 
which takes in influenza.txt and produces the influenza_fixed.fasta. influenza_fixed.fasta is influenza.txt with each sequence on one line. 

The second script, protein_extractor_from_total.py, takes in influenza_fixed.fasta and creates a file of only the header lines and sequences of samples from Minnesota. The file created is Minnesota_influenza.txt. 

