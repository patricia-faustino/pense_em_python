import math


def distance(x1, x2, y1, y2):
    dx = calculate_difference_squared(x1, x2)
    dy = calculate_difference_squared(y1, y2)
    squared_total = dx + dy
    return math.sqrt(squared_total)


def calculate_difference_squared(x1, x2):
    return (x2 - x1) ** 2


print(distance(1, 2, 4, 6))


def hypotenuse(a, b):
    return math.sqrt(calculate_sum_squared(a, b))


def calculate_sum_squared(a, b):
    return a ** 2 + b ** 2


print(hypotenuse(3, 4))