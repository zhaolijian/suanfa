# 首个共同祖先
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 这个思路值得学习
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # 说明p，q两个节点左右子树一边一个
        if l and r:
            return root
        # 说明p、q两个节点在同一侧
        return l if l else r