# 给定一棵二叉搜索树，请找出其中第k大的节点。


# 思路： 中序遍历的逆序
# 方法1
class Solution:
    def kthLargest(self, root, k: int) -> int:
        # 右中左   第k个
        def dfs(node):
            nonlocal k, res
            if not node:
                return
            dfs(node.right)
            k -= 1
            if k == 0:
                res = node.val
                return
            dfs(node.left)

        res = 0
        dfs(root)
        return res


# 方法2
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        res = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            k -= 1
            if k == 0:
                res = cur.val
            cur = cur.left
        return res
