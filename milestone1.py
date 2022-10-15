def s(dna):
    #calculates number of times each nucleotide appears in a string
    #makes sure string is capatalized 
    dna = dna.upper()
    count_A = dna.count('A')
    count_C = dna.count('C')
    count_G = dna.count('G')
    count_T = dna.count('T')
    return count_A,count_C,count_G,count_T
#calls function and nucleotides being counted
count = s("")
nucleotides = ('A','C','G','T')
#makes a dictionary
#creates an item using nucleotides and subsequent value count
dictionary = dict(zip(nucleotides,count))
print(dictionary)
#sources
#https://appdividend.com/2022/09/24/python-zip-dictionary/
#https://www.youtube.com/watch?v=qj-V2Ep4coY


def dna2rna(dna): #function to convert DNA strand to RNA
    rna = ''
    for symbol in dna:
        if symbol == 'A':
            rna = rna + 'A'
        elif symbol == 'T':
            rna = rna + 'U'
        elif symbol == 'G':
            rna = rna + 'G'
        elif symbol == 'C':
            rna = rna + 'C'
    return rna
def reverse_complement(dna):
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
 

def mendels_law(hom, het, rec):
    from math import factorial
# calculating how many times each pairing occurs (hom and hom, hom and het, etc.)
# formula for unique pairings from https://byjus.com/combination-formula/
    if hom > 1:
        hom_hom = factorial(hom) / (2 * factorial(hom - 2))
    else:
        hom_hom = 0
    hom_het = hom * het
    hom_rec = hom * rec
    if het > 1:
        het_het = factorial(het) / (2 * factorial(het - 2))
    else:
        het_het = 0
    het_rec = het * rec
# calculating total number of pairings using the same formula
    total_pairings = factorial(hom + het + rec) / (2 * factorial(hom + het + rec - 2))
# summing all pairings multiplied by the probability of a dominant offspring for each pairing
# dividing by total pairing converts into a probability
    prob_dom = ((1 * hom_hom) + (1 * hom_het) + (1 * hom_rec) + (0.75 * het_het) + (0.5 * het_rec)) / total_pairings
    return prob_dom

  
def fibonacci_rabbits(n, k):
    #returns 1 for first and second term of sequence (both always equal one).
    if n==1 or n==2:
        return 1
    #fibonacci equation is Fn-1 + Fn-2
    #runs through equation for value n which calculates number of pairs of rabbits
    elif n > 2:
        return fibonacci_rabbits(n-1,k)+k*fibonacci_rabbits(n-2,k)           
#sources
#https://www.programiz.com/python-programming/recursion
#https://www.youtube.com/watch?v=ngCos392W4w


def gc_content(dna_list):
    percent_list = []                                  # empty list that we will fill with GC percentage values
    for strand in dna_list:
        count_gc = strand.count("G")+strand.count("C") # counts G's and C's in each strand
        percent_gc = (count_gc/len(strand))*100        # calculates GC percentage for each strand
        percent_list.append(percent_gc)                # adds GC percentage values for each strand to the list
    max_gc_percent = max(percent_list)                 # finds the maximum percentage value in the list 
    #[REFERENCE]: https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
    max_gc_index = percent_list.index(max_gc_percent)  # finds the index of the maximum percentage value (first value is index 0)
    return (max_gc_index, max_gc_percent)
    

def locate_substring(dna_snippet, dna):
    #establishing a list that contains matches
    matches = []     
    #looking for places there might be a match
    for i in range(len(dna)-len(dna_snippet)+1):   
        #finds a match for the first index
        if dna[i] == dna_snippet[0]:
            match = True
            #checks to see if the rest of the pattern is there
            for n in range(len(dna_snippet)):
                if dna_snippet[n] != dna[i+n]:
                    match = False
                    break
            #adds all locations where theres a match into a list
            if match == True:
                matches.append(i)     
    return matches 
#source
#https://pynative.com/python-nested-loops/
#https://www.youtube.com/watch?v=O60CFmcWyEY
    

def hamming_dist(dna1,dna2):
    list_1 = []
    list_1[:0] = dna1
    
    list_2 = []
    list_2[:0] = dna2
    
    count = 0
    for i in range(0,len(list_1)):
        if list_1[ i ] != list_2[ i ]:
            count += 1
    return count
  

def count_dom_phenotype(genotypes):
# coefficient 2 out front indicates 2 offspring per pairing
# coefficient for each item is percent offspring that are dominant phenotype (first three are coeff. 1)
    dom_offspring = 2 * (genotypes[0] + genotypes[1] + genotypes[2] + 0.75*genotypes[3] + 0.5*genotypes[4])
    return dom_offspring
  

def source_rna(protein):
    # from Lab 3
    rna2codon = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

            'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        }
    # modulo 1000000
    mod = 1000000
    count = 3
    for character in protein:
        temporary = 0
        # Check each key-value in dictionary
        for k,v in rna2codon.items():
            if v == character:
                temporary = (temporary + 1)
        count = (count * temporary)        
    return count%mod
  
def dna2rna(dna):
    rna = ''
    for symbol in dna:
        if symbol == 'A':
            rna = rna + 'A'
        elif symbol == 'T':
            rna = rna + 'U'
        elif symbol == 'G':
            rna = rna + 'G'
        elif symbol == 'C':
            rna = rna + 'C'
    return rna
def splice_rna(dna, intron_list):
    for strand in intron_list:
        dna = dna.replace(strand,"")
    rna = dna2rna(dna)
    return rna2codon(rna)
def rna2codon(triplets):
    amino = ''
    for triplet in range(0,int( len( triplets ) / 3 )):
        triplet = triplets[3*triplet:3*triplet+3]
        amino = amino + rna2codon(triplet)
    return amino
