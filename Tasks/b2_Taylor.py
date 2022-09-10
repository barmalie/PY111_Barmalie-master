# """
# Taylor series
# """
# from typing import Union
#
#
# def ex(x: Union[int, float]) -> float:
#     """
#     Calculate value of e^x with Taylor series
#
#     :param x: x value
#     :return: e^x value
#     """
#     print(x)
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
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

print("The factorial of 23 is : ", end="")
print(factorial(23))
# #Taylor
# import math
#
# x = 2
# e_to_2 = x**0/math.factorial(0) + x**1/math.factorial(1) + x**2/math.factorial(2) + x**3/math.factorial(3) + x**4/math.factorial(4)
# print(e_to_2)
# print(math.exp(2))