class Deque:
    def __init__(self) -> None:
        """
        Initializes an empty deque.
        """
        self._deque = []

    def size(self) -> int:
        """
        Returns the number of elements in the deque.

        Returns:
            int: The size of the deque.
        """
        return len(self._deque)

    def is_empty(self) -> bool:
        """
        Checks whether the deque is empty.

        Returns:
            bool: True if the deque is empty, False otherwise.
        """
        return len(self._deque) == 0

    def append(self, value: any) -> None:
        """
        Appends a value to the end of the deque.

        Args:
            value (any): The value to be appended to the deque.
        """
        self._deque.append(value)

    def append_left(self, value: any) -> None:
        """
        Adds a value to the front of the deque.

        Args:
            value (any): The value to be added to the front of the deque.
        """
        self._deque.insert(0, [value])

    def peek_left(self) -> any:
        """
        Returns the first item from the deque without removing it.

        If the deque is empty, raises an IndexError with the message "Peek from an empty deque".

        Returns:
            any: The first item from the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty deque")
        return self._deque[0]

    def peek_right(self) -> any:
        """
        Returns the last item from the deque without removing it.

        If the deque is empty, raises an IndexError with the message "Peek from an empty deque".

        Returns:
            any: The last item from the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty deque")
        return self._deque[-1]

    def pop(self) -> any:
        """
        Removes and returns the last item from the deque.
        If the deque is empty, raises an IndexError.

        Returns:
            int: The last item from the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty deque")
        return self._deque.pop()

    def pop_left(self) -> any:
        """
        Removes and returns the first item from the deque.
        If the deque is empty, raises an IndexError.

        Returns:
            any: The first item from the deque.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty deque")
        return self._deque.pop(0)

    def index(self, value: any, beg: int = 0, end: int | None = None) -> set[int] | None:
        """
        Finds all indexes of a value within a specified range in the deque.

        Args:
            value (any): The value to search for in the deque.
            beg (int): The starting index for the search.
            end (int): The ending index for the search.

        Returns:
            set[int] | None: A set of indexes where the value is found in the specified range, 
            or None if the value is not found.
        
        Raises:
            IndexError: If the starting or ending index is out of bounds.
        """
        if beg < 0 or end > len(self._deque) - 1:
            raise IndexError("Invalid start and/or end values")
        if beg > end:
            raise IndexError("Start index cannot be greater than end index")
        if end is None:
            end = len(self._deque)
        result = set()
        for index in range(beg, end):
            if self._deque[index] == value:
                result.add(index)
        return result if result else None

    def insert(self, value: any, index: int) -> None:
        """
        Inserts a value at the specified index in the deque.

        Args:
            value (any): The value to be inserted.
            index (int): The index where the value should be inserted.
        """
        self.append(value)
        for prev_index in range(self.size() - 2, index - 1, -1):
            self._deque[prev_index], self._deque[prev_index+1] = (
                self._deque[prev_index+1], self._deque[prev_index]
                )

    def remove(self, value: any) -> str:
        """
        Removes the first occurrence of a value from the deque.

        Args:
            value (any): The value to be removed.

        Returns:
            str: A message indicating whether the value was found and deleted, 
            or not found in the deque.
        """
        for index, values in enumerate(self._deque):
            if values == value:
                del self._deque[index]
                return f"Value deleted at index {index}"
        return "Value not in deque"

    def count(self, value: any) -> str:
        """
        Counts the occurrences of a value in the deque.

        Args:
            value (any): The value to count in the deque.

        Returns:
            str: A message indicating how many times the value appears in the deque.
        """
        indexes = len(self.index(value))
        count = len(indexes) if indexes else 0
        return f"Value found {count} times"

    def display(self) -> None:
        """
        Prints the current state of the deque.

        Returns:
            None: This function does not return anything, it only prints the deque.
        """
        print(self._deque)
