def digitize(n):
    """
    Converts a non-negative integer into a list of its digits in reverse order.

    Parameters:
    n (int): A non-negative integer whose digits are to be extracted.

    Returns:
    list[int]: A list containing the digits of the number in reverse order.

    Example:
    >>> digitize(35231)
    [1, 3, 2, 5, 3]

    >>> digitize(0)
    [0]
    """
    return [int(digit) for digit in str(n)][::-1]
# Example usage:
print(digitize(35231))  # Output: [1, 3, 2, 5, 3]
print(digitize(0))      # Output: [0]