# 二叉树的最大深度
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1 bfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            res += 1
            next_queue = []
            while queue:
                temp = queue.pop(0)
                if temp.left:
                    next_queue.append(temp.left)
                if temp.right:
                    next_queue.append(temp.right)
            queue = next_queue
        return res


# 或者下面的bfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        array = [root]
        res = 0
        while array:
            res += 1
            for i in range(len(array)):
                temp = array.pop(0)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
        return res


# 方法3 dfs
class Solution:
    def __init__(self):
        self.res = 0

    def maxDepth(self, root: TreeNode) -> int:
        def dfs(root, depth):
            if not root.left and not root.right:
                self.res = max(self.res, depth)
            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)

        if not root:
            return 0
        dfs(root, 1)
        return self.res


# 方法3 递归
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return max(l, r) + 1
