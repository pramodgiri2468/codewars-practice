def remove_char(s):
    """
    Remove the first and last characters from a string.

    This function takes a string with a minimum length of two
    characters and returns a new string with the first and
    last characters removed. If the string contains exactly
    two characters, the function returns an empty string.

    Parameters:
    s (str): The input string. It will always contain
             at least two characters.

    Returns:
    str: The string with the first and last characters removed.

    Examples:
    remove_char("eloquent")
    -> "loquen"

    remove_char("country")
    -> "ountr"

    remove_char("ab")
    -> ""

    remove_char("xyz")
    -> "y"
    """

    return s[1:-1]
# Example usage:
print(remove_char("eloquent"))  # Output: "loquen"
print(remove_char("country"))    # Output: "ountr"
print(remove_char("ab"))         # Output: ""