def count_by(x, n):
    """
    Generate a list of multiples of a given number.

    Parameters:
    x (int): The number whose multiples are to be generated.
    n (int): The number of multiples to generate.

    Returns:
    list: A list containing the first `n` multiples of `x`.

    Example:
    >>> count_by(2, 5)
    [2, 4, 6, 8, 10]
    """
    result = []

    for i in range(1, n + 1):
        result.append(x * i)

    return result


# ---- Function Execution ----
# This line runs the function and prints the output in VS Code terminal
print(count_by(2, 5))

