# """
# Taylor series
# """
# from typing import Union
#
# #
# def ex(x: Union[int, float]) -> float:
# #     """
# #     Calculate value of e^x with Taylor series
# #
# #     :param x: x value
# #     :return: e^x value
# #     """
#     x = 2
#     factorial = lambda n: n * factorial(n-1) if n > 1 else 1
#     e**x = x**0/factorial(0) + x**1/factorial(1) + x**2/factorial(2) + x**3/factorial(3) + x**4/factorial(4)
#     print(x)
#     print(e**x)

#     return 0
#
#
# def sinx(x: Union[int, float]) -> float:
#     """
#     Calculate sin(x) with Taylor series
#
#     :param x: x value
#     :return: sin(x) value
#     """
#     print(x)
#     return 0
#
# # factorial
# n = 23
# def factorial(*n):
#     fact = 1
#     #n = 23
#     for i in range(1, n + 1):
#         fact = fact * i
#     return fact
# print("The factorial of 23 is : ", end="")
# factorial(22)
# #Taylor
# import math
#
# x = 2
# e_to_2 = x**0/math.factorial(0) + x**1/math.factorial(1) + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4)
# print(e_to_2)
# print(math.exp(2))

## Результат
#factorial =(round(factorial(5.4),4))
# print(factorial(5))
# x = 2
#
# print(e_to_2)

from itertools import count
import math
EPSELON =0.001
def get_item(x,n):
    return x**n/math.factorial(n)
def get_sin(x,n):
    return ((-1)**n)*(x**(2*n+1))/math.factorial(2*n)+1
def ex(x):
    sum_=1
    for n count(1,1): #бессконечная прогрессия
        current_item = get_item_n(x,n)
        sum += current_item
        if current_item <= EPSELON
            return sum_
        return sum
def sinx(x):
    for n in count(0,1):# минус единица в степени ноль
        concurrent_item = get_sin(x,n)
        print(concurrent_item)
        sum_ += concurrent_item
        if abs(concurrent_item <= EPSELON):
            break

    print(x)
    return sum_



