# 二叉树的镜像
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root


# 方法2
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return root
            temp = root.left
            root.left = dfs(root.right)
            root.right = dfs(temp)
            return root

        if not root or (not root.left and not root.right):
            return root
        return dfs(root)