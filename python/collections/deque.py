from __future__ import annotations

from dataclasses import dataclass
from typing import Any, cast


@dataclass
class Node:
    val: Any

    next: Node | None
    prev: Node | None


class Dequeue:
    start: Node
    end: Node
    _size: int

    def __init__(self) -> None:
        self.start = Node(val=None, next=None, prev=None)
        self.end = Node(val=None, next=None, prev=self.start)
        self.start.next = self.end
        self._size = 0

    def push(self, val: Any) -> None:
        new_node = Node(val=val, next=self.start.next, prev=self.start)
        self.start.next = new_node
        cast(Node, new_node.next).prev = new_node
        self._size += 1

    def pop(self) -> Any:
        if self.end.prev is self.start:
            return
        val = cast(Node, self.end.prev).val
        cast(Node, cast(Node, self.end.prev).prev).next = self.end

        self._size -= 1
        return val

    def peek(self) -> Any:
        return cast(Node, self.end.prev).val

    def size(self) -> int:
        return self._size
