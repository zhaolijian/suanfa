# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def reConstructBinaryTree(self, pre, tin):
#         if len(pre) == 0 or len(tin) == 0:
#             return None
#         root = TreeNode(pre.pop(0))
#         index = tin.index(root.val)
#         root.left = self.reConstructBinaryTree(pre, tin[:index])
#         root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
#         return root

# 根据后序和中序构造
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, last, tin):
        if not last or not tin:
            return None
        root = TreeNode(last.pop(-1))
        index = tin.index(root.val)
        root.right = self.reConstructBinaryTree(last, tin[index + 1:])
        root.left = self.reConstructBinaryTree(last, tin[:index])
        return root


if __name__ == '__main__':
    s = Solution()
    # pre = [1, 2, 4, 7, 3, 5, 6, 8]
    last = [7, 4, 2, 5, 8, 6, 3, 1]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    r = s.reConstructBinaryTree(last, tin)
    print(r)

