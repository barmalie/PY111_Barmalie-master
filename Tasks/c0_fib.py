def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """



def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(1,n):
        sum_ = a + b
        a = b
        b =sum_
        return b

# from functools import reduce
# ## Данные
# n = 10
# ## Однострочник
# fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n - 2), [0, 1])
# ## Результат
# print(fibs)

