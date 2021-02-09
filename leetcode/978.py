# 当 A 的子数组 A[i], A[i+1], ..., A[j] 满足下列条件时，我们称其为湍流子数组：
# 若 i <= k < j，当 k 为奇数时， A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
# 或 若 i <= k < j，当 k 为偶数时，A[k] > A[k+1] ，且当 k 为奇数时， A[k] < A[k+1]。
# 也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。
# 返回 A 的最大湍流子数组的长度。


# 普通dp
class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        length = len(arr)
        dp = [[1 for i in range(2)] for j in range(length)]
        for i in range(1, length):
            if arr[i] > arr[i - 1]:
                dp[i][0] = dp[i - 1][1] + 1
            elif arr[i] < arr[i - 1]:
                dp[i][1] = dp[i - 1][0] + 1
        res = 1
        for i in range(length):
            if dp[i][0] > res:
                res = dp[i][0]
            if dp[i][1] > res:
                res = dp[i][1]
        return res



# dp优化
class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        length = len(arr)
        last_up, last_down, cur_up, cur_down, res = 1, 1, 1, 1, 1
        for i in range(1, length):
            if arr[i] > arr[i - 1]:
                cur_up = last_down + 1
                cur_down = 1
            elif arr[i] < arr[i - 1]:
                cur_up = 1
                cur_down = last_up + 1
            else:
                cur_up, cur_down = 1, 1
            res = max(res, cur_up, cur_down)
            last_up, last_down = cur_up, cur_down
        return res


if __name__ == '__main__':
    s = Solution()
    arr = [9,4,2,10,7,8,8,1,9]
    print(s.maxTurbulenceSize(arr))