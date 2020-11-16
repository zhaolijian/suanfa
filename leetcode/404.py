# 计算给定二叉树的所有左叶子之和。
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def func(root):
            nonlocal res
            if not root or (not root.left and not root.right):
                return
            if root.left and not root.left.left and not root.left.right:
                res += root.left.val
            if root.left and (root.left.left or root.left.right):
                func(root.left)
            if root.right:
                func(root.right)

        res = 0
        func(root)
        return res