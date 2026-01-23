def to_jaden_case(string):
    """
    Convert a sentence into Jaden Case.

    This function takes a string and capitalizes the first letter
    of every word, mimicking the writing style often used by
    Jaden Smith on social media. Contractions and punctuation
    are handled correctly, with only the first character of
    each word being capitalized.

    Parameters:
    string (str): A sentence containing words separated by spaces.

    Returns:
    str: The input string converted so that each word starts
         with a capital letter.

    Examples:
    to_jaden_case("how can mirrors be real if our eyes aren't real")
    -> "How Can Mirrors Be Real If Our Eyes Aren't Real"

    to_jaden_case("hello world")
    -> "Hello World"
    """

    return " ".join(word.capitalize() for word in string.split())
# Example usage:
print(to_jaden_case("how can mirrors be real if our eyes aren't real"))
print(to_jaden_case("hello world"))