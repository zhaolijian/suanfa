# class Solution:
#     def __init__(self):
#         self.res = []
#
#     def subsets(self, nums):
#         # 回溯算法
#         self.func([], nums)
#         return self.res
#
#     # 之前的字符串,后接字符串
#     def func(self, array, nums):
#         self.res.append(array)
#         for i in range(len(nums)):
#             self.func(array + [nums[i]], nums[i + 1:])
#         return
#
#
# if __name__ == '__main__':
#     s = Solution()
#     nums = list(map(int, input().split()))
#     print(s.subsets(nums))


class Solution:
    def subsets(self, nums):
        def func(nums, already):
            nonlocal res
            res.append(already)
            if not nums:
                return
            for i, ele in enumerate(nums):
                func(nums[i + 1:], already + [ele])

        res = []
        nums.sort()
        func(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))