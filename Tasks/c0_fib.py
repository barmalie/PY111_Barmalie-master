def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(1,n):
        # a = b
        # sum_ = a + b
        # b =sum_
        a, b = b, a+b
        return b
    def generator_fib(n):
        if n<0:
            raise  ValueError
            a = 0
            yield a

            b = 1
            yield b
        for _ in range(1,n):
            a,b = b ,a +b
        yield b
        N =10
        #list_fin_iterative =[fib_iterative(i) for i in range(N)]
        list_fin_iterative =[]
        for i in range(N):
            current_number = fib_iterative(i)
            list_fin_iterative.append(current_number) #O(n^2)
        list_generator = [num for num in generator_fib(N-1)]
        generator = generator_fib(N-1)
        for _ in range(N):
            current_number = next(generator) #O(N)

# from functools import reduce
# ## Данные
# n = 10
# ## Однострочник
# fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n - 2), [0, 1])
# ## Результат
# print(fibs)

