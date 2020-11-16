class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        elif not t2:
            return t1
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    temp = t1.left
    temp.left = TreeNode(5)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    temp1 = t2.left
    temp1.right = TreeNode(4)
    temp2 = t2.right
    temp2.right = TreeNode(7)
    s = Solution()
    print(s.mergeTrees(t1, t2).val)