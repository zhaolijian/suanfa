# 最小高度树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def func(start, end):
            if start > end:
                return
            mid = (start + end) // 2
            root = TreeNode(nums[mid])
            root.left = func(start, mid - 1)
            root.right = func(mid + 1, end)
            return root
        if not nums:
            return None
        length = len(nums)
        return func(0, length - 1)
