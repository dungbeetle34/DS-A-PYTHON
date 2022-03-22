class HashTable:
    def __init__(self):
        self.bucket = 16
        self.hashmap = [[] for i in range(self.bucket)]

    def _hash(self, key):
        return len(key) % self.bucket

    def set(self, key, value):
        address = self._hash(key)
        ref = self.hashmap[address]
        for i in range(len(ref)):
            if ref[i][0] == key:
                ref[i][1] = value
                return None
        ref.append([key, value])
        return None
    
    def get(self, key):
        address = self._hash(key)
        currentBucket = self.hashmap[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] == key:
                    return currentBucket[i][1]
        return None

    def keys(self):
        keysArray = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i]:
                for j in range(len(self.hashmap[i])):
                    if self.hashmap[i][j]:
                        keysArray.append(self.hashmap[i][j][0])
        return keysArray

    def keys2(self):
        if not self.hashmap:
            return -1
        result = []
        for i in range(len(self.hashmap)):
            if self.hashmap[i] and len(self.hashmap[i]):
                if len(self.hashmap) > 1:
                    for j in range(len(self.hashmap[i])):
                        result.append(self.hashmap[i][j][0])
                else:
                    result.append(self.hashmap[i][0])
        return result

myHashTable = HashTable()
myHashTable.set('grapes', 10000)
myHashTable.set('apples', 54)
myHashTable.set('oranges', 4)
myHashTable.set('bananas', 5)
myHashTable.set('pears', 542)
myHashTable.set('mangos', 534)
# print(myHashTable.keys())
# print(myHashTable.keys2())


# Given an array return the first recurring character
# Otherwise, return undefined

def recurringChar(list):
    dict = {}
    for index, value in enumerate(list):
        if value in dict:
            return value
        dict[value] = index
        print(dict)
    return None

print(recurringChar([2,5,1,2,3,5,1,2,4]))
print(recurringChar([2,1,1,2,3,5,1,2,4]))
print(recurringChar([2,3,4,5]))