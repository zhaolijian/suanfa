# 给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def func(root, sum, array):
            if not root:
                return
            if not root.left and not root.right and sum == root.val:
                array.append(root.val)
                res.append(array)
                return
            func(root.left, sum - root.val, array + [root.val])
            func(root.right, sum - root.val, array + [root.val])

        res = []
        func(root, sum, [])
        return res