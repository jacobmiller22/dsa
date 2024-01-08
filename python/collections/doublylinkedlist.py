from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    val: Any

    next: Node | None
    prev: Node | None


class DoublyLinkedList:
    start: Node
    end: Node

    def __init__(self) -> None:
        # Construct sentinel nodes
        self.start = Node(val=None, prev=None, next=None)
        self.end = Node(val=None, prev=self.start, next=None)
        self.start.next = self.end
