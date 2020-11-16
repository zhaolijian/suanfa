class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_numebr, length = sum(nums), len(nums)
        if sum_numebr % 2 != 0:
            return False
        else:
            avg = sum_numebr // 2
            # 只要nums中有元素可以组成avg即可
            init = [[False for i in range(avg + 1)] for j in range(length)]
            for i in range(avg + 1):
                if nums[0] == i:
                    init[0][i] = True
            for i in range(1, length):
                for j in range(avg + 1):
                    if nums[i] == j:
                        init[i][j] = True
                    else:
                        init[i][j] = init[i - 1][j] or init[i - 1][j - nums[i]]
            return init[-1][-1]

if __name__ == '__main__':
    s = Solution()
    nums = [1,5,11,5]
    print(s.canPartition(nums))