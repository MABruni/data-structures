"""
Module for implementing a simple Hash Table (also known as a Hash Map).
This implementation supports insertion, retrieval, deletion, and rehashing
of elements. The hash table resizes dynamically when the load factor exceeds
a predefined threshold.
"""

class HashTable():
    """
    A simple implementation of a hash table (hash map) that stores key-value pairs.
    
    The hash table uses separate chaining for collision resolution. It resizes
    dynamically by doubling the table size once the load factor exceeds 0.7.
    """

    def __init__(self, size: int = 10):
        """
        Initializes a new hash table with a specified initial size.

        Args:
            size (int): The initial size of the hash table. Default is 10.
        """
        self._size = size
        self._list = [[] for _ in range(self._size)]
        self._usage = 0

    def usage(self):
        """
        Returns the number of elements currently stored in the hash table.

        This value indicates how many key-value pairs exist in the hash table,
        regardless of its size.

        Returns:
            int: The total number of elements in the hash table.
        """
        return self._usage

    def load(self) -> float:
        """
        Returns the current load factor of the hash table.

        The load factor is the ratio of the number of elements to the size of the table.

        Returns:
            float: The load factor of the hash table.
        """
        return self._usage / self._size

    def _hash(self, key: any) -> int:
        """
        Computes a hash value for the given key.

        The hash function sums the Unicode code points of each character in the key
        and returns the remainder when divided by the table size.

        Args:
            key (any): The key to be hashed.

        Returns:
            int: The computed hash value for the given key.
        """
        return sum(ord(char) for char in str(key)) % self._size

    def rehash(self) -> None:
        """
        Resizes the hash table by doubling its size and rehashing all existing elements.

        The table size is doubled and elements are redistributed based on their new hash values.
        """
        self._size *= 2
        new_list = [[] for _ in range(self._size)]
        for buckets in self._list:
            for (existing_key, existing_data) in buckets:
                new_hash = self._hash(existing_key)
                new_list[new_hash].append((existing_key, existing_data))
        self._list = new_list

    def insert(self, key: any, data: any) -> None:
        """
        Inserts a key-value pair into the hash table.

        If the key already exists, its value is updated. If the load factor exceeds 0.7,
        the table is resized by doubling its size.

        Args:
            key (any): The key to insert.
            data (any): The value associated with the key.
        """
        self._usage += 1
        if self.load() >= 0.7:
            self.rehash()
        hash_index = self._hash(key)
        bucket = self._list[hash_index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, data)
                return
        bucket.append((key, data))

    def get(self, key: any) -> any:
        """
        Retrieves the value associated with a given key.

        If the key is not found, returns None.

        Args:
            key (any): The key whose associated value is to be retrieved.

        Returns:
            any: The value associated with the given key, or None if the key is not found.
        """
        hash_index = self._hash(key)
        bucket = self._list[hash_index]
        for _, (existing_key, existing_data) in enumerate(bucket):
            if existing_key == key:
                return existing_data
        return None

    def remove(self, key: any) -> None:
        """
        Removes the key-value pair from the hash table.

        If the key does not exist in the table, raises a ValueError.

        Args:
            key (any): The key to remove.

        Raises:
            ValueError: If the key does not exist in the hash table.
        """
        hash_index = self._hash(key)
        bucket = self._list[hash_index]
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                return
        raise ValueError(f"No entry with key {key}")
