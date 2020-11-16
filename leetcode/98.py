# 验证二叉搜索树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(node, min_value, max_value):
            if not node:
                return True
            if node.val <= min_value or node.val >= max_value:
                return False
            return func(node.left, min_value, node.val) and func(node.right, node.val, max_value)

        return func(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    l = root.left
    l.left = TreeNode(0)
    l.right = TreeNode(2)
    r = root.right
    r.left = TreeNode(4)
    r.right = TreeNode(6)
    print(s.isValidBST(root))