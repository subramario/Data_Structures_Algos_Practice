class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next 

    def append(self, data):
        node = Node(data)
        cur = self.head
        prev = None

        if self.head == None:
            self.head = node
            return

        while cur:
            prev = cur
            cur = cur.next

        prev.next = node
        node.prev = prev
        cur = node


        
doubly = DLL()

doubly.append(1)
doubly.append(1)
doubly.append(1)

print("Head is: " + str(doubly.head.data))

doubly.print()

