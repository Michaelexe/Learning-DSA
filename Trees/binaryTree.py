from dataclasses import dataclass
from turtle import right


class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def traversePreOrder(self):
        print(self.value, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.value, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.value, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
