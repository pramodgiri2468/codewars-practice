def row_sum_odd_numbers(n):
    """
    Calculate the sum of the numbers in the nth row of a triangle
    of consecutive odd numbers.

    In a triangle formed by consecutive odd numbers, the sum of
    the numbers in the nth row follows a mathematical pattern:
    the sum is equal to n³ (n cubed).

    Parameters:
    n (int): The row number (starting from 1).

    Returns:
    int: The sum of the odd numbers in the nth row.

    Examples:
    >>> row_sum_odd_numbers(1)
    1

    >>> row_sum_odd_numbers(2)
    8

    >>> row_sum_odd_numbers(4)
    64
    """

    return n ** 3
# Example usage:
print(row_sum_odd_numbers(1))  # Output: 1
print(row_sum_odd_numbers(2))  # Output: 8
print(row_sum_odd_numbers(4))  # Output: 64