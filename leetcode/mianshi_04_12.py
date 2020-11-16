# 给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。
# 注意，路径不一定非得从二叉树的根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.path(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def path(self, root, sum):
        if not root:
            return 0
        res = 0
        if root.val == sum:
            res += 1
        res += self.path(root.left, sum - root.val)
        res += self.path(root.right, sum - root.val)
        return res
