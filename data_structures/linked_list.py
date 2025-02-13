"""
linked_list.py
==============

This module implements a basic singly linked list data structure.

Classes:
    - Node: Represents a node in the linked list.
    - LinkedList: Provides methods for managing a linked list, including
      insertion, traversal, searching, and checking if the list is empty.

Usage:
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(20)
    linked_list.traversal(print)  # Prints the linked list nodes.
"""
class Node():
    """
    Represents a node in a singly linked list.

    Attributes:
        data (any): The data stored in the node.
        next (Node): The reference to the next node in the list.
    """
    def __init__(self, data: any, next_node: 'Node' = None) -> None:
        """
        Initializes a new Node instance.

        Args:
            data (any): The data to store in the node.
            next_node (Node, optional): The reference to the next node. Defaults to None.
        """
        self._data = data
        self._next = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            any: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """
        Sets the data of the node.

        Args:
            value (any): The new data to store in the node.
        """
        self._data = value

    @property
    def next(self):
        """
        Retrieves the reference to the next node.

        Returns:
            Node: The next node in the linked list, or None if this is the last node.
        """
        return self._next

    @next.setter
    def next(self, new_node):
        """
        Sets the reference to the next node.

        Args:
            new_node (Node): The new next node, or None.

        Raises:
            TypeError: If new_node is not a Node or None.
        """
        if new_node is None or isinstance(new_node, Node):
            self._next = new_node
        else:
            raise TypeError("Next link must be a Node or None")

    @property
    def is_last(self):
        """
        Checks if this node is the last node in the list.

        Returns:
            bool: True if the node is the last, False otherwise.
        """
        return self.next is None

    def __str__(self):
        """
        Returns a string representation of the node's data.

        Returns:
            str: The string representation of the data.
        """
        return str(self.data)

    def __repr__(self):
        """
        Returns a detailed string representation of the node.

        Returns:
            str: A string in the format 'Node(data=<data>)'.
        """
        return f"Node(data={self.data})"


class LinkedList():
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head (first node) of the linked list.
    """
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self._head = None

    @property
    def head(self):
        """
        Retrieves the head of the linked list.

        Returns:
            Node: The head node of the linked list, or None if the list is empty.
        """
        return self._head

    @head.setter
    def head(self, new_node):
        """
        Sets the head of the linked list.

        Args:
            new_node (Node): The new head node, or None.

        Raises:
            TypeError: If new_node is not a Node or None.
        """
        if new_node is None or isinstance(new_node, Node):
            self._head = new_node
        else:
            raise TypeError("First node must be None or a Node object.")

    def traversal(self, func=print):
        """
        Traverses the linked list and applies a function to each node's data.

        Args:
            func (callable): The function to apply to each node's data. Defaults to print.
        """
        current = self.head
        while current is not None:
            func(current.data)
            current = current.next

    def insert(self, data):
        """
        Inserts a new node with the given data at the beginning of the linked list.

        Args:
            data (any): The data to insert into the new node.
        """
        new_node = Node(data, self.head)
        self.head = new_node

    def find(self, value):
        """
        Finds the first node with the specified value and its position in the list.

        Args:
            value (any): The value to search for.

        Returns:
            tuple: A message and the position of the node if found, otherwise None and -1.
        """
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return f"Node with value {current.data} found at position {index}"
            current = current.next
            index += 1
        return None, -1

    def is_empty(self):
        """
        Checks if the linked list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self.head is None
