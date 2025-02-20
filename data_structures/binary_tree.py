from __future__ import annotations
from data_structures.deque_list import Deque

class Node:
    def __init__(self, value: any, left: Node | None = None, right: Node | None = None, parent: Node | None = None) -> None:
        self._value = value
        self._left = left
        self._right = right
        self._parent = parent
    
    @property
    def value(self) -> any:
        return self._value

    @property
    def parent(self) -> Node | None:
        return self._parent

    @parent.setter
    def parent(self, node: Node) -> None:
        self._parent = node

    @property
    def left(self) -> Node | None:
        return self._left

    @left.setter
    def left(self, node: Node) -> None:
        self._left = node

    @property
    def right(self) -> Node | None:
        return self._right

    @right.setter
    def right(self, node: Node) -> None:
        self._right = node

class BinaryTree:
    def __init__(self) -> None:
        self._root = None

    @property
    def root(self) -> Node | None:
        return self._root

    def print_tree_bfs(self) -> str:
        nodes = self.bfs()
        values = [node.value for node in nodes]
        level = 1
        start = 0
        end = 1
        message = []
        while start < len(values):
            end = min(end, len(values))
            message.append(f'Level {level}: {values[start:end]}')
            start = end
            end = start + 2**level
            level += 1
        return ("\n".join(message))

    def bfs(self) -> list[Node] | None:
        nodes = []
        traversal_queue = Deque()
        traversal_queue.append(self._root)

        while not traversal_queue.is_empty():
            current = traversal_queue.pop_left()
            nodes.append(current)
            if current.left:
                traversal_queue.append(current.left)

            if current.right:
                traversal_queue.append(current.right)

        return nodes

    def insert_node(self, value: any) -> None:
        new_node = Node(value)
        if not self._root:
            self._root = new_node
            return

        traversal_queue = Deque()
        traversal_queue.append(self._root)

        while traversal_queue:
            current = traversal_queue.pop_left()
            if not current.left:
                current.left = new_node
                new_node.parent = current
                return
            traversal_queue.append(current.left)

            if not current.right:
                current.right = new_node
                new_node.parent = current
                return
            traversal_queue.append(current.right)

    def find(self, target: any) -> Node | None:
        nodes = self.bfs()
        for node in nodes:
            if node.value == target:
                return node
        return None

    def last_node(self) -> Node | None:
        if not self._root:
            return None
        return self.bfs()[-1]

    def is_empty(self) -> bool:
        return self._root is None

    def delete_node(self, target: any) -> str | None:
        if self.is_empty():
            return 'Binary tree is empty'

        target_node = self.find(target)
        if target_node is None:
            return 'Target value not found in the binary tree'

        last_node = self.last_node()

        # Target node is not the last node
        if last_node is not target_node:
            # Unlink last node's parent from last_node
            if last_node.parent.left is last_node:
                last_node.parent.left = None
            elif last_node.parent.right is last_node:
                last_node.parent.right = None
            # If target node is the root update the root reference to the last node
            if target_node is self._root:
                self._root = last_node
                last_node.parent = None
            # Update last node's parent
            else:
                last_node.parent = target_node.parent

            # Make last node inherit target_node children.
            last_node.left = target_node.left if target_node.left is not last_node else None
            last_node.right = target_node.right if target_node.right is not last_node else None

            # Update target node's children parent pointer.
            if target_node.left and target_node.left is not last_node:
                target_node.left.parent = last_node
            if target_node.right and target_node.right is not last_node:
                target_node.right.parent = last_node

            # Update target node's parent to point at last node.
            if target_node.parent:
                if target_node.parent.left is target_node:
                    target_node.parent.left = last_node
                elif target_node.parent.right is target_node:
                    target_node.parent.right = last_node

            # Remove all links from target_node.
            target_node.parent, target_node.right, target_node.left = None, None, None

            # Keep tree structure.
            if last_node.right is None and last_node.left is not None:
                last_node.right = last_node.left
                last_node.left = None

        # Target node is the last node
        else:
            # Binary tree only has one node, the root.
            if last_node is self._root:
                self._root = None
            # Target node is not the root.
            else:
                # If target node is a right child, remove the downstream link
                if target_node.parent.right is target_node:
                    target_node.parent.right = None
                # If target node is a left child, remove the downstream link
                else:
                    target_node.parent.left = None
                # Remove upstream link.
                target_node.parent = None
        return None
    
    def print_pre_order_traversal(self) -> str:
        nodes = self.pre_order_traversal()
        values = [node.value for node in nodes]
        print(f"Pre-order: {values}")

    def pre_order_traversal(self) -> list[Node]:
        nodes = []
        def traverse(node: Node | None) -> None:
            if node:
                nodes.append(node)
                traverse(node.left)
                traverse(node.right)
        traverse(self._root)
        return nodes
    
    def print_in_order_traversal(self) -> str:
        nodes = self.in_order_traversal()
        values = [node.value for node in nodes]
        print(f"In-order traversal: {values}")
        
    def in_order_traversal(self) -> list[Node]:
        nodes = []
        def traverse(node: Node | None) -> None:
            if node:
                traverse(node.left)
                nodes.append(node)
                traverse(node.right)
        traverse(self._root)
        return nodes
    
    def print_post_order_traversal(self) -> str:
        nodes = self.post_order_traversal()
        values = [node.value for node in nodes]
        print(f"Post-order traversal: {values}")
    
    def post_order_traversal(self) -> list[Node]:
        nodes = []
        def traverse(node: Node | None) -> None:
            if node:
                traverse(node.left)
                traverse(node.right)
                nodes.append(node)
        traverse(self._root)
        return nodes
