# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
# 如果不存在满足条件的子数组，则返回 0

# 滑动窗口+单调队列
from collections import deque
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        length = len(nums)
        res, left, right = 0, 0, 0
        # queMin：单调递增（包括相等）的最小值队列
        # queMax: 单调递减（包括相等）的最大值队列
        queMin, queMax = deque(), deque()
        while right < length:
            while queMax and queMax[-1] < nums[right]:
                queMax.pop()
            while queMin and queMin[-1] > nums[right]:
                queMin.pop()
            queMax.append(nums[right])
            queMin.append(nums[right])
            while queMin and queMax and queMax[0] - queMin[0] > limit:
                if nums[left] == queMax[0]:
                    queMax.popleft()
                if nums[left] == queMin[0]:
                    queMin.popleft()
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res