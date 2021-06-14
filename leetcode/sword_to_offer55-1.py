# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。


# 方法1 dfs
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, depth):
            nonlocal res
            if not node:
                res = max(res, depth)
                return
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        res = 0
        dfs(root, 0)
        return res


# 方法2 层次遍历
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        array = [root]
        while array:
            res += 1
            for i in range(len(array)):
                temp = array.pop(0)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
        return res
