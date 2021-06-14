# 一个长度为n的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n之内。在范围0～n内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid
        return l