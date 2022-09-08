"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.pr_queue = {} # todo для очереди можно использовать python dict

    def enqueue(self, ind: int, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.priority = priority

        priority.pr_queue.append(ind, elem)
        return None

    def dequeue(self, ind: int) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """

        return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.pr_queue.clear()
        return None
