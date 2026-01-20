def century(year):
    """
    Determine the century of a given year.

    A century spans 100 years:
    - 1st century: years 1 to 100
    - 2nd century: years 101 to 200
    - and so on.

    This function calculates the correct century using
    strict construction, meaning years ending in 00
    belong to the previous century.

    Parameters:
    year (int): A positive integer representing the year.

    Returns:
    int: The century in which the given year falls.
    """
    return (year - 1) // 100 + 1
print(century(1705))  # 18
print(century(1900))  # 19
print(century(2000))  # 20
