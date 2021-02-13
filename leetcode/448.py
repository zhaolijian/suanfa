# 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

#
# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             newIndex = abs(nums[i]) - 1
#             if nums[newIndex] >= 0:
#                 nums[newIndex] *= -1
#         res = []
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 res.append(i + 1)
#         return res

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = []
        for ele in nums:
            temp = ele % length - 1
            nums[temp] += length
        for i, ele in enumerate(nums):
            if ele <= length:
                res.append(i + 1)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers(nums))