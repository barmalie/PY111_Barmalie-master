"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""
# node = {
#     "key":
#     "value":
#     "left":
#     "rigth":
# }
#
# root = {
#     "key": 8,
#
#     "left": None {"key": 8,
#                     "value": 3,
#                     "left": None,
#                     "rigth": None,
#                    }
#     "rigth": None,
# }
from typing import Any, Optional, Tuple
# import networkx as nx


class BinarySearchTree:
    @staticmethod
    def _create_node(key: Any, value: Any, left: Optional[dict], right: Optional[dict],):
        return {"key": key,
               "value": value,
                "left": left,
                "right": right,
                }
    def __init__(self):
        self.root:Optional[dict]=None
    def insert(self, key: int, value: Any) -> None:
        if self.root is None:
            self.root = self._create_node(key,value)
        else:
            current_node = self.root
            while True:
                current_key = current_node["key"]
                if key > current_key: # уходим в правое полудерево
                    right_node = current_node["right"]
                    if right_node is None:
                        current_node["right"] = self._create_node(key, value)
                        break
                    current_node = current_node["right"]
                else:
                    left_node = current_node["left"]
                    if left_node is None:
                        current_node["left"] = self._create_node(key, value)


        return None

        """
        Insert (key, value) pair to binary search tree

        :param key: key from pair (key is used for positioning node in the tree)
        :param value: value associated with key
        :return: None
        """
        print(key, value)
        return None

    def remove(self, key: int) -> Optional[Tuple[int, Any]]:
        """
        Remove key and associated value from the BST if exists

        :param key: key to be removed
        :return: deleted (key, value) pair or None
        """
        print(key)
        return None

    def find(self, key: int) -> Optional[Any]:
        """
        Find value by given key in the BST

        :param key: key for search in the BST
        :return: value associated with the corresponding key
        """
        print(key)
        return None

    def clear(self) -> None:
        """
        Clear the tree

        :return: None
        """
        return None
