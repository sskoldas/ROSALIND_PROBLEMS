from Bio import SeqIO

def count_low_quality_positions_1(fastq_filename):
    """
    PROBLEM:
    Given: FASTQ file, quality threshold q
    Return: Number of positions where mean base quality falls below given threshold
    """

    with open(fastq_filename, "r") as handle:
        threshold_line = handle.readline().strip()
        threshold = int(threshold_line)
        sequence = SeqIO.parse(handle, "fastq")

        position_qualities = []

        for record in sequence:
            qual_scores = record.letter_annotations["phred_quality"]
            if len(position_qualities) < len(qual_scores):
                position_qualities.extend([[] for _ in range(len(qual_scores) - len(position_qualities))])
            for i, score in enumerate(qual_scores):
                position_qualities[i].append(score)

        # Compute mean quality per position and count positions below threshold
        low_quality_count = 0
        for position_scores in position_qualities:
            mean_quality = sum(position_scores) / len(position_scores)
            if mean_quality < threshold:
                low_quality_count += 1

        return low_quality_count




def count_low_quality_positions_2(fastq_filename):
    with open(filename, "r") as handle:
        threshold = int(handle.readline())
        records = list(SeqIO.parse(handle, "fastq"))

        count = 0
        for i in range(0, len(records[0].seq)):
            sum = 0
            for j in range(0, len(records)):
                sum += records[j].letter_annotations["phred_quality"][i]
            if sum / len(records) < threshold:
                count += 1
        print(count)




filename = "/home/sskoldas/Downloads/rosalind_bphr.txt"
print(count_low_quality_positions_1(filename))
print(count_low_quality_positions_2(filename))






