def is_valid_walk(walk):
    """
    Determine whether a walk is valid.

    A walk is considered valid if:
    1. It takes exactly 10 minutes (10 steps).
    2. It returns the walker to the starting point.

    Each step represents one minute and moves one block
    in one of the four cardinal directions:
    - 'n' moves north
    - 's' moves south
    - 'e' moves east
    - 'w' moves west

    Parameters:
    ----------
    walk : list of str
        A list of direction characters ('n', 's', 'e', 'w').

    Returns:
    -------
    bool
        True if the walk takes exactly 10 steps and ends at
        the starting position, otherwise False.

    Examples:
    --------
    >>> is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])
    True

    >>> is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])
    False

    >>> is_valid_walk(['n','s'])
    False
    """

    if len(walk) != 10:
        return False

    x = 0
    y = 0

    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1

    return x == 0 and y == 0
# Example usage:
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))  # Output: True
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))  # Output: False
print(is_valid_walk(['n','s']))  # Output: False