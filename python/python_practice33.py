def dna_to_rna(dna):
    """
    Converts a DNA sequence into an RNA sequence.

    Parameters:
    dna (str): A string representing a DNA sequence consisting
               only of the characters 'G', 'C', 'A', and 'T'.

    Returns:
    str: The corresponding RNA sequence where all 'T' characters
         are replaced with 'U'.
    """
    return dna.replace('T', 'U')
# Example usage:
print(dna_to_rna("GATTACA"))  # Output: "GAUUACA"
print(dna_to_rna("CGTA"))     # Output: "CGUA"