class Stack:
    """A simple implementation of a stack data structure."""
    def __init__(self) -> None:
        """Initializes an empty stack."""
        self._stack = []

    def push(self, value: 'any') -> None:
        """
        Adds a value to the top of the stack.
        
        Args:
            value (any): The element to add to the stack."""
        self._stack.append(value)

    def pop(self) -> any:
        """
        Removes the value at the top of the stack and returns it.

        Returns:
            any: The element removed from the top of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        return self._stack.pop()

    def peek(self) -> any:
        """
        Returns the value at the top of the stack without removing it.

        Returns:
            any: The value at the top of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self._stack[-1]

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._stack) == 0

    def size(self) -> int:
        """
        Returns the number of elements in the stack.

        Returns:
            int: The size of the stack.
        """
        return len(self._stack)
