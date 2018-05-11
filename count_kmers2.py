#!/usr/bin/env python3

import sys
import glob
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Check the sequence
def wrong_character(seq):
    bad_char = {}
    for al in seq:
        if al not in 'GCAT':
            if al in bad_char: bad_char[ al ] += 1
            else: bad_char[ al ] = 1
    if bad_char != {}:
        return bad_char

#Count the kmers
def count_kmers(seq, k):
    counts = {}
    if k>0 and type(k) is int:
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            assert len(kmer) == k, \
            "Trying to add wrong kmer: " +\
            kmer+ "from line" + str(line_num) +\
            " position " + str(i)
            if kmer not in counts:
                counts[kmer] = 0
            counts[kmer] += 1
    return counts

#Generate table
def gen_table(data, name):
    content = pd.DataFrame([[c[0], c[1], c[2]] for c in data],
    columns = ['k', 'observed kmers', 'possible kmers'])
    content.to_csv('output/tables/'+name+'.csv', index=False)

#Generate graph for linguistic complexity
def gen_graph_lc(filename, name_list, linguistic_complexity_counts):
    objects = name_list
    y_pos = np.arange(len(objects))
    value = linguistic_complexity_counts
    plt.figure(0)
    plt.bar(y_pos, value, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Value')
    plt.xlabel('Species')
    plt.title('Linguistic Complexity')
    graph_inital = filename + '_LC.png'
    plt.savefig('output/graphs/'+graph_inital)

#Generate graph for comparison between total obseved and possible kmers
def gen_graph_comp(filename, name_list, observed_total_counts, possible_total_counts):
    fig, ax = plt.subplots()
    index = np.arange(len(name_list))
    bar_width = 0.30
    opacity = 0.70
    rects1 = plt.bar(index, observed_total_counts, bar_width,
                    alpha=opacity, color='blue', label='Observed')
    rects2 = plt.bar(index + bar_width, possible_total_counts, bar_width,
                    alpha=opacity, color='green', label='Possible')
    plt.xlabel('Species')
    plt.ylabel('Number of kmers')
    plt.title('Total Observed vs Possible Kmers')
    plt.xticks(index + bar_width, name_list)
    plt.legend()
    graph_name = filename + '_Comp_Kmers.png'
    plt.savefig('output/graphs/'+graph_name)

#Main function 
if __name__ == "__main__":
    filename=sys.argv[1]
    if filename in glob.glob('*.fasta'):
        f = open(filename,'r')
        seq = f.readlines()
        name_list = []
        observed_total_counts = []
        possible_total_counts = []
        linguistic_complexity_counts = []

        for line_num, line in enumerate(seq[0:len(seq)]):
            if len(line) > 1 :
                if '>' in line :
                    #print("Species Name", line)
                    line = line.replace(">", "")
                    name = line.rstrip()
                    name_list.append(name)
                else:
                    seq = line.rstrip()
                    #print("Sequence =", seq)
                    bad_char = wrong_character(seq)
                    if bad_char != None:
                        print()
                        print('Process stopped! Wrong character sequence detected', bad_char)
                        print('Please corect the sequence and re-run again', line)
                        print()
                        exit()
                    else:
                        k_counts = []
                        observed_counts = []
                        possible_counts = []

                        for k in range(1,len(seq)+1):
                            if k == 1:
                                possible = 4
                            else:
                                possible = len(seq) - k + 1
                            counts = count_kmers(seq, k)
                            observed = len(counts)
                            k_counts.append(k)
                            observed_counts.append(observed)
                            possible_counts.append(possible)
                            #print(k_list, observed_list, possible_list)

                        #counts total observed and possible kmers
                        observed_total = sum(observed_counts)
                        possible_total = sum(possible_counts)
                        linguistic_complexity = observed_total/possible_total
                        observed_counts.append(observed_total)
                        observed_total_counts.append(observed_total)
                        possible_counts.append(possible_total)
                        possible_total_counts.append(possible_total)
                        linguistic_complexity_counts.append(linguistic_complexity)
                        k_counts.append('Total');

                        #generate the data for the table
                        data = list(zip(k_counts, observed_counts, possible_counts))
                        contents = gen_table(data, name)
                       
                        #generate lingustic complexity graph
                        lc_graph = gen_graph_lc(filename, name_list, linguistic_complexity_counts)

                        #generate total observed and possible kmers graphs
                        top_graph = gen_graph_comp(filename, name_list, observed_total_counts, possible_total_counts)

    else:
        print('file is not recognized, it should be .fasta format!')