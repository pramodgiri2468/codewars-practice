def are_you_playing_banjo(name):
    """
    Check if a person plays banjo based on their name.

    Parameters:
    name (str): The name of the person

    Returns:
    str: "{name} plays banjo" if the name starts with 'R' or 'r'
         "{name} does not play banjo" otherwise
    """
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
print(are_you_playing_banjo("Robert"))  # "Robert plays banjo"
print(are_you_playing_banjo("Alice"))   # "Alice does not play banjo"
print(are_you_playing_banjo("rachel"))  # "rachel plays