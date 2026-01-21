def basic_op(operator, value1, value2):
    """
    Perform a basic mathematical operation on two numbers.

    The function supports the following operations:
    '+' : addition
    '-' : subtraction
    '*' : multiplication
    '/' : division

    Parameters:
    operator (str): A string representing the operation ('+', '-', '*', '/')
    value1 (int or float): The first number
    value2 (int or float): The second number

    Returns:
    int or float: The result after applying the chosen operation
    """
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
print(basic_op('+', 4, 7))  # 11
print(basic_op('-', 15, 18))  # -3
print(basic_op('*', 5, 5))  # 25
print(basic_op('/', 49, 7))  # 7.0