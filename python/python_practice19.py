def string_to_array(s):
    """
    Convert a string into a list of words.

    This function splits the input string into a list using a single
    space character as the separator. It preserves empty strings when
    the input is an empty string, ensuring compatibility with edge
    cases such as Codewars test requirements.

    Parameters:
    s (str): The input string containing words separated by spaces.
             The string may also be empty.

    Returns:
    list: A list of words (strings) obtained by splitting the input
          string on spaces.

    Examples:
    string_to_array("Robin Singh")
    -> ["Robin", "Singh"]

    string_to_array("I love arrays they are my favorite")
    -> ["I", "love", "arrays", "they", "are", "my", "favorite"]

    string_to_array("")
    -> [""]
    """

    return s.split(" ")
# Example usage:
print(string_to_array("Robin Singh"))  # Output: ["Robin", "Singh"]
print(string_to_array("I love arrays they are my favorite"))  # Output: ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(string_to_array(""))  # Output: [""]