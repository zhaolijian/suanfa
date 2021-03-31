# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
# 注意：n 的值小于15000。


class Solution:
    def find132pattern(self, nums) -> bool:
        # 到当前为止的最小值
        min_array = [nums[0]]
        length = len(nums)
        for i in range(1, length):
            min_array.append(min(min_array[-1], nums[i]))
        # 栈中存放次小值
        stack = []
        # nums[i]作为最大值
        for i in range(length - 1, -1, -1):
            # 保证了栈中的次小值大于最小值
            while stack and stack[-1] <= min_array[i]:
                stack.pop()
            # 如果遍历值大于栈中的次小值,并且上面的while循环保证了次小值大于最小值,则返回true
            if stack and nums[i] > stack[-1]:
                return True
            # 栈为空或者nums[i]<=stack[-1]的情况,所以栈中存放的是递减序列
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [3,5,0,3,4]
    print(s.find132pattern(nums))