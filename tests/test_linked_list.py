"""
linked_list_tests.py
====================

This module contains unit tests for the LinkedList and Node classes.

It tests the basic functionality of the LinkedList, such as insertion,
traversal, searching for values, and checking if the list is empty. It also
tests the Node class, including the data and next references, as well as 
various edge cases such as invalid operations.

Test Functions:
    - test_insert: Tests inserting elements into the linked list.
    - test_traversal: Tests traversing the linked list.
    - test_find_existing_value: Tests finding an existing value in the linked list.
    - test_find_non_existing_value: Tests finding a non-existing value in the linked list.
    - test_is_empty: Tests checking if the linked list is empty.
    - test_node_data_setter: Tests the setter for the node's data.
    - test_node_next_setter: Tests the setter for the node's next reference.
    - test_invalid_node_next_setter: Tests setting invalid next value on a node.
    - test_node_is_last: Tests checking if the node is the last in the list.
    - test_node_str_repr: Tests the string and repr representation of the node.
    - test_linked_list_head_setter: Tests setting the head of the linked list.
    - test_invalid_linked_list_head_setter: Tests setting an invalid head value on the linked list.
"""

import pytest
from data_structures.linked_list import LinkedList, Node


@pytest.fixture(name="linked_list")
def linked_list_fixture():
    """Builds the initial linked list to perform tests"""
    ll = LinkedList()
    ll.insert(10)
    ll.insert(20)
    return ll


def test_insert(linked_list):
    """Test inserting elements into the linked list."""
    assert linked_list.head.data == 20  # The most recent insert should be at the head
    assert linked_list.head.next.data == 10  # The previous element should be linked


def test_traversal(linked_list):
    """Test traversing the linked list."""
    result = []
    linked_list.traversal(result.append)
    assert result == [20, 10]  # Should traverse the list in order: head -> next


def test_find_existing_value(linked_list):
    """Test finding an existing value in the linked list."""
    result = linked_list.find(10)
    assert result == "Node with value 10 found at position 1"


def test_find_non_existing_value(linked_list):
    """Test finding a non-existing value in the linked list."""
    result = linked_list.find(30)
    assert result == (None, -1)  # The value 30 should not be found


def test_is_empty(linked_list):
    """Test checking if the linked list is empty."""
    assert linked_list.is_empty() is False  # The list should not be empty
    empty_ll = LinkedList()
    assert empty_ll.is_empty() is True  # An empty linked list should return True


def test_node_data_setter():
    """Test the setter for the node's data."""
    node = Node(10)
    assert node.data == 10  # Initially the data should be 10
    node.data = 20
    assert node.data == 20  # The data should be updated to 20


def test_node_next_setter():
    """Test the setter for the node's next reference."""
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2
    assert node1.next == node2  # node1 should point to node2
    assert node2.is_last is True  # node2 should be the last node


def test_invalid_node_next_setter():
    """Test setting an invalid next value on a node."""
    node = Node(10)
    with pytest.raises(TypeError):  # Expecting TypeError when setting next to a non-Node value
        node.next = "invalid"


def test_node_is_last():
    """Test checking if the node is the last in the list."""
    node1 = Node(10)
    node2 = Node(20)
    node1.next = node2
    assert node1.is_last is False  # node1 should not be the last node
    assert node2.is_last is True  # node2 should be the last node


def test_node_str_repr():
    """Test the string and repr representation of the node."""
    node = Node(10)
    assert str(node) == "10"  # str should return the data as a string
    assert repr(node) == "Node(data=10)"  # repr should return a detailed representation


def test_linked_list_head_setter():
    """Test setting the head of the linked list."""
    ll = LinkedList()
    node = Node(30)
    ll.head = node
    assert ll.head == node  # The head of the list should be the node just set


def test_invalid_linked_list_head_setter():
    """Test setting an invalid head value on the linked list."""
    ll = LinkedList()
    with pytest.raises(TypeError):  # Expecting TypeError when setting the head to a non-Node value
        ll.head = "invalid"
