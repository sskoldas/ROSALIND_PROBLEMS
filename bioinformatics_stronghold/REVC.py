from Bio.Seq import Seq

def complementing_strand_of_dna(filename):
    """
    Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s.
    """
    with open(filename, 'r') as file:
        sequence = file.readline().strip()
    
    seq_obj = Seq(sequence)

    reverse_complement = seq_obj.reverse_complement()
    
    print(str(reverse_complement))

filename = "/home/sskoldas/Downloads/rosalind_revc.txt"
complementing_strand_of_dna(filename)
