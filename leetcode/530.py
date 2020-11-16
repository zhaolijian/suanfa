# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

# 中序遍历
# 方法1： 得到中序遍历数组
class Solution:
    def getMinimumDifference(self, root) -> int:
        array = []
        res = float('inf')
        def mid(root):
            if not root:
                return
            mid(root.left)
            array.append(root.val)
            mid(root.right)
        mid(root)
        for i in range(1, len(array)):
            res = min(res, array[i] - array[i - 1])
        return res

# 方法2 空间优化，只保留前一个节点值
class Solution:
    def getMinimumDifference(self, root) -> int:
        res = float('inf')
        pre = -1
        def func(root):
            nonlocal res, pre
            if not root:
                return
            func(root.left)
            if pre != -1:
                res = min(res, root.val - pre)
            pre = root.val
            func(root.right)
        func(root)
        return res