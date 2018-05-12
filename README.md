# Assignment_Python - BIO 539
# Counting Kmers and its Linguistic Complexity
## Authors
Deky Rahma Sukarno

## Description
This repository was created as part of Python Assignment on Big Data Analysis course, which attempt to analyse The linguistic complexity of a sequence using Python script.

## Prerequisite
Python 3
Jupyter Notebook
pytest (for testing the script)

## Contents of the repository
This repository consists of:
1. count_kmers2.py : the main script. used to analyse the data
2. test_for_count_kmers2.py : script to test the main script logic
3. count_kmers.ipynb : jupyter notebook script as trial and error of python script that latter used in main script
4. Sample.fasta : sample file as trial data for the script
5. nd2.fasta : the given data to analyze
6. output folder: folder to store the results, contain of "Graphs" and "Tables" folder

## How to
To replicate the process:

A. Install:
1. Install the Python
2. Install the Jupyter Notebook

B. Download:
1. Download all the file. The output folder not neccesary to download, you can create manually later for your analyse.

C. Running the test for the script:
1. Open python/annaconda command prompt
2. Navigate to your script folder
3. Running the test script using this command: pytest

D. Running the script:
1. Put the data file you want to analyze in the same folder with the count_kmers2.py
2. Create folder "output", and within it create folder "Graphs" and "Tables"
3. Open python/annaconda command prompt
4. Navigate to your script folder
5. Running the script using this command: python count_kmers2.py [datafile]
6. The results will stored in graphs and tables folder you created before
7. Sometime you will get an error because of your data contained with wrong character of the sequence. If it is happened, pease check and correct the line before re-run.

## Working procedures in this repository
Procedures performed in this repository included:
1. Create a Seq object that accepts a DNA sequence (a string).
2. Add a method to count kmers of size k, where k is specified as a argument.
3. Add a method to create a pandas data frame containing all possible k and the associated number of observed and expected kmers (see above table).
4. Add a method to produce a graph from the data frame of the proportion of each kmer observed.
5. Add a method to calculate linguistic complexity.
6. Write a script to thoroughly test each of functions.
7. Use the main function to read in sequence data and output results. 


## Acknowledgement
1. Prof. Rachell for all superb things we've learn in Big Data Analysis class
2. Whatsapp Group of BIO539 for all good job n the disscussion

Have a nice summers for all of you out there!
