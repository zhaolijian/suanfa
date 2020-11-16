# 最小的k个数
# 方法1 构建最大堆
import heapq
class Solution:
    def getLeastNumbers(self, arr, k: int):
        if k == 0:
            return []
        temp = arr[:k]
        heapq._heapify_max(temp)
        for i in range(k, len(arr)):
            if temp[0] > arr[i]:
                # 不能直接使用_heapreplace_max函数，因为这个函数不管arr[i]是否小于最大堆顶，都会先删除堆顶，再将arr[i]加入堆
                heapq._heapreplace_max(temp, arr[i])
        return temp

# 方法2 堆
# import heapq
# class Solution:
#     def getLeastNumbers(self, arr, k: int):
#         return heapq.nsmallest(k, arr)
#
# 方法3 归并排序
# class Solution:
#     def getLeastNumbers(self, arr, k: int):
#         def func(arr):
#             length = len(arr)
#             if length <= 1:
#                 return arr
#             mid = length // 2
#             left = func(arr[:mid])
#             right = func(arr[mid:])
#             i, j = 0, 0
#             result = []
#             while i < mid and j < length - mid:
#                 if left[i] < right[j]:
#                     result.append(left[i])
#                     i += 1
#                 else:
#                     result.append(right[j])
#                     j += 1
#             if i < mid:
#                 result += left[i: mid]
#             if j < length - mid:
#                 result += right[j: length - mid]
#             return result
#
#         return func(arr)[:k]


if __name__ == '__main__':
    s = Solution()
    arr = [3,2,1]
    k = 2
    print(s.getLeastNumbers(arr, k))