from typing import Optional, List
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, arr: List[int]):
        self.root = None
        n = len(arr)
        nodes = [None]
        for i in arr:
            if i is not None:
                nodes.append(TreeNode(val=i))
            else:
                nodes.append(None)
        for i in range(1, n + 1):
            if nodes[i]:
                nodes[i].left = nodes[2 * i] if 2 * i < n else None
                nodes[i].right = nodes[2 * i + 1] if (2 * i + 1 < n) else None
        self.root = nodes[1]
