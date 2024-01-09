from __future__ import annotations

from dataclasses import dataclass
from typing import Any, cast


@dataclass
class Node:
    val: Any

    next: Node | None


class LinkedList:
    start: Node  # Start points to a sentinal node
    end: Node
    _size: int

    def __init__(self) -> None:
        self.start = Node(val=None, next=None)
        self.end = Node(val=None, next=None)
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

        i = 0
        curr = self.start
        while curr is not self.end:
            if i == index:
                curr.next = Node(val=val, next=curr.next)
                self._size += 1
                return
            i += 1
            curr = cast(Node, curr.next)
        raise IndexError("Provided index out of bounds")

    def pop(self, index: int = 0) -> Any:
        i = -1
        curr = self.start
        while curr.next is not None:
            if i + 1 == index:
                val = curr.next.val
                curr.next = curr.next.next
                self._size -= 1
                return val
        raise IndexError("Provided index out of bounds")

    def push(self, val: Any, index: int | None = None) -> None:
        self._insert(val, index or self._size)
