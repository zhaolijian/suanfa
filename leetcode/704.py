# 二分查找
class Solution:
    def search(self, nums, target: int) -> int:
        def solu(left, right):
            nonlocal res
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
            if left < mid:
                solu(left, mid - 1)
            if mid < right:
                solu(mid + 1, right)

        length = len(nums)
        res = -1
        solu(0, length - 1)
        return res