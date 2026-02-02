def open_or_senior(data):
    """
    Categorize club members as 'Senior' or 'Open' based on age and handicap.

    This function takes a list of pairs, where each pair contains a person's
    age and handicap. A person is classified as 'Senior' if:
    - Their age is 55 or older, AND
    - Their handicap is greater than 7.

    If either condition is not met, the person is classified as 'Open'.

    Parameters:
    data (list of lists or tuples): A list of pairs in the form [age, handicap],
                                   where both values are integers.

    Returns:
    list of str: A list of strings where each element is either "Senior" or "Open",
                 corresponding to each person in the input list.

    Examples:
    >>> open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]])
    ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']

    >>> open_or_senior([[55, 8], [54, 10]])
    ['Senior', 'Open']
    """

    result = []
    for age, handicap in data:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result
# Example usage:
print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
# Output: ['Open', 'Open', 'Senior', 'Open', 'Open', 'Senior']
print(open_or_senior([[55, 8], [54, 10]]))
# Output: ['Senior', 'Open']