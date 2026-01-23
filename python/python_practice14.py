def paperwork(n, m):
    """
    Calculate the total number of pages needed to copy paperwork.

    This function determines how many blank pages are required
    when 'n' classmates each need a copy of paperwork consisting
    of 'm' pages. If either the number of classmates or the number
    of pages is negative, the function returns 0.

    Parameters:
    n (int): The number of classmates.
    m (int): The number of pages in the paperwork.

    Returns:
    int: The total number of pages needed, or 0 if the input
         values are invalid (negative).

    Examples:
    paperwork(5, 5)
    -> 25

    paperwork(-5, 5)
    -> 0

    paperwork(5, -5)
    -> 0
    """

    if n < 0 or m < 0:
        return 0
    return n * m
# Example usage:
print(paperwork(5, 5))   # Output: 25
print(paperwork(-5, 5))  # Output: 0
print(paperwork(5, -5))  # Output: 0