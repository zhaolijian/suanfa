# 给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = []
        cur = root
        res = 0
        init = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            init.append(temp.val)
            if temp.val > high:
                return res
            if low <= temp.val <= high:
                res += temp.val
            if temp.right:
                cur = temp.right
        return res