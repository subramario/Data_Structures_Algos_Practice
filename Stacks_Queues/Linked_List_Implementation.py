class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        cur = self.head

        if self.head is None:
            print("Stack is empty.")
            return 0
        else:
            while cur:
                count += 1
                cur = cur.next
            return count

    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    def print(self):
        if self.size() == 0:
            return

        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

        print("Head is: " + str(self.head.data))
        print("The size is: " + str(self.size()) + "\n")

    def top(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur.data
        
    def push(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def pop(self):
        prev = None
        cur = self.head

        if self.head is None:
            return

        while cur.next:
            prev = cur
            cur = cur.next
        prev.next = None
        cur = None

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()
print(stack.empty())