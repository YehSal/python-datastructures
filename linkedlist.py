#!/usr/bin/env python3

"""
This module is a linked list implementation.
"""

class Node:
    """
    Node class to be used in our linked list.
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Linkedlist:
    """
    Linked list implementation that supports functions including inserting
    at head, inserting at tail, extracting elements, and displaying all
    elements in the ist
    """
    def __init__(self, head):
        self.head = Node(head)
        self.tail = Node(head)

    def insert_tail(self, value):
        """
        Insert new node to the tail of the linked list.
        Time Complexity: O(n)
        """
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
        self.tail = current.next

    def insert_head(self, value):
        """
        Insert new node to the head of the linked list, making sure to update head.
        Time Complexity: O(1)
        """
        to_insert = Node(value)
        to_insert.next = self.head
        self.tail = self.head
        self.head = to_insert

    def extract(self, value):
        """
        Remove element specified and return it
        """
        current = self.head

        if current.value == value:
            self.head = self.head.next # Extract head
            return current

        while current.next is not None: # Extract middle or tail node
            if current.next.value == value:

                if current.next == self.tail:
                    tail_old = current.next
                    self.tail = current
                    return tail_old

                to_return = current.next
                current.next = current.next.next
                return to_return

            current = current.next

        return False

    def find(self, value):
        """
        Find a specific element in the linked list
        """
        current = self.head

        while current is not None:
            if current.value == value:
                return current
            current = current.next

    def display(self):
        """
        Print all node values in the linked list
        """
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def size(self):
        size = 0
        current = self.head

        while current is not None:
            size += 1
            current = current.next

        return size

    def _is_empty(self):
        """
        Check if list is empty
        """
        if self.head is None:
            return True
        return False
