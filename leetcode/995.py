# 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0。
# 返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。

# 差分数组统计反转次数，复杂度O(len(A))
class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        length = len(A)
        # 两个相邻元素反转次数之差
        diff = [0] * (length + 1)
        res, revCnt = 0, 0
        for i in range(length):
            # revCnt表示当前位置需要反转的次数
            revCnt += diff[i]
            if (A[i] + revCnt) % 2 == 0:
                if i + K > length:
                    return -1
                res += 1
                revCnt += 1
                diff[i + K] += 1
        return res




# 超时，复杂度O(len(A) * K)
class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        left, length, res = 0, len(A), 0
        while left < length:
            if A[left] == 0:
                if left + K <= length:
                    res += 1
                    for i in range(left, left + K):
                        A[i] = 1 if A[i] == 0 else 0
                else:
                    return -1
            left += 1
        return res