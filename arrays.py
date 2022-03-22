class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __repr__(self):
        return 'MyArray { length: ' + str(self.length) + ', data: ' + str(self.data) + '}'
    
    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        deletedItem = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1
        return deletedItem


newArray = Array()
newArray.push('hi')
newArray.push('you')
newArray.push('!')
newArray.delete(0)
newArray.push('are')
newArray.push('nice')
newArray.delete(1)
# print(newArray)

# Create a function that reverses a string
# 'Hi my name is Eric' --> 'cirE si eman ym iH'

def reverse(str):
    if (not str or len(str) < 2):
        return 'CoMe bACk WItH A BeTtR iNpUt'
    output = ''
    for char in str[::-1]:
        output += char
    return output

# print(reverse('Hi my name is Eric'))
# print(reverse('h'))


# [0,3,4,6,30,31]

def mergeSortedArrays(l1, l2):
    if len(l1) == 0 or len(l2) == 0:
        return l1 + l2
    answer = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            answer.append(l1[i])
            i += 1
        elif l2[j] < l1[i]:
            answer.append(l2[j])
            j += 1
    return answer+l1[i:]+l2[j:]

print(mergeSortedArrays([0,3,4,31], [4,6,30]))
print(mergeSortedArrays([0], []))
print(mergeSortedArrays([], []))