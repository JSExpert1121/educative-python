from binary_search_tree import BST, Node
from datetime import datetime

def run():
    input_data = [10, 3, 1, 25, 9, 13]
    tree = BST(input_data[0])

    for item in input_data[1:]:
        tree.insert(item)

    tree.root.left.right.right = Node(11)
    print(tree.search(9))
    print(tree.search(14))

    start = datetime.now()
    print(tree.is_satisfied_bst1())
    print(datetime.now() - start)

    start = datetime.now()
    print(tree.is_satisfied_bst2())
    print(datetime.now() - start)


if __name__ == '__main__':
    run()
