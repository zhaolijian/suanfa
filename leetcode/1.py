# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


# 方法1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, number in enumerate(nums):
            if target - number in d:
                return [d[target - number], i]
            d[number] = i


# 方法2
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        for key in d:
            if target - key == key and len(d[key]) >= 2:
                return sorted([d[key][0], d[key][1]])
            if target - key != key and target - key in d:
                return sorted([d[key][0], d[target - key][0]])