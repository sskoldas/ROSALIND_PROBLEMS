from Bio import SeqIO
from Bio.Seq import Seq

def finding_genes_with_orf(file_path):
    """
    PROBLEM
    Given: A DNA string s of length at most 1 kbp.
    Return: The longest protein string that can be translated from an ORF of s.
    If more than one protein string of maximum length exists, then you may output any solution.
    """

    # Read the DNA sequence from the file
    try:
        # Attempt to read as FASTA
        record = SeqIO.read(file_path, "fasta")
        dna_seq_obj = record.seq
    except:
        # If not FASTA, read the entire file and remove newlines
        with open(file_path, 'r') as f:
            lines = f.readlines()
            # Remove headers (lines starting with '>') and join the rest
            dna_seq = ''.join(line.strip() for line in lines if not line.startswith('>'))
            dna_seq_obj = Seq(dna_seq)

    # Generate the reverse complement
    rev_seq_obj = dna_seq_obj.reverse_complement()

    sequences = [dna_seq_obj, rev_seq_obj]

    protein_seqs = set()

    for seq in sequences:
        for frame in range(3):
            # Translate the sequence in the current reading frame
            translated_seq = seq[frame:].translate(to_stop=False)
            aa_seq = str(translated_seq)
            length = len(aa_seq)

            # Search for ORFs starting with 'M' and ending with '*'
            for i in range(length):
                if aa_seq[i] == 'M':
                    for j in range(i + 1, length):
                        if aa_seq[j] == '*':
                            protein = aa_seq[i:j]
                            protein_seqs.add(protein)
                            break  # Stop at the first stop codon
                    else:
                        # No stop codon found; skip incomplete protein
                        continue

    if protein_seqs:
        longest_protein = max(protein_seqs, key=len)
        print(longest_protein)
        return longest_protein
    else:
        print("No protein found")
        return None

# Example usage:
file_path = "/home/sskoldas/Downloads/rosalind_orfr.txt"
print(finding_genes_with_orf(file_path))
