# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
class TreeNode:
    def __init(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 中序遍历
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # 中序排序
        res = float('inf')
        stack = []
        cur = root
        last_val = -1
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            if last_val != -1:
                res = min(res, temp.val - last_val)
            last_val = temp.val
            cur = temp.right
        return res