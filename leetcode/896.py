# 如果数组是单调递增或单调递减的，那么它是单调的。
# 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
# 当给定的数组 A 是单调数组时返回 true，否则返回 false。


# 方法1 一次遍历
class Solution:
    def isMonotonic(self, A):
        length = len(A)
        increase, decrease = True, True
        for i in range(1, length):
            if A[i] > A[i - 1]:
                decrease = False
            if A[i] < A[i - 1]:
                increase = False
            if not increase and not decrease:
                return False
        return True


# 方法2 两次遍历
class Solution:
    def isMonotonic(self, A):
        length = len(A)
        if length == 1:
            return True
        increase, decrease = True, True
        for i in range(1, length):
            if A[i] < A[i - 1]:
                increase = False
                break
        for i in range(1, length):
            if A[i] > A[i - 1]:
                decrease = False
                break
        return increase or decrease