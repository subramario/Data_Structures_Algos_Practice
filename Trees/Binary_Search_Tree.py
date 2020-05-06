class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, value, start):
        if value < start.value:
            if start.left is None:
                start.left = Node(value)
                return
            else:
                self.insert(value, start.left)

        if value > start.value:
            if start.right is None:
                start.right = Node(value)
                return
            else:
                self.insert(value, start.right)

        if value == start:
            print("Value already added to binary search tree.")
            return

    def inorder_traversal(self, start):
        if start:
            print(start.value)
            self.inorder_traversal(start.left)
            self.inorder_traversal(start.right)
            return


tree = BST(8)
tree.insert(3, tree.root)
tree.insert(10, tree.root)
tree.insert(1, tree.root)
tree.insert(6, tree.root)
tree.insert(9, tree.root)
tree.insert(11, tree.root)


tree.inorder_traversal(tree.root)