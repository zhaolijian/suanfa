# 判断是否是平衡二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def func(root):
            nonlocal res
            if not root:
                return 0
            l = func(root.left)
            r = func(root.right)
            if abs(l - r) > 1:
                res = False
            return max(l, r) + 1

        res = True
        func(root)
        return res


if __name__ == '__main__':
    s = Solution