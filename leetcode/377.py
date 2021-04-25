# 给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
# 题目数据保证答案符合 32 位整数范围。


# dfs+记忆化搜索
class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        nums.sort()
        visisted = {}
        def dfs(target):
            if target in visisted:
                return visisted[target]
            res = 0
            if target == 0:
                return 1
            for i, ele in enumerate(nums):
                if ele <= target:
                    res += dfs(target - ele)
                else:
                    break
            visisted[target] = res
            return res
        return dfs(target)