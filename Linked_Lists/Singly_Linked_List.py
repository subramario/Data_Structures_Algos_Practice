class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

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
        print("\n")

    def prepend(self,data):
        node = Node(data)

        if self.head == None:
            self.head = node
            return

        cur = self.head
        node.next = cur
        self.head = node

    def append(self,data):
        node = Node(data)
        
        if self.head == None:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def insert_after_value(self, value, data):
        node = Node(data)

        if value < 0:
            print("Error! Must be a positive position.")

        cur = self.head
        while cur:
            if (cur.data == value):
                node.next = cur.next
                cur.next = node
                return
            else:
                cur = cur.next

    def insert_after_position(self,position,data):
        node = Node(data)
        count = 0
        size = self.size()

        if position > size:
            print("Error! Node not added - position exceeded size of existing list.")
            return

        if position < 0:
            print("Error! Node not added - must include a positive position.")
            return

        cur = self.head
        while cur:
            if count != position:
                cur = cur.next
                count += 1
            else:
                break

        node.next = cur.next
        cur.next = node

    def delete_value(self, key):
        cur = self.head
        prev = None

        if key == self.head.data:
            cur = None
            self.head = self.head.next
            return

        while cur and cur.data != key:
            prev = cur
            cur = cur.next

        if cur is None:
            print("Error: List does not contain this value.")
            return

        prev.next = cur.next
        cur = None

    def delete_position(self,position):
        prev = None
        cur = self.head
        count = 0

        if position > self.size():
            print("Error: position cannot be greater than size of the list.")
            return

        if position < 0:
            print("Error: position cannot be a negative number.")
            return

        if position == 0:
            self.head = self.head.next
            cur = None
            return

        while count != position:
            prev = cur
            cur = cur.next
            count += 1

        prev.next = cur.next
        cur = None


    def reverse(self):
        prev = None
        cur = self.head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        self.head = prev

        
sl_list = SLL()
sl_list.append(1)
sl_list.append(2)
sl_list.append(3)
sl_list.print()
print("Old head was: " + str(sl_list.head.data))
sl_list.reverse()
sl_list.print()
print("New head is: " + str(sl_list.head.data))


