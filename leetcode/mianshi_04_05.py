# 实现一个函数，检查一棵二叉树是否为二叉搜索树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1 左边值都比根节点值小，右边值都比根节点值大
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(root, min, max):
            if not root:
                return True
            if root.val <= min or root.val >= max:
                return False
            return func(root.left, min, root.val) and func(root.right, root.val, max)

        if not root:
            return True
        # root左边所有节点的范围为(float('-inf'), root.val), 右边所有节点的范围为(root.val, float('inf'))
        return func(root.left, float('-inf'), root.val) and func(root.right, root.val, float('inf'))


# 方法2 中序遍历，是递增序列且无重复值
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(root):
            if root:
                func(root.left)
                res.append(root.val)
                func(root.right)

        res = []
        func(root)
        return res == sorted(set(res))
