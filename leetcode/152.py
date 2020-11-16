# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         # 当前位置最大值、最小值
#         m, l = 1, 1
#         # 结果
#         res = float('-inf')
#         for i in range(len(nums)):
#             if nums[i] < 0:
#                 m, l = l, m
#             m = max(m * nums[i], nums[i])
#             l = min(l * nums[i], nums[i])
#             res = max(m, res)
#         return res


class Solution:
    def maxProduct(self, nums) -> int:
        m, l = 1, 1
        res = float('-inf')
        for i in range(len(nums)):
            if nums[i] > 0:
                m = max(nums[i], m * nums[i])
                l = min(nums[i], l * nums[i])
            else:
                temp = m
                m = max(nums[i], l * nums[i])
                l = min(nums[i], temp * nums[i])
            res = max(res, m)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-4,-3,-2]
    print(s.maxProduct(nums))