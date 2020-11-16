# 给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的）
from bisect import bisect_left
class Solution:
    def LIS(self , arr ):
        # write code here
        length = len(arr)
        if length <= 1:
            return arr
        # 每个位置对应的长度
        array = [1]
        # 递增序列
        l = [arr[0]]
        cur_len = 1
        res = []
        for i in range(1, length):
            if arr[i] > l[-1]:
                l.append(arr[i])
                cur_len += 1
                array.append(cur_len)
            else:
                index = bisect_left(l, arr[i])
                l[index] = arr[i]
                array.append(index + 1)
        max_index = arr.index(l[-1])
        cur_length = cur_len
        for i in range(max_index, -1, -1):
            if not res or (arr[i] < res[-1] and array[i] == cur_length):
                res.append(arr[i])
                cur_length -= 1
        return res[::-1]