def lovefunc(flower1, flower2):
    """
    Determine whether two people are in love based on flower petals.

    This function checks the number of petals on two flowers. If one
    flower has an even number of petals and the other has an odd number,
    the function returns True, indicating they are in love. Otherwise,
    it returns False.

    Parameters:
    flower1 (int): The number of petals on the first flower.
    flower2 (int): The number of petals on the second flower.

    Returns:
    bool: True if one flower has an even number of petals and the other
          has an odd number; False otherwise.

    Examples:
    lovefunc(4, 7)
    -> True

    lovefunc(6, 10)
    -> False

    lovefunc(5, 9)
    -> False
    """

    return (flower1 % 2) != (flower2 % 2)
# Example usage:
print(lovefunc(4, 7))   # Output: True
print(lovefunc(6, 10))  # Output: False
print(lovefunc(5, 9))   # Output: False