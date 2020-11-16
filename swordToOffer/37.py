# 统计一个数字在排序数组中出现的次数。


# 二分查找，复杂度：logn
class Solution:
    def GetNumberOfK(self, data, k):
        if len(data) == 0:
            return 0
        if len(data) == 1 and data[0] == k:
            return 1
        l, r = 0, len(data) - 1
        res = 0
        temp = -1
        while l < r:
            mid = (l + r) // 2
            if data[mid] > k:
                r = mid - 1
            elif data[mid] < k:
                l = mid + 1
            else:
                temp = mid
                break
        if temp == -1:
            return 0
        for i in range(temp, len(data)):
            if data[i] == k:
                res += 1
        for j in range(temp - 1, -1, -1):
            if data[j] == k:
                res += 1
        return res


# class Solution:
#     def GetNumberOfK(self, data, k):
#         sum = 0
#         for i in data:
#             if i == k:
#                 sum += 1
#         return sum