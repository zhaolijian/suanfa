# 给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
# 换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
# 以数组形式返回答案。

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        # 每个值的数量
        init = [0] * 101
        # 比该位置小的值的数量
        array = [0] * 101
        res = []
        for ele in nums:
            init[ele] += 1
        for i in range(1, 101):
            array[i] = array[i - 1] + init[i - 1]
        for ele in nums:
            res.append(array[ele])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [8,1,2,2,3]
    print(s.smallerNumbersThanCurrent(nums))