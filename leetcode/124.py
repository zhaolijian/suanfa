class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = float('-inf')
        
    def maxPathSum(self, root) -> int:
        def func(root):
            if not root:
                return 0
            left = max(func(root.left), 0)
            right = max(func(root.right), 0)
            self.res = max(self.res, root.val + left + right)
            return root.val + max(left, right)
        func(root)
        return self.res if self.res != float('-inf') else 0


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.maxPathSum(root))