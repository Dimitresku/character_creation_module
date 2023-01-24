"""Imports the square root function."""
from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number):
    """Calculate the square root."""
    return sqrt(number)


def calc(your_number):
    """Calculate the square root."""
    if your_number <= 0:
        print(0)
    result = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {result}')


print(message)
calc(25.5)
