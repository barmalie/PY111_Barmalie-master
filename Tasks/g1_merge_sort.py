from typing import List
from random import randint
from operator import lt, gt


# def sort(container: List[int], ascending: bool = True) -> List[int]:
#     """
#     Sort input container with merge sort
#     Сортировка миграцией
#
#     :param container: container of elements to be sorted
#     :return: container sorted in ascending order
#     """
#     # numbers = 51# терминальное значение
#     # container = [] #пустой список
#     # for i in range(numbers): #итерация в диапазоне 31
#     #     container.append(randint(-101, 101)) #добавление в пустой список чисел от минус ста до ста
#     #
#     # for i in range(numbers-1):
#     #     for j in range(numbers-i-1):
#     #         if container[j] > container[j + 1]:
#     #             container[j], container[j + 1] = container[j + 1], container[j]
#     #
#     # #return container
#     #             print(container)
#     offset = 1# введение
#     #ascending
#     compare_operator = gt if ascending else lt
#     for _ in range(len(container)):
#         is_change = False# (модернизация)не было ни одной замены элемента, список изначально отсортирован
#
#         for i in range(len(container)-offset):# применение вместо минус 1
#             #if container[i] > container[i+1]:
#             if compare_operator(container[i],container[i+1]):
#                 container[i], container[i+1] = container[i +1],container[i]
#                 is_change = True# модернизация
#         if not is_change:
#             break
#         offset += 1#добавление при каждой итерации
#     return container
# if __name__ =="__main__":
#     list_ = [1,24,3,41,5,67]
#     sorted = sort(list_)
#     print(sorted)
#     print(sort(list_, ascending=False))
#     print(max(list_))
#     print(min(list_))
#     print(reversed(sort(list_)))

# def merge(left, right):
#     right_index, left_index = 0, 0
#     list = []
#     while len(right_index) < len(right) and len(left_index) < len(right):
#         if left_index(left) < right_index(right):
#             list.append(right_index)
#             left_index += 1
#         else:
#             list.append(right[right_index])
#             right_index += 1
#
#     list += left[left_index:]
#     list += right[right_index:]
#     return list
#
#
#
# def merge_sort(array):
#     if len(array) <= 1:# базовый случай
#         return array
#     half = len(array) // 2
#     left = merge_sort(array[:half])
#     right = merge_sort(array[half:])
#
#     return merge_sort(left, right)

def merge_function(sorted_left, sorted_right):
    sorted_result = []
    current_left_index = 0
    current_right_index = 0
    while True:
        current_left_value = sorted_left(current_left_index)
        current_right_value = sorted_right(current_right_index)
        if current_left_value < current_right_value:
            # берем значение левой части
            # в итоговый массив записываем наименьшее
            sorted_result.append(current_left_value)
            current_left_index += 1
        else: # берем значение из правой части
            sorted_result.append(current_right_value)
            current_right_index += 1
            # прописываем алгоритм для заброски в массив последнего числа
        if current_right_index == len(sorted_left):
            sorted_result.extend(sorted_right[current_right_index:])
            break

        elif current_right_index == len(sorted_right):
            sorted_result.extend(sorted_left[current_right_index:])
            # sorted_result = sorted_result + sorted_right
            break

    return  sorted_result

def sort(container):
    # терминальный случай
    if len(container) == 1:
        return container
    middle_index = len(container)//2
    left_part = sort(container[:middle_index])
    right_part = sort(container[middle_index:])
    # обход в глубину
    # в данной функции сделали разбиение
    return merge_func(left_part, right_part)