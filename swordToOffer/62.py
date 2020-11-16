class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     # 返回对应节点TreeNode
#     def KthNode(self, pRoot, k):
#         if not pRoot or k <= 0:
#             return None
#         stack = []
#         count = 0
#         while pRoot or stack:
#             if pRoot:
#                 stack.append(pRoot)
#                 pRoot = pRoot.left
#             else:
#                 pRoot = stack.pop(-1)
#                 count += 1
#                 if count == k:
#                     return pRoot
#                 pRoot = pRoot.right
#         return None

# class Solution:
#     # 返回对应节点TreeNode
#     def KthNode(self, pRoot, k):
#         if not pRoot or not k:
#             return None
#         res = []
#
#         def Traversal(node):
#             if len(res) >= k or not node:
#                 return None
#             Traversal(node.left)
#             res.append(node)
#             Traversal(node.right)
#         Traversal(pRoot)
#         if len(res) < k:
#             return None
#         return res[k - 1]


class Solution:
    def __init__(self):
        self.array = []

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot or k <= 0:
            return None
        self.midTraversal(pRoot, k)
        if len(self.array) >= k:
            return self.array[k - 1]
        return None

    def midTraversal(self, pRoot, k):
        if len(self.array) >= k or not pRoot:
            return
        self.midTraversal(pRoot.left, k)
        self.array.append(pRoot)
        self.midTraversal(pRoot.right, k)


if __name__ == '__main__':
    s = Solution()
    pRoot = TreeNode(8)
    pRoot.left = TreeNode(6)
    pRoot.right = TreeNode(10)
    l = pRoot.left
    r = pRoot.right
    l.left = TreeNode(5)
    l.right = TreeNode(7)
    r.left = TreeNode(9)
    r.right = TreeNode(11)
    l = s.KthNode(pRoot, 4)
    print(l.val)