
from Bio import SeqIO

def computing_gc(filename):
    """
    Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
    """

    with open(filename, 'r') as handle:
        records = list(SeqIO.parse(handle, "fasta"))
        

    highest_gc_content = 0
    highest_gc_id = None


    for record in records:
        GC=0
        total_length = len(record.seq)
        for nucleotide in record.seq:
            if nucleotide == 'G' or nucleotide == 'C':
                GC += 1
        
        gc_content = (GC / total_length) * 100 if total_length > 0 else 0

        if gc_content > highest_gc_content:
            highest_gc_content = gc_content
            highest_gc_id = record.id

    print(f"{highest_gc_id}")
    print(f"{highest_gc_content}")
            

filename = "/home/sskoldas/Downloads/rosalind_gc.txt"
computing_gc(filename)

