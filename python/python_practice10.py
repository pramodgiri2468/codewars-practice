def abbrev_name(name):
    """
    Convert a two-word name into initials.

    Parameters:
    name (str): A string containing exactly two words separated by a space

    Returns:
    str: The initials in uppercase separated by a dot
    """
    first, last = name.split()
    return first[0].upper() + "." + last[0].upper()
print(abbrev_name("john doe"))  # "J.D"
print(abbrev_name("Jane Smith"))  # "J.S"
print(abbrev_name("pramod giri"))  # "P.G"