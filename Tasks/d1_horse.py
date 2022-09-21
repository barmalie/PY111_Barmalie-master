# def calculate_paths(shape: (int, int), point: (int, int)) -> int:
#     """
#     Given field with size rows*cols count available paths from (0, 0) to point
#
#     :param shape: tuple of rows and cols (each from 1 to rows/cols)
#     :param point: desired point for horse
#     :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
#     """
#     dx = abc(x1, x2)
#     dy = abc(y1, y2)
#     if dx == 0 or dy == 0:
#         score += 1
#     delta = abs(dx - dy)
#
#     if delta == 1 and score == 0:
#         print("yes")
#     else:
#         print("no")
#
#     print(shape, point)
#     return 0

def step_1(n, m):
    # n = int(input("Введите x координату :"))
    # m = int(input("Введите y координату :"))
    start_point_x = n + 1
    start_point_y = m + 1

    next_point_x = start_point_x + 1 or start_point_x + 2
    next_point_y = start_point_y + 2 or start_point_y + 1
    if next_point_x == 2:
        next_point_y = 3
        print('{}, {}'.format(next_point_x, next_point_y))
    elif next_point_x == 3:
        next_point_y = 2
        print('{}, {}'.format(next_point_x, next_point_y))


s = step_1(0,0)
print(s)