"""
Test suite for the HashTable class.

This module contains tests for the custom `HashTable` implementation, covering:
- Basic functionality: insertion, retrieval, and removal of key-value pairs.
- Load factor calculation and its impact on performance.
- Rehashing: both manual and automatic, ensuring data integrity during resizing.
- Edge cases: handling empty strings, `None` as keys, and duplicate key updates.
- Error handling: ensuring appropriate exceptions are raised for invalid operations.

The tests use `pytest` for efficient test execution and rely on fixtures to
initialize a `HashTable` instance with pre-inserted values.

Tests included:
1. `test_load`: Verifies correct calculation of the load factor.
2. `test_rehash`: Ensures rehashing maintains data integrity and updates the table size.
3. `test_automatic_rehash`: Tests automatic rehashing triggered by exceeding the 
    load factor threshold.
4. `test_insert`: Checks insertion of new items and updates to existing ones.
5. `test_get`: Validates retrieval for existing keys and returns `None` for non-existent keys.
6. `test_remove`: Tests removal of keys and proper handling of non-existent keys.
7. `test_edge_cases`: Covers edge cases such as empty strings, `None`, and duplicate keys.
"""
import pytest
from data_structures.hash_table import HashTable

@pytest.fixture(name="ht")
def hash_fixture():
    """
    Fixture to initialize a HashTable with some pre-inserted values.
    """
    ht = HashTable()
    ht.insert('hello', 10)
    ht.insert('bye', 20)
    return ht

def test_load(ht):
    """
    Test the load factor calculation.
    """
    assert ht.load() == 2 / 10

def test_rehash(ht):
    """
    Test rehashing preserves data integrity.
    """
    ht.rehash()
    assert ht.get('hello') == 10
    assert ht.get('bye') == 20
    assert ht.load() == 2 / 20  # Load factor after rehashing

def test_automatic_rehash(ht):
    """
    Test automatic rehashing when the load factor exceeds the threshold.
    """
    # Insert enough items to trigger a rehash
    for i in range(3, 9):
        ht.insert(str(i), i * 10)

    assert ht.usage() == 8  # 2 pre-inserted + 6 new items
    assert ht.load() == 8 / 20  # Table size doubled to 20
    assert ht.get('hello') == 10  # Ensure data integrity after rehash

def test_insert(ht):
    """
    Test inserting new items and updating existing ones.
    """
    # Insert new keys
    ht.insert('new_key', 50)
    ht.insert('another_key', 60)
    assert ht.usage() == 4

    # Update an existing key
    ht.insert('hello', 100)
    assert ht.get('hello') == 100

def test_get(ht):
    """
    Test retrieving values for existing and non-existing keys.
    """
    assert ht.get('hello') == 10
    assert ht.get('bye') == 20

    # Test for a non-existent key
    assert ht.get('nonexistent') is None

def test_remove(ht):
    """
    Test removing an existing key and handling removal of a non-existing key.
    """
    ht.remove('hello')
    assert ht.get('hello') is None  # Key no longer exists

    # Attempt to remove a non-existent key
    with pytest.raises(ValueError, match="No entry with key nonexistent"):
        ht.remove('nonexistent')

def test_edge_cases(ht):
    """
    Test edge cases like empty strings, None, and duplicate keys.
    """
    # Empty string as a key
    ht.insert('', 123)
    assert ht.get('') == 123

    # None as a key
    ht.insert(None, 456)
    assert ht.get(None) == 456

    # Duplicate key updates
    ht.insert('duplicate', 1)
    ht.insert('duplicate', 2)
    assert ht.get('duplicate') == 2
