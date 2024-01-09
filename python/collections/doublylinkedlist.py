from __future__ import annotations

from dataclasses import dataclass
from typing import Any, cast


@dataclass
class Node:
    val: Any

    next: Node | None
    prev: Node | None


class DoublyLinkedList:
    start: Node
    end: Node
    _size: int

    def __init__(self) -> None:
        # Construct sentinel nodes
        self.start = Node(val=None, prev=None, next=None)
        self.end = Node(val=None, prev=self.start, next=None)
        self.start.next = self.end
        self._size = 0

    def size(self) -> int:
        return self._size

    def index(self, val) -> int:
        """Gives the index of the first occurance of value

        @param val {Any} The value to look find
        """
        i = 0
        curr = self.start.next
        while curr is not None:
            if curr.val == val:
                return i

            i += 1
            curr = curr.next
        return -1

    def _insert(self, val: Any, index: int = 0) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Provided index out of bounds")

        i = -1
        curr = self.start
        while curr is not None:
            if i == index:
                new_node = Node(val=val, next=curr, prev=curr.prev)
                cast(Node, curr.prev).next = new_node
                if curr.next is not None:
                    curr.next.prev = new_node
                self._size += 1
                return
            i += 1
            curr = cast(Node, curr.next)
        raise IndexError("Provided index out of bounds")

    def pop(self, index: int = 0) -> Any:
        if index < 0 or index > self._size - 1:
            raise IndexError("Provided index out of bounds")

        i = 0
        curr: Node = cast(Node, self.start.next)
        while curr is not self.end:
            if i == index:
                val = curr.val
                # curr.prev will at least be the start sentinel
                cast(Node, curr.prev).next = curr.next
                # curr.next will at most be the end sentinel
                cast(Node, curr.next).prev = curr.prev
                self._size -= 1
                return val
            curr = cast(Node, curr.next)
        raise IndexError("Provided index out of bounds")

    def push(self, val: Any, index: int | None = None) -> None:
        self._insert(val, index or self._size)
