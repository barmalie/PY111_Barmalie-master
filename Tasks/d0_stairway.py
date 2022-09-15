from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)
    return reverse_stairway_path(stairway)
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
#
def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    # stair_way цена одной ступеньки
    count_stairs = len(stairway)  # количество
    total_cost: list[int] = [0] * count_stairs  # стоимость дойти до ступеньки

    # изначальные условия
    total_cost[0] = stairway[0]  # для первой ступени
    total_cost[1] = stairway[1]  # для второй ступени
    for i in range(2, count_stairs):
        if stairway[0] == 1:
            return total_cost[0]

        if stairway[1] == 2:
            return total_cost[1]

        current_stair = count_stairs  # стоимость текущей ступени

        return current_stair + min(reverse_stairway_path(i - 1), reverse_stairway_path(i - 2))

