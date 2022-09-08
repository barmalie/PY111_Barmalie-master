"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priority_queue = [] # todo для очереди можно использовать python dict

    def enqueue(self, ind: int, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.enqueue_item = {
            "elem": elem,
            "priority": priority
        }
        if not self.priority_queue:
            self.priority_queue.append(self.enqueue_item)
            return None
        for index, self.current_item in enumerate(self.priority_queue):
            if self.enqueue_item["priority"] >= self.current_item["priority"]:
                self.priority_queue.insert(index,self.enqueue_item)
                break
        else:
            self.priority_queue.append(self.enqueue_item)


        priority.priority_queue.append(ind, elem)
        return 0

    def dequeue(self, ind: int) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.priority_queue:
            return None
        return self.priority_queue.pop("elem")

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        reversed_index = - ind-1
        return self.priority_queue[reversed_index]["elem"]

        return elem

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priority_queue.clear()
        return None
