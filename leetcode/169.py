import collections


# 方法1
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = collections.Counter(nums)
        for key in temp:
            if temp[key] > len(nums) // 2:
                return key


# 方法2 哈希
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        init = {}
        for i in range(len(nums)):
            if nums[i] in init:
                init[nums[i]] += 1
            else:
                init[nums[i]] = 1
            if init[nums[i]] > len(nums) // 2:
                return nums[i]


# 方法3， 排序
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]