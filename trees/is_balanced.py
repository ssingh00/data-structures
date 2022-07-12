# Definition for a binary tree node.
from typing import Optional
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
        return build(lst)

    def printpreorder(self, root):
        if root is None:
            return
        print (root.val,end=' ')
        self.printInorder(root.left)
        self.printInorder(root.right)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maximum(root, i):
            if root is None:
                return i
            return max(maximum(root.left, i+1), maximum(root.right, i+1))

        def recurse(root):
            if root is None:
                return True
            # The max length of each subbranch. Their difference must be 1 or less or exit.
            lbranch = maximum(root.left, 0)
            rbranch = maximum(root.right, 0)
            if abs(lbranch-rbranch) > 1:
                return False
            return recurse(root.left) and recurse(root.right)
        
        return recurse(root)
if __name__=="__main__":
    root = [3,9,20,null,null,15,7]
    sl = Solution()
    print("<<<------------------------>>>")
    print(sl.isBalanced(root))