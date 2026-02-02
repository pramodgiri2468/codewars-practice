def find_needle(haystack):
    """
    Locate the position of the string "needle" in a list.

    This function searches through a list containing various elements
    (junk items) and finds the index of the element "needle".
    It then returns a formatted message indicating the position
    where the needle was found.

    Parameters:
    haystack (list): A list containing various elements, including
                     exactly one occurrence of the string "needle".

    Returns:
    str: A message stating the position of the needle in the format:
         "found the needle at position X".

    Examples:
    >>> find_needle(["hay", "junk", "hay", "needle"])
    'found the needle at position 3'

    >>> find_needle(["needle"])
    'found the needle at position 0'
    """

    index = haystack.index("needle")
    return f"found the needle at position {index}"
# Example usage:
print(find_needle(["hay", "junk", "hay", "needle"]))  # Output: 'found the needle at position 3'
print(find_needle(["needle"]))  # Output