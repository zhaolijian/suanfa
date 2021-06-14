# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
class Solution:
    def isBalanced(self, root) -> bool:
        def func(node):
            nonlocal res
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left_depth = func(node.left)
            right_depth = func(node.right)
            if abs(left_depth - right_depth) > 1:
                res = False
            return max(left_depth, right_depth) + 1

        res = True
        func(root)
        return res