# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: TreeNode):
        def func(root, array):
            if not root.left and not root.right:
                array += [str(root.val)]
                self.res.append('->'.join(array))
                return
            if root.left:
                func(root.left, array + [str(root.val)])
            if root.right:
                func(root.right, array + [str(root.val)])

        if not root:
            return []
        func(root, [])
        return self.res


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    l = root.left
    l.left = TreeNode(4)
    l.right = TreeNode(5)
    r = root.right
    r.right = TreeNode(7)
    print(s.binaryTreePaths(root))