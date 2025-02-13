"""
node.py
=======

This module defines the `Node` class for use in doubly linked lists.

The `Node` class represents a single element in the linked list, storing data
and references to both the next and previous nodes in the list. This class
provides getters and setters for the data and the links (next and previous)
using Python's `property` decorators for a more Pythonic interface.

Exceptions:
    - `InvalidArgument`: Raised when invalid arguments are passed to the setters.

Classes:
    - `Node`: A class representing a node in a doubly linked list with attributes 
      for data, next node, and previous node, as well as properties for managing 
      these attributes.

Usage:
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2
    node2.previous = node1
    print(node1.data)      # Output: 10
    print(node1.next.data) # Output: 20
    print(node2.previous.data) # Output: 10
"""

class InvalidArgument(Exception):
    """Custom exception raised when an invalid argument is provided."""

class Node:
    """
    Represents a node in a doubly linked list.

    Attributes:
        data (any): The data stored in the node.
        next (Node): The reference to the next node in the list.
        previous (Node): The reference to the previous node in the list.
    """
    def __init__(self, data, next_node=None, previous=None) -> None:
        """
        Initializes a new node in the linked list.

        Args:
            data (any): The data to store in the node.
            next_node (Node, optional): The reference to the next node. Defaults to None.
            previous (Node, optional): The reference to the previous node. Defaults to None.
        """
        self._data = data
        self._next = next_node
        self._previous = previous

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
        Sets the data for the node.

        Args:
            value (any): The new data to store in the node.
        """
        self._data = value

    @property
    def next(self):
        """
        Retrieves the reference to the next node in the list.

        Returns:
            Node: The next node, or None if there is no next node.
        """
        return self._next

    @next.setter
    def next(self, new_node):
        """
        Sets the reference to the next node in the list.

        Args:
            new_node (Node or None): The new next node to link to, or None.

        Raises:
            InvalidArgument: If the new_node is not a Node instance or None.
        """
        if new_node is None or isinstance(new_node, Node):
            self._next = new_node
        else:
            raise InvalidArgument("Next needs to be None or a Node object.")

    @property
    def previous(self):
        """
        Retrieves the reference to the previous node in the list.

        Returns:
            Node: The previous node, or None if there is no previous node.
        """
        return self._previous

    @previous.setter
    def previous(self, new_node):
        """
        Sets the reference to the previous node in the list.

        Args:
            new_node (Node or None): The new previous node to link to, or None.

        Raises:
            InvalidArgument: If the new_node is not a Node instance or None.
        """
        if new_node is None or isinstance(new_node, Node):
            self._previous = new_node
        else:
            raise InvalidArgument("Previous needs to be None or a Node object.")

class DoubleLinkedList:
    """
    A class representing a doubly linked list.

    Attributes:
        _head (Node | None): The first node in the list.
        _tail (Node | None): The last node in the list.
        _size (int): The number of nodes in the list.

    Methods:
        is_empty(): Returns True if the list is empty, False otherwise.
        size(): Returns the number of nodes in the list.
        head(): Returns the first node of the list.
        insert_at_head(new_node: Node): Inserts a new node at the beginning of the list.
        insert_at_tail(new_node: Node): Inserts a new node at the end of the list.
        insert_at_position(new_node: Node, position: int): Inserts a new node at
            a specific position.
        delete_from_head(): Deletes the node at the beginning of the list.
        delete_from_tail(): Deletes the node at the end of the list.
        delete_from_position(position: int): Deletes the node at a specific position.
        find(value: any): Finds and returns the first node with the specified data.
        update_node(old_data: any, new_data: any): Updates the data of the node
            with the specified old data.
        traversal_forward(): Returns a list of node data traversed from head to tail.
        traversal_backward(): Returns a list of node data traversed from tail to head.
        clear(): Clears all nodes from the list.
    """

    def __init__(self) -> None:
        """
        Initializes an empty doubly linked list.

        Attributes are set to None for both head and tail, and the size is set to 0.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self) -> bool:
        """
        Checks if the list is empty.

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self._head is None
    
    @property
    def size(self) -> int:
        """
        Returns the number of nodes in the list.

        Returns:
            int: The size of the list.
        """
        return self._size

    @property
    def head(self):
        """
        Returns the first node in the list.

        Returns:
            Node | None: The head node, or None if the list is empty.
        """
        return self._head
    
    @property
    def tail(self):
        """
        Returns the last node in the list.

        Returns:
            Node | None: The tail node, or None if the list is empty.
        """
        return self._tail

    def insert_at_head(self, new_node: Node) -> None:
        """
        Inserts a new node at the beginning of the list.

        Args:
            new_node (Node): The node to be inserted.

        Raises:
            TypeError: If the new node is not an instance of Node.
        """
        if new_node is None or isinstance(new_node, Node):
            if self._head is None:
                self._head, self._tail = new_node, new_node
            else:
                new_node.next = self._head
                self._head = new_node
                new_node.next.previous = self._head
            self._size += 1
        else:
            raise TypeError("new_node must be an instance of Node or None")

    def insert_at_tail(self, new_node: Node) -> None:
        """
        Inserts a new node at the end of the list.

        Args:
            new_node (Node): The node to be inserted.

        Raises:
            TypeError: If the new node is not an instance of Node.
        """
        if isinstance(new_node, Node):
            if self.is_empty():
                self._head, self._tail = new_node, new_node
            else:
                new_node.previous = self._tail
                self._tail.next = new_node
                self._tail = new_node
            self._size += 1
        else:
            raise TypeError("new_node must be an instance of Node")

    def insert_at_position(self, new_node: Node, position: int) -> None:
        """
        Inserts a new node at a specific position in the list.

        Args:
            new_node (Node): The node to be inserted.
            position (int): The position where the new node should be inserted.

        Raises:
            IndexError: If the position is out of bounds.
            TypeError: If the new node is not an instance of Node.
        """
        if position < 0 or position > self._size:
            raise IndexError("Position must be a valid index")
        if isinstance(new_node, Node):
            if position == 0:
                self.insert_at_head(new_node)
            elif position == self._size:
                self.insert_at_tail(new_node)
            else:
                current = self._head
                count = 0
                while count != position:
                    current = current.next
                    count += 1
                new_node.previous = current.previous
                new_node.next = current
                current.previous.next = new_node
                current.previous = new_node
                self._size += 1
        else:
            raise TypeError("new_node must be an instance of Node")

    def delete_from_head(self) -> None:
        """
        Deletes the node at the beginning of the list.

        Raises:
            IndexError: If the list is empty.
        """
        if self._size == 0:
            raise IndexError("Cannot delete from an empty list")
        if self._size == 1:
            self._head, self._tail = None, None
        else:
            self._head = self._head.next
            self._head.previous = None
        self._size -= 1

    def delete_from_tail(self) -> None:
        """
        Deletes the node at the end of the list.

        Raises:
            IndexError: If the list is empty.
        """
        if self._size == 0:
            raise IndexError("Cannot delete from an empty list")
        if self._size == 1:
            self._head, self._tail = None, None
        else:
            self._tail = self._tail.previous
            self._tail.next = None
        self._size -= 1

    def delete_from_position(self, position: int) -> None:
        """
        Deletes the node at a specific position.

        Args:
            position (int): The position of the node to be deleted.

        Raises:
            IndexError: If the position is out of bounds.
        """
        if self._size == 0:
            raise IndexError("Cannot delete from an empty list")
        if position < 0 or position >= self._size:
            raise IndexError(f"Position out of bounds, must be between 0 and {self._size - 1}")
        if position == 0:
            self.delete_from_head()
        elif position == self._size - 1:
            self.delete_from_tail()
        else:
            count = 0
            current = self._head
            while count != position:
                current = current.next
                count += 1
            current.previous.next = current.next
            current.next.previous = current.previous
            self._size -= 1

    def find(self, value: any) -> Node | None:
        """
        Finds and returns the first node with the specified value.

        Args:
            value (any): The value to search for.

        Returns:
            Node | None: The node containing the specified value, or None if not found.
        """
        current = self._head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def update_node(self, old_data: any, new_data: any) -> None:
        """
        Updates the data of the node containing the specified old data.

        Args:
            old_data (any): The data to search for.
            new_data (any): The new data to update the node with.

        Raises:
            IndexError: If the list is empty.
            ValueError: If no node with the specified old data is found.
        """
        if self.is_empty():
            raise IndexError("Cannot update empty list.")
        current = self._head
        while current:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next
        raise ValueError(f"Node with data {old_data} not found in the list.")

    def traversal_forward(self):
        """
        Traverses the list from head to tail and returns the node data in a list.

        Returns:
            list: A list of node data from head to tail.
        """
        result = []
        current = self._head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def traversal_backward(self):
        """
        Traverses the list from tail to head and returns the node data in a list.

        Returns:
            list: A list of node data from tail to head.
        """
        result = []
        current = self._tail
        while current:
            result.append(current.data)
            current = current.previous
        return result

    def clear(self):
        """
        Clears all nodes from the list, resetting the head, tail, and size.

        After calling this method, the list will be empty.
        """
        if self._head != self._tail:
            self._head.next, self._tail.previous = None, None
        self._head, self._tail = None, None
        self._size = 0

if __name__ == "__main__":
    dll = DoubleLinkedList()
    # Add initial nodes for the fixture
    node1 = Node(10)
    node2 = Node(20)
    dll.insert_at_head(node1)
    dll.insert_at_head(node2)
    dll.clear()
