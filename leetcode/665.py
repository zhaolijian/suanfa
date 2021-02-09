# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。


class Solution:
    def checkPossibility(self, nums) -> bool:
        length = len(nums)
        change = 0
        for i in range(length - 1):
            if nums[i] > nums[i + 1]:
                change += 1
                # 当出现两次前面比后面大的时候,返回false
                if change > 1:
                    return False
                # 防止i+1及之后的元素都比前面的元素小，但却是非递减序列的情况，比如3412，12是非递减序列，但是却比前面的4都小
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]
        return True