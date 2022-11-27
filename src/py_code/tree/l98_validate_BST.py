import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    stack = []
    prev = -math.inf
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if root.val <= prev:
            return False
        prev = root.val
        root = root.right
    return True

if __name__ == '__main__':
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t2 = TreeNode(2, t1, t3)
    isValidBST(t2)



