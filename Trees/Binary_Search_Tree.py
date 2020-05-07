class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

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

class BST:
    def __init__(self, root):
        self.root = Node(root)

    def get_min(self,start):
        if start.left is None:
            print(start.value)
            return
        else:
            self.get_min(start.left)

    def get_max(self,start):
        if start.right is None:
            print(start.value)
            return
        else:
            self.get_max(start.right)

    def size(self, start):
        if start is None:
            return 0

        left_branch = self.size(start.left)
        right_branch = self.size(start.right)
        return (1 + left_branch + right_branch)

    def height(self, start):
        if start is None:
            return -1

        left_height = self.height(start.left)
        right_height = self.height(start.right)
        return 1 + max(left_height,right_height)

    def print_ascending(self, start):
        self.inorder_traversal(start)

    def preorder_traversal(self,start):
        if start:
            print(start.value)
            self.preorder_traversal(start.left)
            self.preorder_traversal(start.right)
            return

    def inorder_traversal(self, start):
        if self.root is None:
            print("Tree is empty.")

        if start:
            self.inorder_traversal(start.left)
            print(start.value)
            self.inorder_traversal(start.right)
            return
        
    def postorder_traversal(self, start):
        if start:
            self.postorder_traversal(start.left)
            self.postorder_traversal(start.right)
            print(start.value)
            return

    def insert(self, value, start):
        if value < start.value:
            if start.left is None:
                start.left = Node(value)
                return
            else:
                self.insert(value, start.left)

        elif value > start.value:
            if start.right is None:
                start.right = Node(value)
                return
            else:
                self.insert(value, start.right)
        else:
            print("Value already added to binary search tree.")
            return

    def delete_value(self, value, start):
        if start is None:
            print("Value not found in this list - cannot delete.")
            return

        if value > start.value:
            self.delete_value(value, start.right)

        if value < start.value:
            self.delete_value(value, start.left)

        if value == start.value:
            start.value = None

    def delete_tree(self, start):
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
            stack.push(parent)
        
        while not stack.empty():
            node = stack.pop()
            node.left = None
            node.right = None
            node = None

        self.root = None
        
        
    def find(self, value, start):
        if start is None:
            print(str(value) + " is not in this tree.")
            return False

        if start.value == value:
            print(str(value) + " is in this tree.")
            return True
        
        if value > start.value:
            self.find(value, start.right)

        if value < start.value:
            self.find(value, start.left)


tree = BST(8)
tree.insert(3, tree.root)
tree.insert(10, tree.root)
tree.insert(1, tree.root)
tree.insert(6, tree.root)
tree.insert(9, tree.root)
tree.insert(11, tree.root)

tree.inorder_traversal(tree.root)