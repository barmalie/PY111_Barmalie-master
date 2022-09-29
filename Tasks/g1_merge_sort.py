from typing import List
from random import randint
from operator import lt, gt


def sort(container: List[int], ascending: bool = True) -> List[int]:
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
    offset = 1# введение
    #ascending
    compare_operator = gt if ascending else lt
    for _ in range(len(container)):
        is_change = False# (модернизация)не было ни одной замены элемента, список изначально отсортирован

        for i in range(len(container)-offset):# применение вместо минус 1
            #if container[i] > container[i+1]:
            if compare_operator(container[i],container[i+1]):
                container[i], container[i+1] = container[i +1],container[i]
                is_change = True# модернизация
        if not is_change:
            break
        offset += 1#добавление при каждой итерации
    return container
if __name__ =="__main__":
    list_ = [1,24,3,41,5,67]
    sorted = sort(list_)
    print(sorted)
    print(sort(list_, ascending=False))
    print(max(list_))
    print(min(list_))
    print(reversed(sort(list_)))