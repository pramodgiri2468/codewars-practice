def grow(arr):
    """
    Calculate the product of all integers in a non-empty list.

    This function takes a list of integers and multiplies all
    the values together in order, returning the final result.
    The input list is guaranteed to be non-empty.

    Parameters:
    arr (list): A non-empty list of integers

    Returns:
    int: The product of all integers in the list
    """
    result = 1
    for num in arr:
        result *= num
    return result
print(grow([1, 2, 3]))  # 6
print(grow([4, 5, 6]))  # 120
print(grow([7, 8, 9, 10]))  # 504