class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def func(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 1
            l = func(root.left)
            r = func(root.right)
            return max(l, r) + 1

        if not root or (not root.left and not root.right):
            return True
        cha = abs(func(root.left) - func(root.right))
        if cha > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)