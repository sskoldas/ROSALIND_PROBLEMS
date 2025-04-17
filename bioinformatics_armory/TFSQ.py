
input_file = "rosalind_tfsq.txt"
output_file = "output.fa"

def fastq_to_fasta(fastq_file, fasta_file):
    """
    PROBLEM
    Given: FASTQ file
    Return: Corresponding FASTA records
    """
    with open(fastq_file, 'r') as fq, open(fasta_file, 'w') as fa:
        while True:
            header = fq.readline().strip()
            if not header:
                break  # End of file
            seq = fq.readline().strip()
            fq.readline()  # Skip the '+' line
            fq.readline()  # Skip the quality line
            if header.startswith('@'):
                fa.write('>' + header[1:] + '\n')
                fa.write(seq + '\n')
            else:
                raise ValueError("Incorrect FASTQ format")



## or you can try it by biopython
from Bio import SeqIO

with open(input_file, 'r') as input_fa, open(output_file, 'w') as output_data:
        SeqIO.convert(input_fa, 'fastq', output_data, "fasta")
