# 二分法变形
class Solution:
    def searchRange(self, nums, target: int):
        left = self.find(nums, target, True)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        else:
            return [left, self.find(nums, target, False) - 1]

    # 在nums找到target的最左侧/最右侧值
    def find(self, nums, target, bool_val):
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > target or (bool_val and nums[mid] == target):
                r = mid
            else:
                l = mid + 1
        return l

