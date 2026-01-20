def get_volume_of_cuboid(length, width, height):
    """
    Calculate the volume of a rectangular cuboid.

    Parameters:
    length (float or int): The length of the cuboid
    width (float or int): The width of the cuboid
    height (float or int): The height of the cuboid

    Returns:
    float or int: The volume of the cuboid
    """
    volume = length * width * height
    return volume
print(get_volume_of_cuboid(2, 3, 4))  # 24
print(get_volume_of_cuboid(1, 5, 6))  # 30
print(get_volume_of_cuboid(0, 4, 5))  # 0
