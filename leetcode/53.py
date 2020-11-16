# 方法一：动态规划
# class Solution:
#     def maxSubArray(self, nums: 'List[int]') -> int:
#         # result存储最大值，sum只管往后加，当变成负数就不往后加了，转而指向下一个数
#         result = nums[0]
#         sum = 0
#         for num in nums:
#             if sum > 0:
#                 sum += num
#             else:
#                 sum = num
#             result = max(result, sum)
#         return result


# 方法二：分治法
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            max_l = self.maxSubArray(nums[0: len(nums) // 2])
            max_r = self.maxSubArray(nums[len(nums) // 2: len(nums)])
        temp = 0
        max_1 = nums[len(nums) // 2 - 1]
        for i in range(len(nums) // 2 - 1, -1, -1):
            temp += nums[i]
            max_1 = max(max_1, temp)
        temp = 0
        max_2 = nums[len(nums) // 2]
        for j in range(len(nums) // 2, len(nums)):
            temp += nums[j]
            max_2 = max(max_2, temp)
        return max(max_l, max_r, max_1 + max_2)


if __name__ == '__main__':
    s = Solution()
    ans = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(ans)

