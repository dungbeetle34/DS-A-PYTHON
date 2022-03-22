# 10 --> 5 --> 16
# 1 --> 10 --> 5 --> 16

class SinglyLinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return f"LinkedList -->\n\thead: [ 'value': {self.head['value']}, 'next': {self.head['next']} ],\n\ttail: [ 'value': {self.tail['value']}, 'next': {self.tail['next']} ],\n\tlength: {self.length}"

    def append(self, value):
        newNode = {
            'value': value,
            'next': None
        }
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = {
            'value': value,
            'next': self.head
        }

        self.head = newNode
        self.length += 1

    def insert(self,index, value):
        newNode = {
            'value': value,
            'next': None
        }
        if index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        counter = 0
        currentNode = self.head
        while counter != index-1:
            currentNode = currentNode['next']
            counter += 1
        temp = currentNode['next']
        currentNode['next'] = newNode
        newNode['next'] = temp
        self.length += 1

    def remove(self, index):
        if index >= self.length:
            return 'Error'
        elif index == 0:
            self.head = self.head['next']
            self.length -= 1
            return
        counter = 0
        currentNode = self.head
        while counter != index-1:
            currentNode = currentNode['next']
            counter += 1
        if index == self.length - 1:
            self.tail = currentNode
        unwantedNode = currentNode['next']
        currentNode['next'] = unwantedNode['next']
        self.length -= 1

    # 1 --> 10 --> 5 --> 16
    # 16 --> 5 --> 10 --> 1
    def reverse(self):
        if self.length == 1:
            return
        first = self.head
        second = first['next']
        while second:
            temp = second['next']
            second['next'] = first
            first = second
            second = temp
        self.head['next'] = None
        self.head = first
        
        

myLinkedList = SinglyLinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.reverse()
print(myLinkedList)


class DoublyLinkedList:
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None,
            'prev': None
        }
        self.tail = self.head
        self.length = 1

    def __repr__(self):
        return f"LinkedList -->\n\thead: [ 'value': {self.head['value']}, 'next': {self.head['next']}, 'prev': {self.head['prev']} ]\n\ttail: [ 'value': {self.tail['value']}, 'next': {self.tail['next']}, 'prev': {self.tail['prev']} ],\n\tlength: {self.length}"

    def append(self, value):
        newNode = {
            'value': value,
            'next': None,
            'prev': None
        }
        newNode['prev'] = self.tail
        self.tail['next'] = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = {
            'value': value,
            'next': self.head,
            'prev': None
        }
        self.head = newNode
        self.length += 1

    def insert(self,index, value):
        newNode = {
            'value': value,
            'next': None,
            'prev': None
        }
        if index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        counter = 0
        currentNode = self.head
        while counter != index-1:
            currentNode = currentNode['next']
            counter += 1
        temp = currentNode['next']
        currentNode['next'] = newNode
        newNode['prev'] = currentNode
        temp['prev'] = newNode
        newNode['next'] = temp
        self.length += 1

    # 1 --> 10 --> 5 --> 16
    # 1 --> 10 --> 99 --> 5 --> 16
    def remove(self, index):
        if index >= self.length:
            return 'Error'
        elif index == 0:
            self.head = self.head['next']
            self.length -= 1
            return
        counter = 0
        currentNode = self.head
        while counter != index-1:
            currentNode = currentNode['next']
            counter += 1
        if index == self.length - 1:
            self.tail = currentNode
        unwantedNode = currentNode['next']
        currentNode['next'] = unwantedNode['next']
        unwantedNode['prev'] = currentNode
        self.length -= 1

myDouble = DoublyLinkedList(10)
myDouble.prepend(1)
myDouble.insert(2, 99)
# print(myDouble)