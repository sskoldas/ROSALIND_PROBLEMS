"""
PROBLEM
Given: A collection of n (n≤10) DNA strings.
Return: The number of given strings that match their reverse complements.
"""


from Bio import SeqIO
from Bio.Seq import Seq

# Define the file path
file = "/home/sskoldas/Downloads/rosalind_rvco.txt" 

count = 0
# Parse the FASTA file using SeqIO
for record in SeqIO.parse(file, 'fasta'):
    seq = record.seq
    if seq == seq.reverse_complement():
        count += 1

print(count)