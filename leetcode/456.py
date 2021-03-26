# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
# 注意：n 的值小于15000。


class Solution:
    def find132pattern(self, nums) -> bool:
        length = len(nums)
        if length < 3:
            return False
        # 开始位置到当前位置的最小值数组
        min_array = [nums[0]]
        for i in range(1, length):
            min_array.append(min(nums[i], min_array[-1]))
        stack = []
        for i in range(length - 1, -1, -1):
            while stack and stack[-1] <= min_array[i]:
                stack.pop()

            # nums[i] > stack[-1]：当前值比后面的值大
            # nums[i]最大值、stack中间值、min_array最小值
            if stack and nums[i] > stack[-1]:
                return True
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    s = Solution()
    nums = [3,5,0,3,4]
    print(s.find132pattern(nums))