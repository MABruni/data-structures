import pytest
from data_structures.double_linked_list import Node, DoubleLinkedList

@pytest.fixture(name="dll")
def doubly_linked_list():
    """Fixture to set up a new doubly linked list before each test."""
    dll = DoubleLinkedList()
    # Add initial nodes for the fixture
    node1 = Node(10)
    node2 = Node(20)
    dll.insert_at_head(node1)
    dll.insert_at_head(node2)
    return dll

def test_insert_at_head(dll):
    """Test insertion of nodes at the head."""
    node1 = Node(30)
    node2 = Node(40)
    dll.insert_at_head(node1)
    dll.insert_at_head(node2)

    assert dll.head.data == 40  # New head after insertion
    assert dll.size == 4  # Size should be 4 now (2 from the fixture + 2 inserted)
    assert dll.head.next.data == 30

def test_insert_at_tail(dll):
    """Test insertion of nodes at the tail."""
    node1 = Node(30)
    node2 = Node(40)
    dll.insert_at_tail(node1)
    dll.insert_at_tail(node2)

    # Traverse forward to check the node values
    result = dll.traversal_forward()
    assert result == [20, 10, 30, 40]
    assert dll.size == 4  # Size should be 4 after two insertions at the tail

def test_insert_at_position(dll):
    """Test insertion at a specific position."""
    node1 = Node(30)
    node2 = Node(40)
    dll.insert_at_position(node1, 1)  # Insert at position 1
    dll.insert_at_position(node2, 2)  # Insert at position 2

    result = dll.traversal_forward()
    assert result == [20, 30, 40, 10]
    assert dll.size == 4  # Size should be 4 after insertions

def test_delete_from_head(dll):
    """Test deletion from the head."""
    dll.delete_from_head()
    assert dll.head.data == 10  # 10 should now be the head
    assert dll.size == 1  # Size should decrease by 1

def test_delete_from_tail(dll):
    """Test deletion from the tail."""
    dll.delete_from_tail()
    result = dll.traversal_forward()
    assert result == [20]  # 20 should remain
    assert dll.size == 1  # Size should decrease by 1

def test_delete_from_position(dll):
    """Test deletion from a specific position."""
    dll.delete_from_position(1)  # Delete node at position 1
    result = dll.traversal_forward()
    assert result == [20]  # Only the node with value 20 should remain
    assert dll.size == 1  # Size should decrease by 1

def test_find_node(dll):
    """Test finding a node by its data."""
    found_node = dll.find(20)
    assert found_node.data == 20  # Should find the node with value 20

def test_update_node(dll):
    """Test updating a node's data."""
    dll.update_node(20, 25)
    updated_node = dll.find(25)
    assert updated_node.data == 25  # Node should be updated to 25

def test_traversal_forward(dll):
    """Test traversal in forward direction."""
    result = dll.traversal_forward()
    assert result == [20, 10]  # Should return values in forward order

def test_traversal_backward(dll):
    """Test traversal in backward direction."""
    result = dll.traversal_backward()
    assert result == [10, 20]  # Should return values in backward order

def test_clear(dll):
    """Test clearing the entire list."""
    dll.clear()
    assert dll.size == 0  # Size should be 0 after clearing
    assert dll.head is None  # Head should be None after clearing
    assert dll.tail is None

def test_is_empty(dll):
    """Test is_empty method."""
    assert dll.is_empty() is False  # It should be False as the list is not empty

    # Remove nodes and check again
    dll.delete_from_head()
    dll.delete_from_tail()
    assert dll.is_empty() is True  # It should be True after clearing all nodes
