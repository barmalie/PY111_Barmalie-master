from typing import List
from random import randint


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort
    Сортировка миграцией

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    # numbers = 51# терминальное значение
    # container = [] #пустой список
    # for i in range(numbers): #итерация в диапазоне 31
    #     container.append(randint(-101, 101)) #добавление в пустой список чисел от минус ста до ста
    #
    # for i in range(numbers-1):
    #     for j in range(numbers-i-1):
    #         if container[j] > container[j + 1]:
    #             container[j], container[j + 1] = container[j + 1], container[j]
    #
    # #return container
    #             print(container)
    for _ in range(len(container)):
        for i in range(len(container)-1):
            if container[i] > container[i+1]:
                container[i],container[i+1] = container[i +1],container[i]
    return container