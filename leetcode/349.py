# 给定两个数组，编写一个函数来计算它们的交集。

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        res = []
        for ele in s1:
            if ele in s2:
                res.append(ele)
        return res