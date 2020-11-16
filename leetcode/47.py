# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
class Solution:
    def permuteUnique(self, nums):
        def dfs(index, already, array):
            nonlocal length
            if index == length:
                res.append(already)
                return
            for i in range(len(array)):
                if i - 1 >= 0 and array[i] == array[i - 1]:
                    continue
                dfs(index + 1, already + [array[i]], array[: i] + array[i + 1:])

        if not nums:
            return []
        length = len(nums)
        nums.sort()
        res = []
        dfs(0, [], nums)
        return list(map(list, res))

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    print(s.permuteUnique(nums))