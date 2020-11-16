# 已知一棵二叉树，如果选择一个节点，则不能选择与之有连边的节点，那么最多能选择多少个节点
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def func(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        temp1, temp2 = 0, 0
        temp = self.func(root.left) + self.func(root.right)
        if root.left:
            temp1 = self.func(root.left.left) + self.func(root.left.right)
        if root.right:
            temp2 = self.func(root.right.left) + self.func(root.right.right)
        return max(temp1 + temp2 + 1, temp)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    l = root.left
    r = root.right
    l.left = TreeNode(4)
    l.right = TreeNode(5)
    r.left = TreeNode(6)
    r.right = TreeNode(7)
    print(s.func(root))