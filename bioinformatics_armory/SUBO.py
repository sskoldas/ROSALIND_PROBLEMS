
def read_fasta(filename):
    """
    Read the DNA sequences 's' and 't' from the FASTA-formatted files.
    """
    with open(filename, "r") as file:
        sequences = {}                                          #to store sequence names as keys and sequences as values
        sequence_name =""
        sequence_data = ""
        for line in file:
            if line.startswith('>'):
                if sequence_name != "":
                    sequences[sequence_name] = sequence_data
                    sequence_data = ""                          #resets sequence_data for the next sequence
                sequence_name = line[1:].strip()                #extracts the sequence name by removing the > character and any leading/trailing whitespace
            else:
                sequence_data += line.strip()
        if sequence_name:                                       #ensures that the last sequence read is added to the sequences dictionary. 
            sequences[sequence_name] = sequence_data
    return sequences


def generate_substrings(sequence, min_len=32, max_len=40):
    """
    Extract all substrings of length 32 to 40 bp from 's' and 't' by using a sliding window approach.
    """
    substrings = set()                                          #automatically removes dublicates, and useful for considering each unique substring only once.
    for length in range(min_len, max_len + 1):
        for i in range(len(sequence)-length+1):
            substrings.add(sequence[i:i+length])
    return substrings


def hamming_distance(sequence_1, sequence_2):                   #Hamming distance requires strings of equal length.
    """
    Compute Hamming distance by comparing each character in the two strings and counting the number of mismatches.
    """
    return sum([x != y for x, y in zip(sequence_1, sequence_2)])


def count_approaximate_matches(substring, sequence, max_edits=3):
    """
    Identify potential repeats and count number of matches allowing up to 3 variations.
    """
    count=0
    length=len(substring)
    for i in range(len(sequence) - length+1):
        window=sequence[i:i+length]
        distance=hamming_distance(substring, window)       
        if distance <= max_edits:
            count += 1
    return count    


def find_repeat_substring(substrings, s_sequence, t_sequence):
    """
    Identify the substring that occurs multiple times in both s and t with up to 3 variations.
    """
    max_total_occurence=0
    repeat_substring=""
    for substring in substrings:
        s_count = count_approaximate_matches(substring, s_sequence)
        t_count = count_approaximate_matches(substring, t_sequence)
        if s_count > 1 and t_count > 0:
            total_occurences = s_count + t_count
            if total_occurences > max_total_occurence:
                max_total_occurence = total_occurences
                repeat_substring = substring
    return repeat_substring


def total_occurences(r, s_sequence, t_sequence):
    s_count = count_approaximate_matches(r, s_sequence)
    t_count = count_approaximate_matches(r, t_sequence)
    return s_count, t_count


def main():
    sequences = read_fasta("/home/sskoldas/Downloads/rosalind_subo.txt")
    sequence_list = list(sequences.values())
    s_sequence = sequence_list[0]
    t_sequence = sequence_list[1]

    # generate candidate substrings from s sequence
    s_substrings = generate_substrings(s_sequence)

    # find the repeat substring r
    r = find_repeat_substring(s_substrings, s_sequence, t_sequence)
    if not r:
        print("No repeat substring found.")
        return
    
    # count the total occurences in s and t
    s_count, t_count = total_occurences(r, s_sequence, t_sequence)
    print(f"{s_count} {t_count}")

if __name__=="__main__":
    """
    PROBLEM:
    Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r of 32-40 bp. By "inexact" we mean that r may appear with slight modifications (each repeat differ by ≤3 changes/indels).
    Return: The total number of occurrences of r as a substring of s, followed by the total number of occurrences of r as a substring of t.
    """
    main()
