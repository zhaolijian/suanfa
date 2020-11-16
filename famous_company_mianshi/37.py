# 给定彼此独立的两棵二叉树，判断 t1 树是否有与 t2 树拓扑结构完全相同的子树。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isContains(self , root1 , root2 ):
        # write code here
        def check(root1, root2):
            if not root1:
                return not root2
            if not root2:
                return not root1
            if root1.val != root2.val:
                return False
            return check(root1.left, root2.left) and check(root1.right, root2.right)
        if not root2:
            return True
        if not root1:
            return False
        if check(root1, root2):
            return True
        return self.isContains(root1.left, root2) or self.isContains(root1.right, root2)


# class Solution:
#     def __init__(self):
#         self.flag = False
#
#     def isContains(self, root1, root2):
#         # write code here
#         if not root2:
#             return True
#
#         def equals(r1, r2):
#             if not r1 and not r2:
#                 return True
#             if not r1 or not r2 or (r1.val != r2.val):
#                 return False
#             return equals(r1.left, r2.left) and equals(r1.right, r2.right)
#
#         def find(root1, root2):
#             if not root1:
#                 return
#             if root1.val == root2.val:
#                 if equals(root1, root2):
#                     self.flag = True
#             find(root1.left, root2)
#             find(root1.right, root2)
#
#         find(root1, root2)
#         return self.flag


if __name__ == '__main__':
    s = Solution()
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    l = root1.left
    r = root1.right
    l.left = TreeNode(4)
    l.right = TreeNode(5)
    r.left = TreeNode(6)
    r.right = TreeNode(7)
    lr = l.right
    lr.left = TreeNode(8)
    lr.right = TreeNode(9)

    root2 = TreeNode(2)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)
    r2 = root2.right
    r2.left = TreeNode(8)
    r2.right = TreeNode(9)
    print(s.isContains(root1, root2))