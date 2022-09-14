from trees import TreeNode, BinaryTree
from typing import Optional, List


def levelOrderBottom(root: Optional[TreeNode]) -> List[List[int]]:
    ans = []

    def recur_helper(node, level):
        if not node:
            return
        if len(ans) == level:
            ans.append([])
        recur_helper(node.left, level + 1)
        recur_helper(node.right, level + 1)
        ans[len(ans) - level - 1].append(node.val)

    recur_helper(root, 0)
    return ans

if __name__ == "__main__":
    btree = BinaryTree([3,9,20,None,None,15,7]).root
    levelOrderBottom(btree)