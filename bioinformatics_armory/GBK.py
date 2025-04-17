



from Bio import Entrez

def find_number_nucleotide_entry(name, start_date, end_date):

    """
    PROBLEM
    Given: A genus name, followed by two dates in YYYY/M/D format.
    Return: The number of Nucleotide GenBank entries for the given genus that were published between the dates specified.

    """

    Entrez.email = "koldaseda@yahoo.com"

    query = f'"{name}"[Organism]'

    handle = Entrez.esearch(db="nucleotide", term=query, datetype="pdat", mindate=start_date, maxdate=end_date)
    record = Entrez.read(handle)
    return record["Count"]
