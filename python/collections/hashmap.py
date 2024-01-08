from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List


@dataclass
class Node:
    key: Any
    val: Any

    next: Node | None


class HashMap:
    capacity: int  # number of buckets
    size: int
    load_factor: float
    items: List[Node | None]

    def __init__(self, capacity: int = 16, load_factor: float = 0.75) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.items: List[Node | None] = [None] * self.capacity
        self.size: int = 0

    def resize(self):
        self.capacity *= 2
        new_items: List[Node | None] = [None] * self.capacity
        for node in self.items:
            if node is None:
                continue

            # Add the nodes in this linked list to the new items list
            # ensuring that the list is built up in the case of collision
            # within the new list
            curr = node
            while curr is not None:
                index = hash(curr.key) % self.capacity
                if new_items[index] is None:
                    new_items[index] = Node(key=curr.key, val=curr.val, next=None)
                else:
                    new_items[index] = Node(
                        key=curr.key, val=curr.val, next=new_items[index]
                    )
                curr = curr.next

    def _get_node(self, key: Any) -> Node | None:
        index: int = hash(key) % self.capacity
        node: Node | None = self.items[index]

        if node is None:
            return None

        if node.next is None:
            return node

        # Find node in collision linked list
        curr = node
        while curr is not None:
            if curr.key == key:
                return node
            curr = curr.next

    def get(self, key: Any) -> Any:
        node: Node | None = self._get_node(key)

        if node is None:
            return None

        return node.val

    def put(self, key: Any, val: Any):
        node: Node | None = self._get_node(key)

        index = hash(key) % self.capacity

        if node is None:
            self.items[index] = Node(key=key, val=val, next=None)
        else:
            node.val = val  # Update the value of the node

        self.size += 1

        if self.size > self.load_factor * self.capacity:
            self.resize()
