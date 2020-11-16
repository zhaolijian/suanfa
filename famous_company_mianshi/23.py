# 给定一个二叉树和一个值\ sum sum，判断是否有从根节点到叶子节点的节点值之和等于\ sum sum 的路径

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = False

    def hasPathSum(self, root, sum):
        def func(root, value):
            if not root:
                return
            if not root.left and not root.right and root.val == value:
                self.res = True
                return
            if root.left:
                func(root.left, value - root.val)
            if root.right:
                func(root.right, value - root.val)

        func(root, sum)
        return self.res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(s.hasPathSum(root, 0))