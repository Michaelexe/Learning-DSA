from operator import index
from tkinter import NoDefaultRoot


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head - new_node

    def insertAfter(self, prev_node, data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete(self, indexFromZero):
        temp_node = self.head

        if indexFromZero == 0:
            self.head = temp_node.next
            return

        # Find the Node previous to the one being deleted
        for i in range(indexFromZero - 1):
            temp_node = temp_node.next
            if temp_node is None:
                break

         # If the node is not present
        if temp_node is None:
            return

        if temp_node.next is None:
            return
        
        temp_next = temp_node.next.next
        temp_node.next = temp_next

    def search(self, key):
        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    def sortLinkedList(self):
        current = self.head
        index = Node(None)

        if self.head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next