# STACK USING LINKED LIST

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    # def __repr__(self):
    #     return f"Stack \nTop: Node (Value: {self.top})\nBottom: Node (Value: {self.bottom})"

    def peek(self):
        if self.isEmpty():
            return None
        else:
            print(self.top.value)
            return self.top.value
            
    
    def push(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer 
            print(f'top: {self.top.value}, next: {self.top.next.value}')

        self.length += 1
        return self

    def pop(self):
        if self.isEmpty():
            return None
        elif self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next
        self.length -= 1
        return self

    def isEmpty(self):
        if self.length == 0:
            return True
        return False


# stack = Stack()
# stack.peek()
# stack.push(4)
# stack.push('e')
# print(stack.length)
# stack.pop()
# print(stack.length)
# stack.pop()
# print(stack.length)

# STACK USING ARRAYS
class StackArray():
    def __init__(self):
        self.array = []

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.array[len(self.array) - 1]

    def push(self, value):
        return self.array.append(value)

    def pop(self):
        return self.array.pop()

    def isEmpty(self):
        if len(self.array) == 0:
            return True
        else:
            return False

# stack2 = StackArray()
# stack2.peek()
# stack2.push(4)
# stack2.push('e')
# print(len(stack2.array))
# stack2.pop()
# print(len(stack2.array))
# stack2.pop()
# print(len(stack2.array))