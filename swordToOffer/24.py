# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     # 返回二维列表，内部每个列表表示找到的路径
#     def FindPath(self, root, expectNumber):
#         if not root:
#             return []
#         result = []
#
#         def FindPathMain(root, path, currentSum):
#             currentSum += root.val
#             path.append(root)
#             if currentSum == expectNumber and root.left is None and root.right is None:
#                 onePath = []
#                 for node in path:
#                     onePath.append(node.val)
#                 result.append(onePath)
#
#             if currentSum < expectNumber:
#                 if root.left:
#                     FindPathMain(root.left, path, currentSum)
#                 if root.right:
#                     FindPathMain(root.right, path, currentSum)
#             path.pop()
#         FindPathMain(root, [], 0)
#         return result


# class Solution:
#     def __init__(self):
#         self.listAll = []
#         self.list = []
#
#     # 返回二维列表，内部每个列表表示找到的路径
#     def FindPath(self, root, expectNumber):
#         if root is None:
#             return self.listAll
#         self.list.append(root.val)
#         expectNumber -= root.val
#         if expectNumber == 0 and root.left is None and root.right is None:
#             self.listAll.append(self.list)
#         self.FindPath(root.left, expectNumber)
#         self.FindPath(root.right, expectNumber)
#         self.list = self.list[:-1]
#         return sorted(self.listAll, key=len, reverse=True)


class Solution:
    def __init__(self):
        self.listAll = []
        self.list = []

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root is None:
            return []
        self.list.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and root.left is None and root.right is None:
            self.listAll.append(self.list)
        self.FindPath(root.left, expectNumber)
        self.FindPath(root.right, expectNumber)
        self.list = self.list[:-1]
        return sorted(self.listAll, key=len, reverse=True)


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(10)
    root.left = TreeNode(5)
    l = root.left
    root.right = TreeNode(12)
    l.left = TreeNode(4)
    l.right = TreeNode(7)
    e = 22
    result = s.FindPath(root, e)
    print(result)