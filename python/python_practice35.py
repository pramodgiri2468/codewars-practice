import math

def find_next_square(sq):
    """
    Finds the next perfect square after the given number.

    A perfect square is a number whose square root is an integer.
    If the given number is itself a perfect square, this function
    returns the next perfect square. Otherwise, it returns -1.

    Parameters:
    sq (int): A non-negative integer to check.

    Returns:
    int: The next perfect square if `sq` is a perfect square,
         otherwise -1.

    Examples:
    find_next_square(121) -> 144
    find_next_square(625) -> 676
    find_next_square(114) -> -1
    """
    
    root = math.sqrt(sq)

    if root.is_integer():
        next_root = int(root) + 1
        return next_root ** 2
    else:
        return -1
# Example usage:
print(find_next_square(121))  # Output: 144
print(find_next_square(625))  # Output: 676
print(find_next_square(114))  # Output: -1