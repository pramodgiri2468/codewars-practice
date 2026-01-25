def remove_smallest(numbers):
    """
    Remove the smallest number from a list without mutating the original list.

    This function takes a list of integers and returns a new list
    with the first occurrence of the smallest number removed.
    The order of the remaining elements is preserved. If the input
    list is empty, it returns an empty list.

    Parameters:
    numbers (list of int): A list of integers representing exhibit ratings.

    Returns:
    list of int: A new list with the first occurrence of the smallest
                 number removed. Original list remains unchanged.

    Examples:
    remove_smallest([1, 2, 3, 4, 5])
    -> [2, 3, 4, 5]

    remove_smallest([5, 3, 2, 1, 4])
    -> [5, 3, 2, 4]

    remove_smallest([2, 2, 1, 2, 1])
    -> [2, 2, 2, 1]

    remove_smallest([])
    -> []
    """

    if not numbers:
        return []

    result = numbers.copy()
    result.remove(min(result))
    return result
# Example usage:        
print(remove_smallest([1, 2, 3, 4, 5]))  # Output: [2, 3, 4, 5]
print(remove_smallest([5, 3, 2, 1, 4]))  # Output: [5, 3, 2, 4]
print(remove_smallest([2, 2, 1, 2, 1]))  # Output: [2, 2, 2, 1]
print(remove_smallest([]))  # Output: []