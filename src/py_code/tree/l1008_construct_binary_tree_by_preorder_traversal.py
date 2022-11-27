from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    def recur(preorder):
        n = len(preorder)
        root_val = preorder[0]
        root = TreeNode(root_val, None, None)
        if n == 1:
            return root
        l = 1
        while l < n:
            if preorder[l] > root_val:
                break
            l = l + 1
        root.left = recur(preorder[1:l]) if l > 1 else None
        root.right = recur(preorder[l:n]) if n > l else None
        return root

    return recur(preorder)


if __name__ == '__main__':
    bstFromPreorder([1, 3])
