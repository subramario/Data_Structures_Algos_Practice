class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class Binary_Tree:
    def __init__(self,root):
        self.root = Node(root)

    "root -> left subtree -> right subtree"
    def preorder_traversal(self, start):
        if start:
            print(start.value)
            self.preorder_traversal(start.left)
            self.preorder_traversal(start.right)
            return

    "left subtree -> root -> right subtree"
    def inorder_traversal(self, start):
        if start:
            self.inorder_traversal(start.left)
            print(start.value)
            self.inorder_traversal(start.right)
            return 
    
    "left subtree -> right subtree -> root"
    def postorder_traversal(self, start):
        if start:
            self.postorder_traversal(start.left)
            self.postorder_traversal(start.right)
            print(start.value)
            return 

#               1
#           /       \
#          2          3
#         /  \      /   \
#        4    5     6    7

tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7) 

# print(tree.print_tree("inorder"))
tree.postorder_traversal(tree.root)