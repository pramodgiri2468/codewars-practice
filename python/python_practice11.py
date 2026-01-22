def count_sheep(n):
    """
    Count sheep from 1 up to a given number and return a formatted string.

    This function takes a non-negative integer and returns a string
    that contains a sequence of numbers followed by the text
    "sheep..." for each count.

    Parameters:
    n (int): A non-negative integer representing the number of sheep

    Returns:
    str: A string in the format "1 sheep...2 sheep...3 sheep..."
         Returns an empty string if n is 0.
    """
    result = ""
    for i in range(1, n + 1):
        result += f"{i} sheep..."
    return result
# Example usage:
print(count_sheep(3))  # Output: "1 sheep...2 sheep...3 sheep..."