# 将有序数组转化为高度平衡二叉搜索树（一个高度平衡二叉树是指一个二叉树每个节点的左右两个子树的高度差的绝对值不超过 1。）
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 思路：中间位置节点作为根节点，左边部分归左子树，右边部分归右子树，所以是高度平衡的
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def func(start, end):
            if start > end:
                return None
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = func(start, mid - 1)
            root.right = func(mid + 1, end)
            return root
        return func(0, len(nums) - 1)