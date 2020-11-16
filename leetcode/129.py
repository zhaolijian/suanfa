class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1 深度优先遍历
class Solution:
    def __init__(self):
        self.res = 0

    def sumNumbers(self, root: TreeNode) -> int:
        def func(root, temp):
            if not root:
                return
            if not root.left and not root.right:
                self.res += (10 * temp + root.val)
            func(root.left, 10 * temp + root.val)
            func(root.right, 10 * temp + root.val)

        func(root, 0)
        return self.res


# 方法2 广度优先遍历
class Solution:
    def __init__(self):
        self.res = 0
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        array = [(root, 0)]
        while array:
            node, val = array.pop()
            if not node.left and not node.right:
                self.res += val * 10 + node.val
            if node.left:
                array.append((node.left, val * 10 + node.val))
            if node.right:
                array.append((node.right, val * 10 + node.val))
        return self.res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(s.sumNumbers(root))