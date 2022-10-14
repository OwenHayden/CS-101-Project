def s(dna): #place the s(dna) function here when complete



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
  
  # add dunction here when completed
  


def gc_content(dna_list):
    
    
    percent_list = []                                  # empty list that we will fill with GC percentage values
    
    for strand in dna_list:
       
        count_gc = strand.count("G")+strand.count("C") # counts G's and C's in each strand
        
        
        
        percent_gc = (count_gc/len(strand))*100        # calculates GC percentage for each strand
        percent_list.append(percent_gc)                # adds GC percentage values for each strand to the list
        
        
    
    
    max_gc_percent = max(percent_list)                 # finds the maximum percentage value in the list [REFERENCE]: https://www.adamsmith.haus/python/answers/how-to-find-the-index-of-the-max-value-in-a-list-in-python
    
    max_gc_index = percent_list.index(max_gc_percent)  # finds the index of the maximum percentage value (first value is index 0)
   
    
    return (max_gc_index, max_gc_percent)
    
  
  
def locate_substring(dna_snippet, dna):
    
    # add function here when complete
    
  
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
  
  
  def splice_rna(dna, intron_list):
    
