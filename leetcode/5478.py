# 你有两个 有序 且数组内元素互不相同的数组 nums1 和 nums2 。
# 一条 合法路径 定义如下：
# 选择数组 nums1 或者 nums2 开始遍历（从下标 0 处开始）。
# 从左到右遍历当前数组。
# 如果你遇到了 nums1 和 nums2 中都存在的值，那么你可以切换路径到另一个数组对应数字处继续遍历（但在合法路径中重复数字只会被统计一次）。
# 得分定义为合法路径中不同数字的和。
# 请你返回所有可能合法路径中的最大得分。
# 由于答案可能很大，请你将它对 10^9 + 7 取余后返回。


class Solution:
    def maxSum(self, nums1, nums2) -> int:
        init = []
        for ele in nums1:
            init.append((ele, 0))
        for ele in nums2:
            init.append((ele, 1))
        init.sort()
        i = 0
        length = len(init)
        res = [0, 0]
        while i < length:
            if i + 1 < length and init[i][0] == init[i + 1][0]:
                res = [max(res) + init[i][0]] * 2
                i += 2
            else:
                res[init[i][1]] += init[i][0]
                i += 1
        return max(res) % (10 ** 9 + 7)


if __name__ == '__main__':
    s = Solution()
    nums1 = [2,4,5,8,10]
    nums2 = [4,6,8,9]
    print(s.maxSum(nums1, nums2))