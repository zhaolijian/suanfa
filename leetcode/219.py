# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

# 方法1 最好的方法
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, ele in enumerate(nums):
            if ele in d and i - d[ele] <= k:
                return True
            d[ele] = i
        return False


# 方法2
from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i, ele in enumerate(nums):
            d[ele].append(i)
        for key in d:
            l = d[key]
            if len(l) >= 2:
                for i in range(1, len(l)):
                    if l[i] - l[i - 1] <= k:
                        return True
        return False