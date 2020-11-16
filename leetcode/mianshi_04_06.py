# 设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
# 如果指定节点没有对应的“下一个”节点，则返回null。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1 二分查找
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        cur, res = root, None
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res


# 方法2 使用flag标示该遍历节点是不是p节点的下一个节点
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        def func(root):
            nonlocal flag, res
            if not res and root:
                func(root.left)
                if flag:
                    res = root
                    flag = False
                if root.val == p.val:
                    flag = True
                func(root.right)

        flag, res = False, None
        func(root)
        return res


# 方法3 中序遍历存储所有节点
# class Solution:
#     def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
#         def func(root):
#             if root:
#                 func(root.left)
#                 res.append(root)
#                 func(root.right)
#
#         res = []
#         func(root)
#         length = len(res)
#         for i in range(length):
#             if res[i] == p:
#                 if i == length - 1:
#                     return None
#                 else:
#                     return res[i + 1]
#         return None


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    l = root.left
    l.left = TreeNode(2)
    l.right = TreeNode(4)
    ll =l.left
    ll.left = TreeNode(1)
    p = ll.left
    print(s.inorderSuccessor(root, p))