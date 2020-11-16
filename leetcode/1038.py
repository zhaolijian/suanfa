# 给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
class Solution:
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.sum = self.sum + root.val
            root.val = self.sum
            self.bstToGst(root.left)
        return root