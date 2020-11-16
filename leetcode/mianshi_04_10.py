# 判断t2是不是t1的子树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def func(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            return func(t1.left, t2.left) and func(t1.right, t2.right)

        if (not t1 and not t2) or not t2:
            return True
        elif not t1:
            return False
        else:
            if t1.val == t2.val and func(t1, t2):
                return True
            else:
                return self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)