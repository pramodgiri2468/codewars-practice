def find_average(numbers):
    """
    Calculate the average (mean) of a list of numbers.

    This function takes a list of numerical values and returns their average.
    If the list is empty, the function returns 0 to avoid division by zero.

    Parameters:
    numbers (list): A list of integers or floating-point numbers.

    Returns:
    float: The average of the numbers in the list.
           Returns 0 if the list is empty.
    """
    
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)
# Example usage:
print(find_average([1, 2, 3, 4, 5]))  # Output: 3.0
print(find_average([]))               # Output: 0