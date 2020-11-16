# # 方法1，先排序再遍历
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         nums.sort()
#         res = 1
#         temp = 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1] + 1:
#                 temp += 1
#                 res = max(res, temp)
#             elif nums[i] == nums[i - 1]:
#                 continue
#             else:
#                 temp = 1
#         return res


# 方法2 哈希
class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        init = set(nums)
        res = 0
        for ele in nums:
            if ele - 1 not in init:
                temp = 1
                while ele + 1 in init:
                    temp += 1
                    ele += 1
                res = max(res, temp)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [100,4,200,1,3,2]
    print(s.longestConsecutive(nums))