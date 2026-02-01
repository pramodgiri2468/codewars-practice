def find_short(s):
    """
    Find the length of the shortest word in a string.

    This function takes a string containing multiple words separated
    by spaces and returns the length of the shortest word.
    The input string is guaranteed to be non-empty.

    Parameters:
    s (str): A string of words separated by spaces.

    Returns:
    int: The length of the shortest word in the string.

    Examples:
    >>> find_short("bitcoin take over the world")
    3

    >>> find_short("simple test")
    4
    """

    return min(len(word) for word in s.split())
# Example usage:
print(find_short("bitcoin take over the world"))  # Output: 3
print(find_short("simple test"))  # Output: 4