
from Bio import Entrez
from Bio import SeqIO

def genbank_to_fasta(ID):

    """
    PROBLEM
    Given: A collection of n (n≤10) GenBank entry IDs.
    Return: The shortest of the strings associated with the IDs in FASTA format.

    """

    Entrez.email = "koldaseda@yahoo.com"

    ids = ",".join(ID)

    handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta", retmode="text")
    records = list(SeqIO.parse(handle, "fasta"))
    handle.close()

    shortest_record = min(records, key=lambda record: len(record.seq))
    return shortest_record.format("fasta")


print(genbank_to_fasta(ID=["FJ817486 JX069768 JX469983"]))