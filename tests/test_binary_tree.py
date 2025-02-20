import pytest
from data_structures.binary_tree import BinaryTree

@pytest.fixture(name="bt")
def binary_tree_fixture():
    bt = BinaryTree()
    bt.insert_node(0)
    bt.insert_node(10)
    bt.insert_node(20)
    bt.insert_node(30)
    bt.insert_node(40)
    bt.insert_node(50)
    return bt

def test_insert_node(bt):
    assert bt.is_empty() is False

    assert bt.root.value == 0
    assert bt.root.left.value == 10
    assert bt.root.right.value == 20
    assert bt.root.left.left.value == 30
    assert bt.root.left.right.value == 40
    assert bt.root.right.left.value == 50
    assert bt.root.right.right is None

def test_find(bt):
    assert bt.find(20).value == 20
    assert bt.find('hello') is None

def test_last_node(bt):
    assert bt.last_node().value == 50
    new_bt = BinaryTree()
    assert new_bt.last_node() is None

def test_is_empty(bt):
    assert not bt.is_empty()
    new_bt = BinaryTree()
    assert new_bt.is_empty()

def test_delete_node_not_found(bt):
    not_found_message = "Target value not found in the binary tree"
    not_found_return = bt.delete_node('hello')
    assert (
        not_found_return == not_found_message
    ), f'Expected {not_found_message}, received {not_found_return}'

def test_delete_node_empty_tree():
    bt = BinaryTree()
    empty_message = "Binary tree is empty"
    response = bt.delete_node("empty")
    assert response == empty_message, f'Expected {empty_message}, received {response}'

def test_delete_root_node(bt):
    bt.delete_node(0)
    assert bt.root.value == 50
    assert bt.print_tree_bfs() == "Level 1: [50]\nLevel 2: [10, 20]\nLevel 3: [30, 40]"

def test_delete_level_2_node(bt):
    bt.delete_node(20)
    assert bt.find(20) is None
    assert bt.print_tree_bfs() == "Level 1: [0]\nLevel 2: [10, 50]\nLevel 3: [30, 40]"

def test_delete_level_3_node(bt):
    bt.delete_node(30)
    assert bt.find(30) is None
    assert bt.print_tree_bfs() == "Level 1: [0]\nLevel 2: [10, 20]\nLevel 3: [50, 40]"
