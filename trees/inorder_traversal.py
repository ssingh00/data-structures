# Definition for a binary tree node.

from typing import List, Optional
from sqlalchemy import null


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def convert_preorder_list_to_bt(self, lst):
        def build(lst):
            if len(lst) == 0:
                return None
            if len(lst) == 1:
                return TreeNode(lst[0])
            mid  = int(len(lst)/2)
            left  = lst[0:mid]
            right = lst[mid+1::]
            return TreeNode(lst[mid], build(left), build(right))
        return build(lst)

    def printInorder(self, root):
        if root is None:
            return
        self.printInorder(root.left)
        print (root.val,end=' ')
        self.printInorder(root.right)



class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        bt = BinaryTree()
        root  = bt.convert_preorder_list_to_bt(root)
        bt.printInorder(root)
        stack = []
        def traverse(root):
            if not root:
                return None
            traverse(root.left)
            stack.append(root.val)
            traverse(root.right)

        traverse(root)
        return stack



if __name__=="__main__":
    root = [1,null,2,3]
    sl = Solution()
    print("<<<------------------------>>>")
    print(sl.inorderTraversal(root))