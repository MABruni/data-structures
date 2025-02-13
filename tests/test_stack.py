import pytest
from data_structures.stack_list import Stack

def test_stack_push():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.size() == 2
    assert stack.peek() == 20

def test_stack_pop():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    popped = stack.pop()
    assert popped == 20
    assert stack.size() == 1
    assert stack.peek() == 10

def test_stack_peek():
    stack = Stack()
    stack.push(5)
    assert stack.peek() == 5
    assert stack.size() == 1

def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False

def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="Pop from an empty stack."):
        stack.pop()

def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError, match="Peek from an empty stack."):
        stack.peek()