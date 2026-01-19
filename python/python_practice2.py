def sum_array(numbers):
    """
    Calculate the sum of all numbers in a list.

    This function takes a list of numbers (integers or floats),
    including negative values, and returns their total sum.
    If the list is empty, the function returns 0.

    Parameters:
    numbers (list): A list of numeric values (int or float).

    Returns:
    float or int: The sum of all numbers in the list.
    """

    total = 0
    for num in numbers:
        total += num
    return total
# Function calls
print(sum_array([1, 5.2, 4, 0, -1]))
print(sum_array([]))
print(sum_array([-2.398]))