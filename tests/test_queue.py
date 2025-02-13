import pytest
from data_structures.queue_list import Queue

@pytest.fixture(name="queue")
def queue_fixture() -> Queue:
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue('hello')
    return queue

def test_enqueue(queue: Queue):
    assert queue.size() == 2
    assert queue.peek() == 1

def test_dequeue(queue: Queue):
    assert queue.dequeue() == 1
    assert queue.size() == 1
    assert queue.peek() == 'hello'

def test_peek(queue: Queue):
    assert queue.peek() == 1

def test_is_empty(queue: Queue):
    assert queue.is_empty() is False
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty() is True

def test_empty_dequeue():
    queue = Queue()
    with pytest.raises(IndexError, match="Dequeue from an empty queue"):
        queue.dequeue()

def test_empty_peek():
    queue = Queue()
    with pytest.raises(IndexError, match="Peek from an empty queue"):
        queue.peek()
