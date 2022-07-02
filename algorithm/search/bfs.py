class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left= None
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None

    def bfs(self):
        currentNode  = self.root
        lst  = []
        qu = []
        qu.push(currentNode)
        while(len(qu) > 0):
            currentNode = qu.pop()