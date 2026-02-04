def expanded_form(num):
    """
    Converts a number into its expanded form as a string.

    Parameters:
    -----------
    num : int
        A whole number greater than 0.

    Returns:
    --------
    str
        Expanded form of the number.

    Examples:
    ---------
    >>> expanded_form(12)
    '10 + 2'
    >>> expanded_form(70304)
    '70000 + 300 + 4'
    """
    
    num_str = str(num)
    parts = []
    
    for i, digit in enumerate(num_str):
        if digit != '0':
            parts.append(digit + '0' * (len(num_str) - i - 1))
    
    return ' + '.join(parts)
# Example usage:
print(expanded_form(12))      # Output: '10 + 2'
print(expanded_form(70304))   # Output: '70000 + 300 +