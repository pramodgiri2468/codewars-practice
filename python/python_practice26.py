def printer_error(s):
    """
    Calculate the printer error rate for a control string.

    The printer is expected to use only colors represented by
    the letters from 'a' to 'm'. Any character outside this range
    is considered an error.

    The function returns the error rate as a string in the format
    "errors/total_length", without reducing the fraction.

    Parameters:
    s (str): A control string consisting of lowercase letters (a–z).

    Returns:
    str: A string representing the error rate in the format
         "number_of_errors/length_of_string".

    Examples:
    >>> printer_error("aaabbbbhaijjjm")
    '0/14'

    >>> printer_error("aaaxbbbbyyhwawiwjjjwwm")
    '8/22'
    """

    errors = 0
    for char in s:
        if char < 'a' or char > 'm':
            errors += 1
    return f"{errors}/{len(s)}"
# Example usage:
print(printer_error("aaabbbbhaijjjm"))  # Output: '0/14'
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))  # Output: '8/22'