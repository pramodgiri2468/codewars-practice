def sum_mix(arr):
    """
    Calculate the sum of a list containing integers and numeric strings.

    This function takes a list where elements may be either integers
    or strings representing integers. Each element is converted to
    an integer before summing, and the final result is returned
    as a number.

    Parameters:
    arr (list): A list containing integers and/or strings of integers.

    Returns:
    int: The total sum of all elements after converting them to integers.

    Examples:
    >>> sum_mix([9, 3, '7', '3'])
    22

    >>> sum_mix(['5', '0', 9, 3, 2, '1'])
    20
    """

    return sum(int(x) for x in arr)
# Example usage:
print(sum_mix([9, 3, '7', '3']))  # Output: