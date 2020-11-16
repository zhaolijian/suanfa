# 给定数组arr，设长度为n，输出arr的最长递增子序列。（如果有多个答案，请输出其中字典序最小的）
import bisect
class Solution:
    def LIS(self , arr ):
        # write code here
        n = len(arr)
        # 每个位置对应的长度
        dp = [1]*n
        lenth = 1
        # 递增序列
        array = [arr[0]]
        for i in range(1, n):
            if arr[i]>array[-1]:
                lenth += 1
                dp[i] = lenth
                array.append(arr[i])
            else:
                index = bisect.bisect(array, arr[i])
                dp[i] = index+1
                array[index] = arr[i]
        res = []
        max_num = array[-1]
        max_num_index = arr.index(max_num)
        lenth = max(dp)
        for i in range(max_num_index, -1, -1):
            if res == [] or (arr[i] < res[-1] and dp[i] == lenth):
                res.append(arr[i])
                lenth -= 1
        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    arr = [1, 3, 5, 2]
    print(s.LIS(arr))