def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    rows = shape[0]
    cols = shape[0]
    def get_step(i,j):
        if i == 0 and j == 0: #первый угол.  попали в начальную точку
            return 1
        if not 0 <= i < rows: #первый угол
            return 0
        if not 0 <= i < cols: # выпали за строки
            return 0
        return 1


    return

if __name__ == "__main__":
    assert 2 == calculate_paths()
    assert 2 == calculate_paths()
