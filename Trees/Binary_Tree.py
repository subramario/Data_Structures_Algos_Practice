class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.insert(0,value)

    def dequeue(self):
        return self.items.pop()

    def peak(self):
        return self.items[-1].value

    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

class Stack:
    def __init__(self):
        self.items = []

    def push(self,value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


class Binary_Tree:
    def __init__(self,root):
        self.root = Node(root)

    # DEPTH FIRST SEARCH (DFS) METHODS!
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
   
    def levelorder_traversal(self, start):
        """
        BREADTH-FIRST-SEARCH (BFS)
        1) Enqueue root element 
        2) Use while loop on queue to repeat following procedure until queue is empty
        3) Peak element in queue and add to traversal
        4) Dequeue element, access left and right children, then enqueue children (left then right)
        5) Repeat
        """
        queue = Queue()
        if start is None:
            return

        queue.enqueue(start)
        while not queue.empty():
            print(queue.peak())
            parent = queue.dequeue()
            if parent.left:
                queue.enqueue(parent.left)
            if parent.right:
                queue.enqueue(parent.right)

    def reverse_levelorder_traversal(self, start):
        """
        REVERSE BREADTH-FIRST-SEARCH (RBFS)
        1) Enqueue root element 
        2) Use while loop on queue to repeat following procedure until queue is empty
        3) Dequeue element, access left and right children, then enqueue children (right then left)
        4) Add parent node to stack
        5) Once queue is empty, pop off the stack to produce traversal
        """
        queue = Queue()
        stack = Stack()

        queue.enqueue(start)
        while not queue.empty():
            parent = queue.dequeue()
            if parent.right:
                queue.enqueue(parent.right)
            if parent.left:
                queue.enqueue(parent.left)
            stack.push(parent.value)
        
        while not stack.empty():
            print(stack.pop())
    
    def height(self, node):
        """
        Basic idea: Recursively call this function to find height of children!
        1) Find max height between left branch and right branch 
        2) Add 1 to max branch height to calculate height of current node
        """
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0

        size_left = self.size(node.left)
        size_right = self.size(node.right)
        
        return (size_left + size_right + 1)

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

print(tree.size(tree.root))