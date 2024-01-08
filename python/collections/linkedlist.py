from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    val: Any

    next: Node | None


class LinkedList:
    start: Node  # Start points to a sentinal node

    def __init__(self) -> None:
        self.start = Node(val=None, next=None)

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

    def insert(self, val: Any, index: int = 0) -> None:
        i = 0
        curr = self.start.next
        while curr is not None:
            if i == index:
                curr = Node(val=val, next=curr)
                return
            i += 1
            curr = curr.next
        raise IndexError("Provided index out of bounds")

    def pop(self, index: int = 0) -> Any:
        i = -1
        curr = self.start
        while curr.next is not None:
            if i + 1 == index:
                val = curr.next.val
                curr.next = curr.next.next
                return val
        raise IndexError("Provided index out of bounds")

    def push(self, val: Any) -> None:
        curr = self.start
        while curr.next is not None:
            # Iterate until the very last element
            curr = curr.next
        curr.next = Node(val=val, next=None)
