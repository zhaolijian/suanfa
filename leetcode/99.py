# 二叉搜索树中的两个节点被错误地交换。
# 请在不改变其结构的情况下，恢复这棵树。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法1 中序遍历，使用数组存放中序遍历节点，时间复杂度O(n),空间复杂度O(n)
# class Solution:
#     def __init__(self):
#         self.res = []
#
#     def recoverTree(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#
#         def func(root):
#             if not root:
#                 return
#             func(root.left)
#             self.res.append(root)
#             func(root.right)
#
#         func(root)
#         index = []
#         for i in range(1, len(self.res)):
#             if self.res[i].val < self.res[i - 1].val:
#                 index.append(i)
#                 if len(index) >= 2:
#                     break
#         # 相邻节点交换
#         if len(index) == 1:
#             self.res[index[0] - 1].val, self.res[index[0]].val = self.res[index[0]].val, self.res[index[0] - 1].val
#         # 非相邻节点交换
#         if len(index) == 2:
#             self.res[index[0] - 1].val, self.res[index[1]].val = self.res[index[1]].val, self.res[index[0] - 1].val


# 方法2 中序遍历，只存储异常节点，时间复杂度O(n),空间复杂度O(1)
class Solution:
    def __init__(self):
        self.firstNode = None
        self.firstNodeNext = None
        self.secondNode = None
        self.preNode = TreeNode(float("-inf"))

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.secondNode:
                return
            elif not self.firstNode and self.preNode.val > root.val:
                self.firstNode = self.preNode
                self.firstNodeNext = root
            elif self.firstNode and self.preNode.val > root.val:
                self.secondNode = root
            self.preNode = root
            inorder(root.right)

        inorder(root)
        if not self.secondNode:
            self.firstNode.val, self.firstNodeNext.val = self.firstNodeNext.val, self.firstNode.val
        else:
            self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val


# 方法2的另一种写法
class Solution:
    def __init__(self):
        self.firstNode = None
        self.secondNode = None
        self.preNode = TreeNode(float("-inf"))

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            # 对于第一个满足self.preNode.val > root.val的节点，设置第一个节点为preNode
            if self.firstNode is None and self.preNode.val > root.val:
                self.firstNode = self.preNode
            # 对于任何一个满足self.preNode.val > root.val的节点，设置第二个节点为secondNode
            if self.firstNode and self.preNode.val > root.val:
                self.secondNode = root
            self.preNode = root
            inorder(root.right)

        inorder(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    s = Solution()
    s.recoverTree(root)