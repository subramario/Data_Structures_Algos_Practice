class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class Binary_Tree:
    def __init__(self,root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(self.root)
        else:
            print("Traversal type \"" + str(traversal_type) + "\" is not supported.")

    "root -> left subtree -> right subtree"
    def preorder_traversal(self, start, traversal = ""):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    
        
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

print(tree.print_tree("preorder"))