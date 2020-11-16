# 幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。
# 前缀和
class Solution:
    def subsets(self, nums):
        def func(index, array):
            nonlocal length
            res.append(array + [nums[index]])
            for i in range(index + 1, length):
                func(i, array + [nums[index]])

        res = [[]]
        length = len(nums)
        for i in range(length):
            func(i, [])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))