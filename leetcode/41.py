# 缺失的第一个正数
# 方法1
# class Solution:
#     def firstMissingPositive(self, nums) -> int:
#         n = len(nums)
#         # 将小于0的值设置为n + 1
#         for i in range(n):
#             if nums[i] <= 0:
#                 nums[i] = n + 1
#
#         # 将值对应的位置的值设置为负数,说明该位置对应的数字出现过
#         for i in range(n):
#             num = abs(nums[i])
#             if num <= n and nums[num - 1] > 0:
#                 nums[num - 1] = -nums[num - 1]
#
#         for i in range(n):
#             if nums[i] > 0:
#                 return i + 1
#         return n + 1


# 方法2 交换
# class Solution:
#     def firstMissingPositive(self, nums) -> int:
#         n = len(nums)
#         for i in range(n):
#             while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
#         for i in range(n):
#             if nums[i] != i + 1:
#                 return i + 1
#         return n + 1

# 交换方法
class Solution:
    def firstMissingPositive(self, nums) -> int:
        length = len(nums)
        for i in range(length):
            while 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1


if __name__ == '__main__':
    s = Solution()
    nums = [3,4,-1,1]
    print(s.firstMissingPositive(nums))