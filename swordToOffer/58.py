class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot or (pRoot.left is None and pRoot.right is None):
            return True
        return self.isSame(pRoot.left, pRoot.right)

    def isSame(self, l, r):
        if not l and not r:
            return True
        elif (l and (not r)) or (r and (not l)):
            return False
        elif l.val == r.val:
            return self.isSame(l.left, r.right) & self.isSame(l.right, r.left)
        return False
