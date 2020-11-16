# 下一个更大元素II
# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
# 数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
# 如果不存在，则输出 -1。

class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        length = len(nums)
        nums *= 2
        res = [-1] * length
        stack = []
        for i in range(2 * length):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop() % length] = nums[i]
            stack.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,1]
    print(s.nextGreaterElements(nums))