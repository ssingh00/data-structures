from asyncio.windows_events import NULL
from contextlib import nullcontext


class Node:
    def __init__(self, data) -> None:
        self.data= data
        self.left = None
        self.right = None

class BinaryTree(Node):
    def __init__(self, data) -> None:
        super().__init__(data)
