# 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
# 返回仅包含 1 的最长（连续）子数组的长度。


# 双指针，窗口不会变小，只会变大，如果n>=k，则左右指针都右移，窗口的长度为仅包含1的最长子数组长度
class Solution:
    def longestOnes(self, A, K: int) -> int:
        length = len(A)
        left, right = 0, 0
        n = 0
        res = 0
        while right < length:
            if A[right] == 0:
                n += 1
            if n <= K:
                res = max(res, right - left + 1)
            else:
                if A[left] == 0:
                    n -= 1
                left += 1
            right += 1
        return res


if __name__ == '__main__':
    s = Solution()
    A = [1,1,1,0,0,0,1,1,1,1,0]
    K = 2
    print(s.longestOnes(A, K))