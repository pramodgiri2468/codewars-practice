def solution(s):
    """
    Insert a space before each uppercase letter in a camelCase string.

    This function converts a camelCase formatted string into a space-separated
    string by adding a space before every uppercase character while keeping
    all characters unchanged.

    Parameters
    ----------
    s : str
        The input string written in camelCase format.

    Returns
    -------
    str
        A new string where each uppercase letter is preceded by a space.

    Examples
    --------
    >>> solution("camelCasing")
    'camel Casing'

    >>> solution("identifier")
    'identifier'

    >>> solution("")
    ''

    Notes
    -----
    - The function iterates through each character of the string.
    - If a character is uppercase, a space is inserted before it.
    - Otherwise, the character is appended normally.
    - Time Complexity: O(n)
    - Space Complexity: O(n)
    """
    result = ""
    for char in s:
        if char.isupper():
            result += " " + char
        else:
            result += char
    return result
# Example usage:
print(solution("camelCasing"))  # Output: 'camel Casing'
print(solution("identifier"))    # Output: 'identifier'
print(solution(""))              # Output: ''