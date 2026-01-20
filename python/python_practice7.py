def repeat_str(repeat, string):
    """
    Repeat a given string a specified number of times.

    This function takes a non-negative integer and a string,
    and returns a new string consisting of the original string
    repeated exactly 'repeat' times. If repeat is 0, an empty
    string is returned.

    Parameters:
    repeat (int): Non-negative integer specifying how many times to repeat the string
    string (str): The string to be repeated

    Returns:
    str: The string repeated 'repeat' times
    """
    return string * repeat
print(repeat_str(3, "abc"))  # "abcabcabc"
print(repeat_str(0, "test"))  # ""
print(repeat_str(2, "hello"))  # "hellohello"