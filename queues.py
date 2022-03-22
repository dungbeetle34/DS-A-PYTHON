class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.first

    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        print(self.last.value)

    def dequeue(self):
        if self.isEmpty():
            return self
        elif self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
        self.length -= 1

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

# queue = Queue()

# queue.enqueue('Joy')
# queue.enqueue('Matt')
# queue.enqueue('Pavel')
# queue.enqueue('Samir')

# queue.dequeue()
# print(queue.length)
# queue.dequeue()
# print(queue.length)
# queue.dequeue()
# print(queue.length)
# queue.dequeue()
# print(queue.length)
