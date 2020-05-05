class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None

    def empty(self):
        if self.head is None:
            return True
        else:
            return False

    def size(self):
        count = 0
        cur = self.head

        while cur:
            count += 1
            cur = cur.next

        return count

    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

        if self.empty():
            print("The queue is empty.")
        else:
            print("The head is: " + str(self.head.data))
            print("The size of the queue is: " + str(self.size()))

    def enqueue(self, data):
        node = Node(data)

        if self.empty():
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        
        cur.next = node

    def dequeue(self):
        cur = self.head
        self.head = self.head.next
        cur = None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.dequeue()
queue.print()

        

        