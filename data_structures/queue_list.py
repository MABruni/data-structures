"""
queue_list.py
========

This module provides a simple implementation of a queue data structure.
A queue is a collection of elements that follows the First-In-First-Out (FIFO) principle.
Elements are added to the end of the queue and removed from the front.

Classes:
    - Queue: Represents the queue and provides methods for enqueueing, dequeueing,
      peeking, checking if the queue is empty, and getting the size of the queue.
"""
class Queue:
    """
    A simple implementation of a queue data structure.

    The queue follows the First-In-First-Out (FIFO) principle, where elements are added 
    to the end of the queue and removed from the front. This implementation uses a list 
    to store the elements.
    
    Methods:
        - enqueue(value): Adds an element to the end of the queue.
        - dequeue(): Removes and returns the front element of the queue.
        - peek(): Returns the front element without removing it.
        - is_empty(): Checks if the queue is empty.
        - size(): Returns the number of elements in the queue.
    """
    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._queue = []

    def enqueue(self, value: any) -> None:
        """
        Add an element to the end of the queue.

        Args:
            value (any): The element to add to the queue.
        """
        self._queue.append(value)

    def dequeue(self) -> any:
        """
        Remove and return the front element of the queue.

        Returns:
            any: The element removed from the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self._queue.pop(0)

    def peek(self) -> any:
        """
        Return the front element of the queue without removing it.

        Returns:
            any: The element at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self._queue[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self._queue) == 0

    def size(self) -> int:
        """Return the number of elements in the queue.

        Returns:
            int: The size of the queue.
        """
        return len(self._queue)
