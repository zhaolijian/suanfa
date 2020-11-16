class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = []
        for i in range(len(nums)):
            if window and i - window[0] + 1 > k:
                window.pop(0)
            while window:
                temp = window[-1]
                if nums[i] > nums[temp]:
                    window.pop()
                else:
                    break
            window.append(i)
            if i + 1 >= k:
                res.append(nums[window[0]])
        return res


# import collections
#
#
# class Solution:
#     def maxSlidingWindow(self, nums, k: int):
#         # 两端可以插入删除的队列
#         q = collections.deque()
#         result = []
#         temp = k
#         if len(nums) != 0:
#             for j in range(k):
#                 q.append(nums[j])
#             for i in range(len(nums) - k + 1):
#                 max_ele = max(q)
#                 result.append(max_ele)
#                 if temp < len(nums):
#                     q.popleft()
#                     q.append(nums[temp])
#                     temp += 1
#         return result


# from collections import deque
#
# 先将k-1个数放入到双端队列中，如果后者比前者大，则删除所有前面小的
# 将第k个数放入双端队列中
# 去除双端队列第一个数字
# class Solution:
#     def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
#         q = deque()
#         result = []
#         if k == 0:
#             return result
#         elif k == 1:
#             return nums
#         else:
#             for i in range(k-1):
#                 # q不为空，并且前面的小于后面的，则递归删除前面的
#                 while q and q[len(q) - 1] < nums[i]:
#                     q.pop()
#                 q.append(nums[i])
#             for i in range(k-1, len(nums)):
#                 while q and q[len(q) - 1] < nums[i]:
#                     q.pop()
#                 q.append(nums[i])
#                 result.append(q[0])
#                 if q[0] == nums[i-k+1]:
#                     q.popleft()
#             return result


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output