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
