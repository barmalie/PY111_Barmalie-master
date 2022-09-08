"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        self.my_queue = []  # todo для очереди можно использовать python list

    def enqueue(self, elem: Any) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.elem = my_queue.append()
        print(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if no elements.

        :return: dequeued element
        """
        if not self.my_queue:
            return None
        return self.my_queue.pop()

    def peek(self, ind: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        self.reversed_index = -ind - 1
        try:
            stack[ind]
        except IndexError:
            return None
        return self.my_stack[self.reversed_index]

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.my_stack.clear()
        return None
