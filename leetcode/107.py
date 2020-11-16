# 给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []
        res = []
        array = deque([root])
        while array:
            cur = []
            for i in range(len(array)):
                temp = array.popleft()
                cur.append(temp.val)
                if temp.left:
                    array.append(temp.left)
                if temp.right:
                    array.append(temp.right)
            res.append(cur)
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    r = root.right
    r.left = TreeNode(15)
    r.right = TreeNode(7)
    print(s.levelOrderBottom(root))