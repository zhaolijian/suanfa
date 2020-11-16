# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 首先判断A中是不是有B的根节点，如果没有，直接返回False
# 如果有，则判断A中的子树和B是否一样
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not pRoot1 or not pRoot2:
            return False
        else:
            return self.isSame(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def isSame(self, pRoot1, pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val == pRoot2.val:
            return self.isSame(pRoot1.left, pRoot2.left) and self.isSame(pRoot1.right, pRoot2.right)
        else:
            return False


if __name__ == '__main__':
    head = TreeNode(8)
    cur = head
    cur.left = TreeNode(8)
    cur.right = TreeNode(7)
    l = cur.left
    l.left = TreeNode(9)
    l.right = TreeNode(2)
    r = l.right
    r.left = TreeNode(4)
    r.right = TreeNode(7)
    s = Solution()

    t2 = TreeNode(8)
    t2.left = TreeNode(9)
    t2.right = TreeNode(2)
    print(s.HasSubtree(head, t2))


