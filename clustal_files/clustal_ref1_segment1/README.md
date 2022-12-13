This folder, clustal_ref1_segment1, contains files from using the online clustal omega tool, found here: 	https://www.ebi.ac.uk/Tools/services/web/toolresult.ebi?jobId=clustalo-I20221210-022646-0342-31507997-	p1m&analysis=text-summary 
That links to this specific run, which will only be kept in their servers for a short time. If you wanted to recreate the files in this folder, you could go to the clustal alignment tool at https://www.ebi.ac.uk/Tools/msa/clustalo/ and upload the file input_sequences.txt. After 5 minutes, this file was done being aligned, and all of the files were downloaded to this folder from the Results Summary tab. The following list of files in this folder were downloaded from clustal web tool: 
	alignment_clustal_format.clustal_num 
	guide_tree.dnd
	input_sequences.txt 
		- the file that was input to clustal, which was the region_1.txt file in the ref_1 folder, in the proteins folder 
	percent_identity_matrix.txt 
		- this is like the genetic-distances.txt file we got from calculating the genetic/edit distances 
	phylogenetic_tree.txt 
	tool_output.txt 

These files were given the same name as what they are labeled in the Results Summary tab, which is not their default file name. For instance, the first file listed is as: 
Input Sequences
	clustalo-I20221210-022646-0342-31507997-p1m.input 

so that file is named input_sequences.txt instead, for clarity of looking at the files here after they are not available to be downloaded from the clustal website. 

The rest of the files in this folder were obtaining as described: 
	genetic-distances.txt 
	README.md 
		- this file 
