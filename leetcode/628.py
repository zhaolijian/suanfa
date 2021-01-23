# 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。


# 方法1 排序找出最大的三个数和最小的两个数，O(nlogn)
class Solution:
    def maximumProduct(self, nums) -> int:
        # 三个最大正数乘积
        # 一个最大正数,两个最大负数乘积
        nums.sort()
        return max(nums[-3] * nums[-2] * nums[-1], nums[0] * nums[1] * nums[-1])


# 方法2 线性扫描找出最大的三个数和最小的两个数，O(n)
class Solution:
    def maximumProduct(self, nums) -> int:
        max_number, second_number, third_number = float('-inf'), float('-inf'), float('-inf')
        min_number, min_second_number = float('inf'), float('inf')
        for ele in nums:
            if ele > max_number:
                third_number = second_number
                second_number = max_number
                max_number = ele
            elif ele > second_number:
                third_number = second_number
                second_number = ele
            elif ele > third_number:
                third_number = ele
            if ele < min_number:
                min_second_number = min_number
                min_number = ele
            elif ele < min_second_number:
                min_second_number = ele
        return max(max_number * second_number * third_number, min_number * min_second_number * max_number)