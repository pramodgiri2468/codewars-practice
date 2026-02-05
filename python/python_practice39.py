def update_light(current):
    """
    Determine the next state of a traffic light.

    This function takes the current color of a traffic light and
    returns the color it should change to following the standard
    traffic light sequence:
    green → yellow → red → green.

    Parameters:
    ----------
    current : str
        The current state of the traffic light.
        Expected values are "green", "yellow", or "red".

    Returns:
    -------
    str
        The next state of the traffic light.

    Examples:
    --------
    >>> update_light("green")
    'yellow'

    >>> update_light("yellow")
    'red'

    >>> update_light("red")
    'green'
    """

    lights = {
        "green": "yellow",
        "yellow": "red",
        "red": "green"
    }
    return lights[current]
# Example usage:
print(update_light("green"))  # Output: 'yellow'
print(update_light("yellow"))  # Output: 'red'
print(update_light("red"))  # Output: 'green'