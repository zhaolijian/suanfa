# 最长重复子数组
# 方法1 dp
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_a, len_b = len(A), len(B)
        dp = [[0 for i in range(len_b + 1)] for j in range(len_a + 1)]
        res = 0
        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else 0
                res = max(res, dp[i][j])
        return res


# 方法2 滑动窗口
# 滑动窗口
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        def func(start_a, start_b, length):
            result = 0
            temp = 0
            for i in range(length):
                if A[start_a + i] == B[start_b + i]:
                    temp += 1
                    result = max(result, temp)
                else:
                    temp = 0
            return result

        res = 0
        len_a, len_b = len(A), len(B)
        # A滑动i个窗口向B靠齐
        for i in range(len_a):
            length = min(len_a - i, len_b)
            res = max(res, func(i, 0, length))
        # B滑动i个窗口向A靠齐
        for i in range(len_b):
            length = min(len_b - i, len_a)
            res = max(res, func(0, i, length))
        return res
