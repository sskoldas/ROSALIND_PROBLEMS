
def dna_to_rna(filename):
    """
    Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t.
    """

    with open(filename, 'r') as file:
        dna_seq = file.readline().strip()

    rna_seq = dna_seq.replace('T','U')
    
    print(rna_seq)

filename = "/home/sskoldas/Downloads/rosalind_rna.txt"
dna_to_rna(filename)