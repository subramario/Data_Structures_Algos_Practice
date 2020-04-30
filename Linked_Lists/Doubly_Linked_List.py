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

    def size(self):
        cur = self.head
        count = 0

        while cur:
            count += 1
            cur = cur.next

        return count

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

    def prepend(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_after_value(self, value, data):
        node = Node(data)
        cur = self.head
        after = self.head.next

        if value == self.head:
            node.next = after
            after.prev = node
            cur.next = node
            node.prev = cur
            self.head = node
            return

        while cur and cur.data != value:
            after = after.next
            cur = cur.next

        if not cur:
            print("Error: Value does not exist in this list - new node not added")
            return

        if after == None:
            cur.next = node
            node.prev = cur
            return

        cur.next = node
        node.prev = cur
        after.prev = node
        node.next = after

    def insert_after_position(self,position,data):
        node = Node(data)
        count = 0
        
        cur = self.head
        after = self.head.next

        if position < 0:
            print("Error: Position must be a positive number.")
            return

        if position > self.size():
            print("Error: Position exceedes the maximum size of the list.")
            return

        if position == self.size():
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur
            return

        while cur and count != position:
            count += 1
            cur = cur.next
            after = after.next

        node.next = after
        after.prev = node
        node.prev = cur
        cur.next = node

    def delete_value(self,value):
        prev = None
        cur = self.head
        after = self.head.next

        if value == self.head.data:
            after.prev = None
            cur = None
            self.head = after
            return

        while cur and cur.data != value:
            prev = cur
            cur = cur.next
            after = after.next

        if after is None:
            prev.next = None
            cur.prev = None
            cur = None
            return

        prev.next = after
        after.prev = prev
        cur = None

    def delete_position(self,position):
        prev = None
        cur = self.head
        after = self.head.next
        count = 0

        if position < 0:
            print("Error: Posiiton must be a positive value.")
            return

        if position > self.size():
            print("Error:Position must be within the maximum size of the list.")
            return

        if position == 0:
            cur.next = None
            cur = None
            after.prev = None
            self.head = after
            return

        while cur and count != position:
            count += 1
            prev = cur
            cur = cur.next
            after = after.next

        if not after:
            prev.next = None
            cur.next = None
            cur.prev = None
            cur = None
            return

        prev.next = after
        after.prev = prev
        cur = None

    def swap(self, key_1, key_2):

        prev_1 = None
        cur_1 = self.head
        after_1 = self.head.next
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next
            after_1 = after_1.next

        prev_2 = None
        cur_2 = self.head
        after_2 = self.head.next
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next
            after_2 = after_2.next

        if after_1:
            after_1.prev = cur_2
        else:
            pass

        if after_2:
            after_2.prev = cur_1
        else:
            pass

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2
        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next
        cur_1.prev, cur_2.prev = prev_2, prev_1


doubly = DLL()

doubly.append(1)
doubly.append(2)
doubly.append(3)
doubly.append(4)
print("Before swap:")
doubly.print()
print("Head is: " + str(doubly.head.data))
doubly.swap(1,4)
print("After swap:")
doubly.print()
print("Head is: " + str(doubly.head.data))

