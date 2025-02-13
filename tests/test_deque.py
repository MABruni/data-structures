"""
Test suite for the Deque class.

This module tests the functionality of a custom Deque implementation. The tests
cover appending, popping, peeking, checking emptiness, and exception handling
for operations on an empty deque.

Features tested:
1. Appending items to both ends.
2. Removing items from both ends.
3. Accessing items without removing them (peeking).
4. Checking if the deque is empty.
5. Proper exception handling for invalid operations on an empty deque.

Usage:
Run the following command to execute all tests:
    pytest test_deque.py

Dependencies:
- pytest: For running test cases.
- Deque: The implementation being tested.
"""

import pytest
from data_structures.deque_list import Deque

@pytest.fixture(name="deque")
def deque_fixture() -> Deque:
    """
    Fixture to initialize a Deque with pre-inserted values.
    
    Returns:
        Deque: A deque with initial values 1 and 'hello'.
    """
    deque = Deque()
    deque.append(1)
    deque.append('hello')
    return deque

def test_append(deque: Deque):
    """
    Test appending items to the right side of the deque.

    Verifies:
        - Appending increases the size of the deque.
    """
    assert deque.size() == 2

def test_append_left(deque: Deque):
    """
    Test appending items to the left side of the deque.

    Verifies:
        - Appending to the left increases the size of the deque.
    """
    deque.append_left(3)
    assert deque.size() == 3

def test_pop(deque: Deque):
    """
    Test removing and returning the rightmost item from the deque.

    Verifies:
        - Popping removes the last item.
        - The size decreases after popping.
    """
    last_item = deque.pop()
    assert last_item == 'hello'
    assert deque.size() == 1

def test_pop_left(deque: Deque):
    """
    Test removing and returning the leftmost item from the deque.

    Verifies:
        - Popping from the left removes the first item.
        - The size decreases after popping.
    """
    first_item = deque.pop_left()
    assert first_item == 1
    assert deque.size() == 1

def test_peek_right(deque: Deque):
    """
    Test returning the rightmost item without removing it.

    Verifies:
        - Peeking does not modify the deque size.
        - The correct rightmost item is returned.
    """
    assert deque.peek_right() == 'hello'

def test_peek_left(deque: Deque):
    """
    Test returning the leftmost item without removing it.

    Verifies:
        - Peeking does not modify the deque size.
        - The correct leftmost item is returned.
    """
    assert deque.peek_left() == 1

def test_is_empty(deque: Deque):
    """
    Test checking if the deque is empty.

    Verifies:
        - `is_empty()` returns False for a non-empty deque.
        - `is_empty()` returns True after all items are removed.
    """
    assert deque.is_empty() is False
    deque.pop()
    deque.pop()
    assert deque.is_empty() is True

def test_empty_pop():
    """
    Test popping from an empty deque raises an exception.

    Verifies:
        - An `IndexError` is raised with the correct message.
    """
    deque = Deque()
    with pytest.raises(IndexError, match="Pop from an empty deque"):
        deque.pop()

def test_empty_pop_left():
    """
    Test popping from the left of an empty deque raises an exception.

    Verifies:
        - An `IndexError` is raised with the correct message.
    """
    deque = Deque()
    with pytest.raises(IndexError, match="Pop from an empty deque"):
        deque.pop_left()

def test_empty_peek_right():
    """
    Test peeking at the rightmost item in an empty deque raises an exception.

    Verifies:
        - An `IndexError` is raised with the correct message.
    """
    deque = Deque()
    with pytest.raises(IndexError, match="Peek from an empty deque"):
        deque.peek_right()

def test_empty_peek_left():
    """
    Test peeking at the leftmost item in an empty deque raises an exception.

    Verifies:
        - An `IndexError` is raised with the correct message.
    """
    deque = Deque()
    with pytest.raises(IndexError, match="Peek from an empty deque"):
        deque.peek_left()
