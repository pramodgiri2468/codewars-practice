def reverse_seq(n):
    """
    Generate a list of integers from n down to 1.

    This function takes a positive integer n and returns a list
    containing all integers from n to 1 in descending order.

    Parameters:
    n (int): A positive integer greater than 0.

    Returns:
    list: A list of integers starting from n down to 1.

    Examples:
    reverse_seq(5)
    -> [5, 4, 3, 2, 1]

    reverse_seq(1)
    -> [1]
    """

    return list(range(n, 0, -1))
# Example usage:
print(reverse_seq(5))  # Output: [5, 4, 3, 2, 1]
print(reverse_seq(1))  # Output: [1]