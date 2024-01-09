from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    val: Any

    next: Node | None


class Queue:
    start: Node | None
    _size: int

    def __init__(self) -> None:
        self.start = None
        self._size = 0

    def push(self, val: Any) -> None:
        self.start = Node(val=val, next=self.start)
        self._size += 1

    def pop(self, val: Any) -> None:
        if self.start is None:
            return

        val = self.start.val
        self._size -= 1

        self.start = self.start.next
        return val

    def peek(self) -> Any:
        if self.start is None:
            return

        return self.start.val

    def size(self) -> int:
        return self._size
