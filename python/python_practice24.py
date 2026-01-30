def get_count(sentence):
    """
    Count the number of vowels in a given string.

    This function counts how many times the vowels
    'a', 'e', 'i', 'o', and 'u' appear in the input string.
    The input string contains only lowercase letters and spaces.
    The letter 'y' is not considered a vowel.

    Parameters:
    sentence (str): The input string to analyze.

    Returns:
    int: The total number of vowels in the string.
    """
    vowels = "aeiou"
    return sum(1 for char in sentence if char in vowels)
# Example usage:
print(get_count("hello world"))  # Output: 3
print(get_count("abracadabra"))   # Output: 5   