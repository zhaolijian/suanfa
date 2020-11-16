# 给定一个二叉树，请计算节点值之和最大的路径的节点值之和是多少。
# 这个路径的开始节点和结束节点可以是二叉树中的任意节点

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        if not root:
            return None
        res = float('-inf')

        def func(root):
            nonlocal res
            if not root:
                return 0
            l = func(root.left)
            r = func(root.right)
            res = max(res, l + r + root.val)
            return max(0, max(l, r) + root.val)

        func(root)
        return res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    print(s.maxPathSum(root))