
def filter_fastq_by_quality(q, p, fastq_file):
    """
    PROBLEM
    Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.
    Return: Number of reads in filtered FASTQ entries

    """
    filtered_read_count = 0

    with open(fastq_file, 'r') as f:
        while True:
            # Read one FASTQ entry (4 lines)
            identifier = f.readline().strip()
            if not identifier:
                break  # End of file
            sequence = f.readline().strip()
            plus_line = f.readline().strip()
            quality_string = f.readline().strip()

            # Convert quality string to quality scores
            quality_scores = [ord(char) - 33 for char in quality_string]

            # Count bases with quality >= q
            high_quality_bases = sum(score >= q for score in quality_scores)
            percentage = (high_quality_bases / len(quality_scores)) * 100

            if percentage >= p:
                filtered_read_count += 1

    return filtered_read_count

# Example usage:
q = 18  # Quality threshold
p = 69.0  # Percentage threshold
fastq_file = "/home/sskoldas/Downloads/rosalind_filt.txt"

num_filtered_reads = filter_fastq_by_quality(q, p, fastq_file)
print(f"Number of reads in filtered FASTQ entries: {num_filtered_reads}")


# or you can use this code by importing SeqIO

from Bio import SeqIO

with open(fastq_file, "r") as f:
    threshold= f.readline().strip().split()

record = SeqIO.parse(fastq_file, "fastq")

count=0
for i in record:
    phred=i.letter_annotations["phred_quality"]
    passes=0
    for j in phred:
        if j >=int(threshold[0]):
            passes +=1
    if (passes/float(len(phred)))*100 >= float(threshold[1]):
        count +=1
print(count)