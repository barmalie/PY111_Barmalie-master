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



bs = lambda l, x, lo, hi: -1 if lo>hi else \
(lo+hi)//2 if l[(lo+hi)//2] == x else \
bs(l, x, lo, (lo+hi)//2-1) if l[(lo+hi)//2] > x else \
bs(l, x, (lo+hi)//2+1, hi)

print(bs(l, x, 0, len(l)-1))