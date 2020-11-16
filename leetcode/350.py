# 两个数组的交集 II

# 方法1 使用collections.Counter
import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        one = collections.Counter(nums1)
        two = collections.Counter(nums2)
        res = []
        for key in one.keys():
            if key in two.keys():
                res += min(one[key], two[key]) * [key]
        return res


# 方法2 先排序
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        len_1, len_2 = len(nums1), len(nums2)
        i, j = 0, 0
        res = []
        while i < len_1 and j < len_2:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return res