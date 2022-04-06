# from turtle import left
import json
from multiprocessing.dummy import current_process

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            return
        else:
            currentNode = self.root
            while True:
                if value < currentNode.value:
                    if not currentNode.left:
                        currentNode.left = newNode
                        return
                    else:
                        currentNode = currentNode.left
                elif value > currentNode.value:
                    if not currentNode.right:
                        currentNode.right = newNode
                        return
                    else:
                        currentNode = currentNode.right


    def lookup(self, value):
        if not self.root:
            return None
        else:
            currentNode = self.root
            while currentNode:
                if currentNode.value == value:
                    return currentNode
                elif value > currentNode.value:
                    currentNode = currentNode.right
                    continue
                else:
                    currentNode = currentNode.left
                    continue
        return

    # def remove(self, value)


def traverse(node):
    tree = {'value': node.value}
    tree.left = node.left == None if None else traverse(node.left)
    tree.right = node.right == None if None else traverse(node.right)
    return tree

tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree2 = traverse(tree)
# json_list = json.dumps(tree2, separators=(',', ':'))
# print(json_list)