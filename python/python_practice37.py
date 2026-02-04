def binary_array_to_number(arr):
    """
    Converts an array of 0s and 1s to its decimal equivalent.

    Parameters:
    -----------
    arr : list of int
        A list of 0s and 1s representing a binary number.

    Returns:
    --------
    int
        The decimal representation of the binary number.

    Examples:
    ---------
    >>> binary_array_to_number([0,0,0,1])
    1
    >>> binary_array_to_number([1,0,1,1])
    11
    """
    binary_str = ''.join(str(bit) for bit in arr)  # Convert list to string
    return int(binary_str, 2)  # Convert binary string to decimal
# Example usage:
print(binary_array_to_number([0,0,0,1]))  # Output: 1
print(binary_array_to_number([1,0,1,1]))  # Output: 11  