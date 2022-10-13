from math import inf
from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = Node(root)


    def insert(self, data):
        self.__insert(self.root, data)


    def search(self, data):
        return self.__search(self.root, data)


    def is_satisfied_bst1(self):
        output = self.__to_array(self.root)
        return self.__sorted(output)


    def __to_array(self, node: Node) -> list:

        left_array = self.__to_array(node.left) if node.left else []
        right_array = self.__to_array(node.right) if node.right else []
        
        return [*left_array, node.data, *right_array]


    def __sorted(self, array: list) -> bool:
        prev = array[0]
        for item in array[1:]:
            if item < prev:
                return False

            prev = item

        return True


    def is_satisfied_bst2(self):
        return self.__is_limited(self.root, -inf, inf)


    def __is_limited(self, node: Node, lower, upper) -> bool:
        if node is None:
            return True

        if node.data < lower or node.data > upper:
            return False

        if not self.__is_limited(node.left, lower, node.data):
            return False
        if not self.__is_limited(node.right, node.data, upper):
            return False

        return True


    def __search(self, parent: Node, data):
        if parent is None:
            return False

        if parent.data == data:
            return True

        if parent.data > data:
            return self.__search(parent.left, data)
        else:
            return self.__search(parent.right, data)


    def __insert(self, parent: Node, data):
        if parent.data > data:
            if parent.left:
                self.__insert(parent.left, data)
            else:
                parent.left = Node(data)
        else:
            if parent.right:
                self.__insert(parent.right, data)
            else:
                parent.right = Node(data)
