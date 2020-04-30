class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def empty(self):
        if not self.stack:
            return True
        else:
            return False

    def print(self):
        for i in self.stack:
            print(i)
        print("The size of the stack is: " + str(self.size()))

    def top(self):
        print(self.stack[-1])

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            self.stack.pop()
        else:
            return

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.empty())
