# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        cur = root
        res = TreeNode()
        cur_new = res
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            temp = stack.pop()
            cur_new.right = TreeNode(temp.val, None, None)
            cur_new = cur_new.right
            if temp.right:
                cur = temp.right
        return res.right