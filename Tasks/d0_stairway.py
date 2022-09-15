from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    total_cost = {}
    def laizy_stairway_path(stair_number: int) -> Union[float,int]:

        if stair_number in total_cost:
            return total_cost[stair_number]
        if stair_number == 0:
            total_cost[stair_number] = stairway[stair_number]
            return stairway[stair_number]
        if stair_number == 1:
            total_cost[stair_number] = stairway[stair_number]
            return stairway[stair_number]

        current_cost = stairway[stair_number]
        total_cost = current_cost + min(laizy_stairway_path(stair_number-1),laizy_stairway_path(stair_number-2))
        return total_cost

    print(stairway)
    return laizy_stairway_path(stairway)
    #прямой метод
# def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
#     #stair_way цена одной ступеньки
#     count_stairs = len(stairway) # количество
#     total_cost: list[int] = [0] * count_stairs # стоимость дойти до ступеньки
#
#     # изначальные условия
#     total_cost[0] = stairway[0] # для первой ступени
#     total_cost[1] = stairway[1] # для второй ступени
#     for i in range(2, count_stairs):
#         total_cost[i] = stairway[i] + min(total_cost[i-1], total_cost[i-2])
#     return total_cost[-1]
#
#     # #прямой метод обхода: i стоимость =i цена + min((i-1)стоимость,(i-2)стоимость)


# см лекцию
# def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
#     # stair_way цена одной ступеньки
#     count_stairs = len(stairway)  # количество ok
#     total_cost: list[int] = [float("inf")] * count_stairs  # стоимость дойти до ступеньки ok
#     # изначальные условия
#     total_cost[0] = stairway[0]  # для первой ступени ok
#     total_cost[1] = stairway[1]  # для второй ступени ok
#     for i in range(0, count_stairs):
#         if i + 1 < count_stairs:
#             total_cost[i + 1] = min(total_cost[i]+stairway[i+1], total_cost[i+1])
#         if i + 2 < count_stairs:
#             total_cost[i + 2] = min(total_cost[i] + stairway[i + 2], total_cost[i + 2])
#         return total_cost[-1]
# ленивый алгоритм
# Возможное решение сортировкой
# Для рекурсии нужно знать правила
#def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:

# from functools import lru_cache
#
# @lru_cache()
# def fib_with_cache(i):
#     count_stairs = len(stairway)
#     total_cost: list[int] = [0] * count_stairs
#     # изначальные условия
#     total_cost[0] = stairway[0]
#     total_cost[1] = stairway[1]
#
#     if stairway[0] == 1:
#         return 0
#     if stairway[1] == 2:
#         return 1
#     fib_numbers = [total_cost(i) for i in count_stairs]
#     return fib_numbers + min(total_cost[i-1], total_cost[i-2])
