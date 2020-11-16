# t2是否是t1的子结构
class Solution:
    def isContains(self, root1, root2):
        def func(r1, r2):
            if not r2:
                return True
            if not r1:
                return False
            if r1.val != r2.val:
                return False
            return func(r1.left, r2.left) and func(r1.right, r2.right)

        if not root2:
            return True
        if not root1:
            return False
        if func(root1, root2):
            return True
        return self.isContains(root1.left, root2) or self.isContains(root1.right, root2)


# 给定彼此独立的两棵二叉树，判断 t1 树是否有与 t2 树拓扑结构完全相同的子树。
class Solution:
    def isContains(self, root1, root2):
        def func(r1, r2):
            if not r1 and not r2:
                return True
            elif not r1 or not r2 or r1.val != r2.val:
                return False
            return func(r1.left, r2.left) and func(r1.right, r2.right)

        if not root2:
            return True
        if not root1:
            return False
        if func(root1, root2):
            return True
        return self.isContains(root1.left, root2) or self.isContains(root1.right, root2)