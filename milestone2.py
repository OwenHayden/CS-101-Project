def get_edges(dna_dict):
    adj_list = []
    for key1, dna1 in dna_dict.items():
            for key2, dna2 in dna_dict.items():
                if key1 != key2 and dna1[-3:] == dna2[:3]:
                    adj_list.append((key1, key2))
            return adj_list

import math
def random_genome(dna, gc_content):
    dna = dna.upper()
    cg = len(dna.replace('A','').replace('T',''))
    at = len(dna.replace('C','').replace('G',''))
    result = []
    for i in range(0, len(gc_content)):
        prob = cg * math.log10(float(gc_content[i]) / 2) + at * math.log10((1 - float(gc_content[i])) / 2)
        result.append(round(prob, 3))
    return result

from itertools import permutations

# first creates a function that combines only two strings (for assemble_genome)
def superstring(string1,string2):
    superstring = ""
    if string1 == string2:
        superstring = string1
    else:
        for i in range(1,len(string1)):
            if string1[-i:] == string2[:i ]:  # compares end of 1st string and start of 2nd string, increasing in length as i increases
                superstring = string1 + string2[i:] # this method naturally selects for smallest string

            elif i == len(string1) - 1 and superstring == '': # when none of the substrings match
                superstring = string1 + string2
                
    return superstring

def assemble_genome(dna_list):
    
    superstring_dict = {}
    new_string = ''
    
    for group in permutations( dna_list,len(dna_list) ):    # tries every possible combo. of strings
        
        new_string = group[0] # repeatedly uses superstring function, adding each string in each permutation
        for i in range(1,len(dna_list)):
            new_string = superstring(new_string,group[i])
            if i == len(dna_list) - 1:  # once it reaches the end of a permutation, adds it to dict with its length as the value
                superstring_dict[ new_string ] = len(new_string)

    shortest_string = min(superstring_dict, key = superstring_dict.get) # finds the key of the smallest value    
    
    return shortest_string
# Source for itertools function: https://docs.python.org/3/library/itertools.html
# Source for finding corresponding key of minimum value: 
# https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary

from math import factorial

def perfect_match(rna):
    
    c = 0
    a = 0
    
    for letter in rna: # counts number of each letter (only 'C' and 'A' are needed because they're equal to 'G' and 'U')
        if letter == 'C':
            c += 1
        elif letter == 'A':
            a += 1
    perfect_matches = factorial(c) * factorial(a) # this is what I worked out to be the formula
    # number of unique pairings for 'C' and 'G' multiplied by those for 'A' and 'U'
    
    return perfect_matches
