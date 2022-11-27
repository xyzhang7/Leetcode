class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def checkEqualTree(root: TreeNode):
    seen = []
    def sum_(node):
        if not node:
            return 0
        seen.append(sum_(node.left) + sum_(node.right) + node.val)
        return seen[-1]
    total = sum_(root)
    seen.pop()
    return total / 2.0 in seen