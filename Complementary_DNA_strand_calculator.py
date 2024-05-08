def complement_dna(dna_seq):
    # Dictionary to map each nucleotide to its complement
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_strand=[]
    re_dna_seq=list(reversed(dna_seq))
    for base in re_dna_seq:
        complement_strand.append(complement[base])
    complement_strand="".join(complement_strand)
    
    print(f"The complementary DNA strand to {dna_seq} is {complement_strand}")
    
def test_valid(dna_seq):
    # Dictionary to map each nucleotide to its complement
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    valid=True

    for base in dna_seq:
        if not(base in complement):
            valid=False
    
    if valid==False:
        print("Invalid DNA sequence. Only A, T, C, and G are allowed.")
    else:
        complement_dna(dna_seq)
    


dna=input("Please enter the DNA strand:")
test_valid(dna)