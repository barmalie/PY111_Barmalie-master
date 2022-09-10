"""
This module implements some functions based on linear search algo
"""
from typing import Sequence
#
#
def min_search(arr: Sequence) -> int:

    list_num = list(enumerate(arr,0))
    min_ = min(list_num, key=lambda i:i[1])
    print(min_)
    return min_[0]
