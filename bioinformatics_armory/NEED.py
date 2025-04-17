# tips: https://www.ebi.ac.uk/jdispatcher/psa/emboss_needle
"""
PROBLEM
Given: Two GenBank IDs.
Return: The maximum global alignment score between the DNA strings associated with these IDs.
"""

from Bio import SeqIO
from Bio import Align
from Bio import Entrez
from Bio.Align import substitution_matrices

file = "/home/sskoldas/Downloads/rosalind_need.txt"

with open(file, 'r') as doc:
    ids_sequences = doc.read().split()

Entrez.email = "koldaseda@yahoo.com"

handle = Entrez.efetch(db='nucleotide', id=ids_sequences, rettype='fasta')

records = list(SeqIO.parse(handle, 'fasta'))

seq_1 = records[0].seq
seq_2 = records[1].seq


align = Align.PairwiseAligner()
matrix = substitution_matrices.load('NUC.4.4')
align.substitution_matrix = matrix
align.open_gap_score = -10
align.extend_gap_score = -1
results = align.score(seq_1, seq_2)

print(results)