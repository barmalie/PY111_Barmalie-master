# from typing import List
from random import randint
#
#def sort(container: List[int]) -> List[int]:
#     """
#     Sort input container with quick sort
#
#     :param container: container of elements to be sorted
#     :return: container sorted in ascending order
#     """
#     list  = []
#     base_element = len(container) //2
#     left_side = 0
#     right_side = len(container)
#     if left_side > 0:
#         for i in left_side:
#             list.append(left_side)
#
#     if right_side > 0:
#         for i in right_side:
#             list.append(right_side)
#
#     return container

def sort(container):
    def _sort(left_border, right_border):
        if left_border >= right_border:
            return
        random_index = randint(left_border, right_border)
        pivot = container[random_index]
        # идем двумя счетчиками
        i, j = left_border, right_border
        while i <= j:
            while container[i] < pivot:
                i += 1# увеличиваем левый счетчик , пока он не встретит элемент бодише или равный опорному
            while container[j] > pivot:
                j -= 1#  уменьшаем правый счетчик , пока он не встретит элемент который меньше или равен опорному

            if i <= j: # если границы пересеклись , в таком случае мы меняем элементы
                container[i], container[j] = container[j], container[i]
                i += 1
                j -= 1
            _sort(left_border, j)
            _sort(i, right_border)
        _sort(0,len(container)-1)

        return container



unsorted = [33, 2, 3, 45, 6, 54, 33]

# ## Однострочник. Мы создадим функцию q, которая реализует алгоритм быстрой сортировки в одной строке кода Python и сортирует любой аргумент, переданный в нее в виде списка целых чисел
#
# #мы создаем новую лямбда-функцию q, при- нимающую в качестве аргумента список l, который нужно отсортировать. В укрупненном виде структура этой лямбда-функции выглядит следующим образом:
#lambda l: q(левый) + опорный_элемент + q(правый) if l else []
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []#При граничном случае рекурсии — когда список пуст и, следовательно, сортируется тривиальным образом — лямбда-функция возвращает пустой список [].
print(q(unsorted))
#
# #Во всех прочих случаях функция берет в качестве первого элемента списка l опорный_элемент и делит все элементы на два подсписка (левый и пра- вый), в зависимости от того, меньше или больше они, чем опорный_элемент.
#
#
# ### Результат
# print(q(unsorted))
# # [2, 3, 6, 33, 33, 45, 54]

def sort(container):

     if not container:
         return container
     pivot = choice(container)
     return sort([v for v in container if v < pivot]) + [v for v in container if v == pivot] + sort[v for v in container if v > pivot])
    # def _sort(left_border, right_border):
    #     if left_border >= right_border:
    #         return
    #     random_index = randint(left_border,right_border)
    #     pivot = container