
from Bio import SeqIO

file = "rosalind_phre.txt"

def read_quality_distribution(file):
    """
    PROBLEM
    Given: A quality threshold, along with FASTQ entries for multiple reads.
    Return: The number of reads whose average quality is below the threshold.
    """
    
    with open(file, "r") as handle:
       threshold = int(handle.readline())
       records = SeqIO.parse(handle, "fastq")

    # Initialize a counter for the number of records below the threshold
    count = 0

    # Iterate over each record in the FASTQ file
    for record in records:
        # Get the list of PHRED quality scores for the current record
        phred_scores = record.letter_annotations["phred_quality"]

        # Calculate the average quality score
        average_quality = sum(phred_scores) / len(phred_scores)
    
        # Check if the average quality is below the threshold
        if average_quality < threshold:
            count += 1  # Increment the counter

    # Print the total count of records below the threshold
    print(count)
