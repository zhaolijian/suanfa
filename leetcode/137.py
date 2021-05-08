# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
from collections import Counter
class Solution:
    def singleNumber(self, nums) -> int:
        freq = Counter(nums)
        ans = [num for num, occ in freq.items() if occ == 1][0]
        return ans