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
        self.__search(self.root, data)


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
                self.__insert(parent.right)
            else:
                parent.right = Node(data)
