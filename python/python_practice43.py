def min_max(lst):
    """
    Determine the minimum and maximum values in a non-empty list.

    This function iterates through a list of numeric values and returns
    the smallest and largest numbers found. It performs a single pass
    through the data, making it efficient for large datasets such as
    sensor readings or time-series measurements.

    Parameters
    ----------
    lst : list of int or float
        A non-empty list containing numeric values.

    Returns
    -------
    list
        A list containing two elements:
        [minimum_value, maximum_value]

    Examples
    --------
    >>> min_max([1, 2, 3, 4, 5])
    [1, 5]

    >>> min_max([2334454, 5])
    [5, 2334454]

    >>> min_max([7])
    [7, 7]

    Notes
    -----
    - Assumes the input list contains at least one element.
    - Useful in data analysis tasks such as:
      • sensor value monitoring (temperature, moisture, pressure)
      • normalization for machine learning
      • range detection in IoT systems

    Time Complexity
    ---------------
    O(n) — The function scans the list once.

    Space Complexity
    ----------------
    O(1) — Uses constant extra memory.
    """
    minimum = lst[0]
    maximum = lst[0]

    for num in lst:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return [minimum, maximum]
# Example usage:
print(min_max([1, 2, 3, 4, 5]))  # Output: [1, 5]
print(min_max([2334454, 5]))  # Output: [5, 2334454]
print(min_max([7]))  # Output: [7, 7]