def friend(x):
    """
    Filters and returns names that contain exactly four letters.

    This function takes a list of strings representing names and
    returns a new list containing only those names that have a
    length of exactly four characters. The original order of names
    is preserved.

    Parameters:
    -----------
    x : list of str
        A list containing names made up of alphabetic characters.

    Returns:
    --------
    list of str
        A list containing only names with exactly four characters.

    Example:
    --------
    >>> friend(["Ryan", "Kieran", "Jason", "Yous"])
    ['Ryan', 'Yous']

    >>> friend(["Peter", "Stephen", "Joe"])
    []
    """

    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result
# Function calls
print(friend(["Ryan", "Kieran", "Jason", "Yous"]))
print(friend(["Peter", "Stephen", "Joe"]))