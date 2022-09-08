"""
My little Stack
"""
from typing import Any

""" Осонва данных : """

class Stack:
    def __init__(self):
        self.my_stack = [] # todo для стека можно использовать python list
        self.reversed_index = 0

    def push(self, elem: Any) -> None:
        """
        Operation that add element to stack

        :param elem: element to be pushed
        :return: Nothing
        """
        self.my_stack.append(elem)

        print(elem)
        return None

    def pop(self) -> Any:
        """
        Pop element from the top of the stack. If not elements - should return None.

        :return: popped element
        """

        if not self.my_stack:
            return None
        return self.my_stack.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the stack without popping it.

        :param ind: index of element (count from the top, 0 - top, 1 - first from top, etc.)
        :return: peeked element or None if no element in this place


        """
        self.reversed_index = -ind-1
        try:
            stack[ind]
        except IndexError:
            return None
        return self.my_stack[self.reversed_index]


    def clear(self) -> None:
        """
        Clear my stack

        :return: None
        """
        self.my_stack.clear()
        return None
