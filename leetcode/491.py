# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

# 方法1
class Solution:
    def findSubsequences(self, nums):
        def dfs(nums, already):
            if len(already) >= 2:
                res.append(already)
            s = set()
            for index, val in enumerate(nums):
                if val not in s and (not already or val >= already[-1]):
                    dfs(nums[index + 1:], already + [val])
                    s.add(val)
        res = []
        dfs(nums, [])
        return res



# 方法2 比较复杂，好理解
# class Solution:
#     def findSubsequences(self, nums):
#         def dfs(nums, already):
#             if (tuple(nums), tuple(already)) not in visited:
#                 if not nums:
#                     if len(already) >= 2 and tuple(already) not in res:
#                         res.add(tuple(already))
#                     return
#                 if not already:
#                     dfs(nums[1:], already)
#                     dfs(nums[1:], already + [nums[0]])
#                 else:
#                     for i in range(len(nums)):
#                         if nums[i] >= already[-1]:
#                             dfs(nums[i + 1:], already + [nums[i]])
#                         dfs(nums[i + 1:], already)
#             visited.add((tuple(nums), tuple(already)))
#
#         length = len(nums)
#         visited = set()
#         res = set()
#         for i in range(length):
#             dfs(nums[i:], [])
#         return list(map(list, res))


if __name__ == '__main__':
    s = Solution()
    nums = [4,4,6,7,7]
    print(s.findSubsequences(nums))