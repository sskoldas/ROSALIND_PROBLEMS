

def counting_dna_nucleotides (filename):
    """
    Given: A DNA string s of length at most 1000 nt.
    Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    """

    with open(filename, "r") as file:
        sequence = file.readline().strip()

    A = T = C = G = 0
    for i in sequence:
        if i == 'A':
            A +=1
        elif i == 'T':
            T +=1
        elif i == 'C':
            C +=1
        else:
            G +=1
    
    print(f"{A} {C} {G} {T}")

filename="/home/sskoldas/Downloads/rosalind_dna.txt"
counting_dna_nucleotides(filename)