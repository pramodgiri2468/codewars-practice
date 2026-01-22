def reverse_words(text):
    """
    Reverse each word in a given string while preserving all spaces.

    This function takes a string as input and reverses the characters
    of each individual word. The order and number of spaces in the
    original string are kept exactly the same.

    Parameters:
    text (str): A string containing words separated by spaces.
                The string may contain multiple consecutive spaces.

    Returns:
    str: A new string where each word is reversed, but all spaces
         remain in their original positions.

    Examples:
    reverse_words("This is an example!")
    -> "sihT si na !elpmaxe"

    reverse_words("double  spaces")
    -> "elbuod  secaps"
    """

    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# Example usage:
print(reverse_words("This is an example!"))  # Output: "sihT si na !elpmaxe"
print(reverse_words("double  spaces"))        # Output: "el