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

    def empty(self):
        if self.head == None:
            return True
        else:
            return False


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

    def pop_front(self):
        return self.head.data
    
    def pop_back(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur.data

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

    def swap(self, first, second):
        prev_1 = None
        key_1 = self.head
        while key_1 and key_1.data != first:
            prev_1 = key_1
            key_1 = key_1.next

        prev_2 = None
        key_2 = self.head
        while key_2 and key_2.data != second:
            prev_2 = key_2
            key_2 = key_2.next

        if not key_1 and not key_2:
            print("Error: Both keys do not exist in this list.")
            return

        if not key_1:
            print("Error: Key_1 does not exist in this list.")
            return

        if not key_2:
            print("Error: Key_2 does not exist in this list.")
            return

        if prev_1:
            prev_1.next = key_2
        else:
            self.head = key_2

        if prev_2:
            prev_2.next = key_1
        else:
            self.head = key_1

        key_1.next, key_2.next = key_2.next, key_1.next


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
print(sl_list.pop_front())
print(sl_list.pop_back())
# print("Old head was: " + str(sl_list.head.data))
# print("New head is: " + str(sl_list.head.data))


