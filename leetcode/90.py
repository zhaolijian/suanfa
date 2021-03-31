# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。


# dfs
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        s = set()
        def dfs(nums, already):
            if tuple(already) not in s:
                s.add(tuple(already))
            if nums:
                dfs(nums[1:], already + [nums[0]])
                dfs(nums[1:], already)

        dfs(nums, [])
        return list(map(list, s))


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,2]
    print(s.subsetsWithDup(nums))