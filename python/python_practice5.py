def solution(string):
    """
    Reverse the given string.

    Parameters:
    string (str): The string to be reversed

    Returns:
    str: The reversed string
    """
    return string[::-1]  # slice the string from end to start
print(solution("world"))  # "dlrow"
print(solution("hello"))  # "olleh"
print(solution("Python"))  # "nohtyP"