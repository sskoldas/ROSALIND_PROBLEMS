
from Bio.Seq import Seq
from Bio.Data import CodonTable

def dna_to_protein(file_path):

    """
    PROBLEM
    Given: A DNA string s of length at most 10 kbp, and a protein string translated by s
    Return: The index of the genetic code variant that was used for translation. (If multiple solutions exist, you may return any one.)
    """

    with open(file_path, 'r') as f:
        input_lines = f.read().splitlines()
        dna_seq = input_lines[0].strip()
        protein_seq = input_lines[1].strip()

    # Convert DNA sequence to a Seq object
    dna_seq_obj = Seq(dna_seq)

    for index in CodonTable.ambiguous_dna_by_id.keys():
        translated_seq = dna_seq_obj.translate(table=index, stop_symbol='', to_stop=False, cds=False)
        
        if str(translated_seq) == protein_seq:
            print(index)
            return index

    print("No matching genetic code index found.")
    return None


file_path = "/home/sskoldas/Downloads/rosalind_ptra.txt"
print(dna_to_protein(file_path))
