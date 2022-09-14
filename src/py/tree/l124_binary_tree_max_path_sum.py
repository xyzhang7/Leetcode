from trees import TreeNode, BinaryTree
from typing import Optional


def maxPathSum(root: Optional[TreeNode]) -> int:
    def max_gain(src):
        curr = 0
        if not src:
            return 0
        left_gain = max_gain(src.left)
        right_gain = max_gain(src.right)
        if src.val > 0:
            curr += src.val
        if left_gain > 0:
            curr += left_gain
        if right_gain > 0:
            curr += right_gain
        return curr

    return max_gain(root)


if __name__ == "__main__":
    l = [-10, 9, 20, None, None, 15, 7]
    maxPathSum(BinaryTree(l).root)

