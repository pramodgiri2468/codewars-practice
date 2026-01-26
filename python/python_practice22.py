def rental_car_cost(d):
    """
    Calculate the total cost of renting a car for a given number of days.

    Each day of rental costs $40.
    - If the car is rented for 7 or more days, a discount of $50 is applied.
    - If the car is rented for 3 to 6 days, a discount of $20 is applied.
    - No discount is applied for fewer than 3 days.

    Parameters:
    d (int): Number of days the car is rented. Must be a non-negative integer.

    Returns:
    int: The total rental cost after applying the applicable discount.
    """
    total = d * 40

    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20

    return total
# Example usage:
print(rental_car_cost(1))  # Output: 40
print(rental_car_cost(3))  # Output: 100
print(rental_car_cost(7))  # Output: 230