def get_grade(s1, s2, s3):
    """
    Calculate the average of three scores and return the corresponding letter grade.

    This function takes three numerical scores, computes their average,
    and returns a letter grade based on standard grading criteria.

    Grading Scale:
    - 90 to 100 : 'A'
    - 80 to 89  : 'B'
    - 70 to 79  : 'C'
    - 60 to 69  : 'D'
    - 0 to 59   : 'F'

    Parameters:
    s1 (int or float): First score (0–100).
    s2 (int or float): Second score (0–100).
    s3 (int or float): Third score (0–100).

    Returns:
    str: A single uppercase letter representing the grade ('A', 'B', 'C', 'D', or 'F').

    Examples:
    get_grade(95, 90, 93)
    -> 'A'

    get_grade(70, 70, 70)
    -> 'C'

    get_grade(50, 60, 40)
    -> 'F'
    """

    average = (s1 + s2 + s3) / 3

    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
# Example usage:
print(get_grade(95, 90, 93))  # Output: 'A'
print(get_grade(70, 70, 70))  # Output: 'C'
print(get_grade(50, 60, 40))  # Output: 'F' 