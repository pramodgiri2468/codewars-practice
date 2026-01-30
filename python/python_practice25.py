def get_age(age):
    """
    Extracts and returns the girl's age as an integer from a given string.

    The input string always starts with a single-digit number (0–9),
    representing the age, followed by descriptive text such as
    "year old" or "years old".

    Parameters:
    age (str): A string containing the age information.
               Example: "5 years old", "1 year old"

    Returns:
    int: The age extracted from the string.

    Example:
    >>> get_age("5 years old")
    5
    >>> get_age("1 year old")
    1
    """
    return int(age[0])
# Example usage:
print(get_age("5 years old"))  # Output: 5
print(get_age("1 year old"))   # Output: 1