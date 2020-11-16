# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 方法1 bfs 最快
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = deque([(root, 1)])
        res = float('inf')
        while d:
            node, val = d.popleft()
            if not node.left and not node.right:
                res = min(res, val)
            if node.left:
                d.append((node.left, val + 1))
            if node.right:
                d.append((node.right, val + 1))
        return res


# 方法2 dfs
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = float('inf')
        def func(node, depth):
            nonlocal res
            if not node.left and not node.right:
                res = min(res, depth)
                return
            if node.left:
                func(node.left, depth + 1)
            if node.right:
                func(node.right, depth + 1)

        func(root, 1)
        return res


# 方法3 dfs
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        res = float('inf')
        if root.left:
            res = min(res, self.minDepth(root.left))
        if root.right:
            res = min(res, self.minDepth(root.right))
        return res + 1


