from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    # """
    # Performs binary search of given element inside of array
    #
    # :param elem: element to be found
    # :param arr: array where element is to be found
    # :return: Index of element if it's presented in the arr, None otherwise
    # """


    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < elem:
            low = mid + 1
        elif elem < arr[mid]:
            high = mid - 1
        else:
            return mid


l = [3, 6, 14, 16, 33, 55, 56, 89]
x = 56
print(binary_search(x, l))
# 6 (индекс найденного элемента
#print(elem, arr)
    #return None
