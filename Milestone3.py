def load_file(file):
    
# open and read the input file
    with open(file) as f:
        lines = f.readlines()

# remove the '/n's to get just DNA strings
    dna_list = []
    for i in range(len(lines)):
        dna_list.append(lines[i].replace('\n',''))
        
    return dna_list
  
  
from itertools import permutations

# first creates a function that combines only two strings
def superstring(string1,string2):
    superstring = ""
    test_ss = ""
    if string1 == string2:
        superstring = string1
    else:
# compares end of 1st string and start of 2nd string, with a length of 8 characters
        if string1[-8:] == string2[:8 ]:
            superstring = string1 + string2[8:]
        else:
            superstring = string1 + string2
           
    return superstring
    
def assemble_genome2(dna_list):
    
    superstring_dict = {}
    new_string = ''
    
# tries every possible combo. of strings
    for group in permutations( dna_list,len(dna_list) ):
        
# repeatedly uses superstring function, adding each string in each permutation
        new_string = group[0]
        for i in range(1,len(dna_list)):
            new_string = superstring(new_string,group[i])
# once it reaches the end of a permutation, adds it to dict with its length as the value
            if i == len(dna_list) - 1:
                superstring_dict[ new_string ] = len(new_string)
                
# finds the key of the smallest value
    shortest_string = min(superstring_dict, key = superstring_dict.get)
    
    
    return shortest_string
            
# Source for itertools function: https://docs.python.org/3/library/itertools.html
# Source for finding corresponding key of minimum value: 
# https://stackoverflow.com/questions/3282823/get-the-key-corresponding-to-the-minimum-value-within-a-dictionary

assemble_genome2(load_file('ms3-dna-mammuthus.txt'))
