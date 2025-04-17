
from Bio import SeqIO
import sys

def base_filtration_by_quality(filename):

    """
    PROBLEM:
    Given: FASTQ file, quality cut-off value q, Phred33 quality score assumed.
    Return: FASTQ file trimmed from the both ends (removed leading and trailing bases with quality lower than q)
    """

    with open(filename, "r") as handle:
        threshold = int(handle.readline().strip())
        records = list(SeqIO.parse(handle, "fastq"))

    trimmed_records = []
    for record in records:
        phred = record.letter_annotations["phred_quality"]
        seq_len = len(phred)

        # find the start and positions
        start = 0
        while start < seq_len and phred[start] < threshold:
            start +=1
        end = seq_len -1
        while end >= 0 and phred[end] < threshold:
            end -=1

        #trim
        if start <= end:
            trimmed_record = record[start:end+1]
            trimmed_records.append(trimmed_record)
        else:
            pass

    SeqIO.write(trimmed_records, sys.stdout, "fastq")
 
filename = "/home/sskoldas/Downloads/rosalind_bfil.txt"
base_filtration_by_quality(filename)

