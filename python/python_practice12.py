def quarter_of(month):
    """
    Determines which quarter of the year a given month belongs to.

    The year is divided into four quarters:
    - Quarter 1: January (1) to March (3)
    - Quarter 2: April (4) to June (6)
    - Quarter 3: July (7) to September (9)
    - Quarter 4: October (10) to December (12)

    Parameters:
    month (int): An integer representing the month (1 to 12).

    Returns:
    int: The quarter of the year (1 to 4) that the month belongs to.

    Example:
    >>> quarter_of(2)
    1
    >>> quarter_of(6)
    2
    >>> quarter_of(11)
    4
    """
    return (month - 1) // 3 + 1
# Example usage:
print(quarter_of(2))  # Output: 1
print(quarter_of(6))  # Output: 2
print(quarter_of(11)) # Output: 4s