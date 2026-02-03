def check_for_factor(base, factor):
    """
    Checks whether a given factor is a factor of the base number.

    Parameters:
    base (int): A non-negative integer to be divided.
    factor (int): A positive integer to check as a factor.

    Returns:
    bool: True if factor divides base exactly, False otherwise.
    """
    return base % factor == 0
# Example usage:
print(check_for_factor(10, 2))  # Output: True
print(check_for_factor(10, 3))  # Output: False