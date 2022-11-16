def shared_motif(dna_list):
    
    longest_motif = ''
    
    for i in range(len(dna_list[0])):
        
        for j in range(i+1, len(dna_list[0])+1):
            
             motif = (dna_list[0])[i:j]   #finds all motifs for first DNA sequence in the list
                
             seq_index = 1  #index of the first motif
            
            #determine if each motif from first sequence is in all the other sequences:
             for str_num in range(1,len(dna_list)):
                if motif in dna_list[seq_index] and seq_index + 1 == len(dna_list) and len(longest_motif) < len(motif):
                        
                        # If a motif is in all sequences and is longer than the previous longest motif, it becomes the new longest common motif.
                        longest_motif = motif
                        
    return longest_substring
         
#REFERENCES: 
#https://www.folkstalk.com/tech/longest-common-substring-with-code-examples/
#https://www.geeksforgeeks.org/longest-common-substring-array-strings/                                                 
            
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



def reverse_complement(dna): #Code taken from Milestone 1
    
    dna = dna.upper()
    complementary_strand = ''
    
    
    for base in dna:   #for loop matches each base to its complementary base
        if base == 'A':
            complementary_strand = complementary_strand + 'T'
        elif base == 'C':
             complementary_strand = complementary_strand + 'G'
        elif base == 'T':
             complementary_strand = complementary_strand + 'A'
        elif base == 'G':
             complementary_strand = complementary_strand + 'C'
    
    reverse_complement = complementary_strand [::-1] #reverses the complementary DNA strand
    
    return reverse_complement



def rev_palindrome(dna):     
    tuples_list = []      
    
    #nested for loop checks all possible pieces of dna from 4 to 12 bp
    
    for i in range(len(dna)-4):         
       
    
        if len(dna) > i+12:
            
            #if dna is more than 12 bp the min length of a piece is 3 bp and max length is 12 bp
            
            for j in range(i+3,i+12):    
                piece_of_dna = dna[i:j+1]  #all possible pieces starting at a particular i
                if reverse_complement(piece_of_dna) == piece_of_dna: #if reverse complement of a piece is the original piece, it's a palindrome!             
                    tuples_list.append((i,j-i+1)) #position (i) is where the piece starts, so length of the piece is found by j-(i+1)
        
        else: 
            
            #if dna is less than 12 bp the max length of a piece is whatever length the dna strand is, but otherwise, the loop is the same
            
            for j in range(i+3,len(dna)):                          
                piece_of_dna = dna[i:j+1] 
                if reverse_complement(piece_of_dna) == piece_of_dna:                 
                    tuples_list.append((i,j-i+1))
    
    return tuples_list

#reference1 = https://datagy.io/python-palindrome/ 
#reference2 = https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/


