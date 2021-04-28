# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1
class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 返回的是节点数量
        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)
            if l + r + 1 > self.res:
                self.res = l + r + 1
            return max(l, r) + 1

        if not root or (not root.left and not root.right):
            return 0
        dfs(root)
        return self.res - 1



# 方法2
class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def func(root):
            if not root or (not root.left and not root.right):
                return 0
            res = 0
            left_val = func(root.left)
            right_val = func(root.right)
            if root.left:
                res += 1 + left_val
            if root.right:
                res += 1 + right_val
            self.result = max(self.result, res)
            if not root.left:
                return 1 + right_val
            if not root.right:
                return 1 + left_val
            return max(left_val, right_val) + 1

        # 返回的是边数量
        func(root)
        return self.result
