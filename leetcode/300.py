# 动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        init = [1 for i in range(length)]
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    init[i] = max(init[i], init[j] + 1)
        return max(init)


# 贪心+二分查找
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums) -> int:
        init = []
        length = len(nums)
        for i in range(length):
            if not init or nums[i] > init[-1]:
                init.append(nums[i])
            else:
                l = bisect_left(init, nums[i])
                init[l] = nums[i]
        return len(init)


# class Solution:
#     def lengthOfLIS(self, nums) -> int:
#         # 存储长度为索引值+1的最长上升子序列的末尾值大小
#         # 长度固定的情况下，最长上升子序列的末尾值越小越好
#         init = []
#         for i in range(len(nums)):
#             if not init or nums[i] > init[-1]:
#                 init.append(nums[i])
#             else:
#                 l, r = 0, len(init) - 1
#                 while l < r:
#                     mid = (l + r) // 2
#                     if init[mid] >= nums[i]:
#                         r = mid
#                     else:
#                         l = mid + 1
#                 # l为数组中第一个大于等于n的位置
#                 init[l] = nums[i]
#         return len(init)


if __name__ == '__main__':
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))