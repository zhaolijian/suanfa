# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。


# 单调队列
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        res = []
        queue = []
        for i in range(k):
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])
        for i in range(k, len(nums)):
            if i - queue[0] >= k:
                queue.pop(0)
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        return res