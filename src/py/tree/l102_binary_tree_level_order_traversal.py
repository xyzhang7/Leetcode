from trees import TreeNode, BinaryTree
from typing import Optional, List


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    ans = []

    def recur_helper(node, level):
        if not node:
            return
        if len(ans) == level:
            ans.append([node.val])
        else:
            ans[level].append(node.val)
        recur_helper(node.left, level + 1)
        recur_helper(node.right, level + 1)

    recur_helper(root, 0)
    return ans

if __name__ == "__main__":
    btree = BinaryTree([1, 2, 3, 4, 5]).root
    levelOrder(btree)