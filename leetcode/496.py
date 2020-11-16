# 下一个更大元素I
# 给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
# nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        d = {}
        len_1, len_2 = len(nums1), len(nums2)
        res = [-1] * len_1
        for i in range(len_2):
            while stack and stack[-1] < nums2[i]:
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for i in range(len_1):
            res[i] = d.get(nums1[i], -1)
        return res