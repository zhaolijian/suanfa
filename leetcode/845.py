# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
# B.length >= 3
# 存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
# （注意：B 可以是 A 的任意子数组，包括整个数组 A。）
# 给出一个整数数组 A，返回最长 “山脉” 的长度。
# 如果不含有 “山脉” 则返回 0。


# 方法1 dp
class Solution:
    def longestMountain(self, A) -> int:
        length = len(A)
        if length < 3:
            return 0
        # 每一个位置左侧符合条件的最长长度
        left = [0] * length
        # 每一个位置右侧符合条件的最长长度
        right = [0] * length
        res = 0
        for i in range(1, length):
            if A[i] > A[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(length - 1, 0, - 1):
            if A[i - 1] > A[i]:
                right[i - 1] = right[i] + 1
        for i in range(length):
            if left[i] > 0 and right[i] > 0:
                res = max(res, left[i] + right[i] + 1)
        return res


# 方法2，双指针
class Solution:
    def longestMountain(self, A) -> int:
        n = len(A)
        ans = left = 0
        while left + 2 < n:
            right = left + 1
            if A[left] < A[left + 1]:
                # 寻找山顶位置
                while right + 1 < n and A[right] < A[right + 1]:
                    right += 1
                # 说明right位置上为山顶位置
                if right < n - 1 and A[right] > A[right + 1]:
                    # 找到右山脚位置
                    while right + 1 < n and A[right] > A[right + 1]:
                        right += 1
                    ans = max(ans, right - left + 1)
                # 说明right位置为山脚或者A[right] = A[right + 1],那么right不可能为左山脚了,直接跳到right+1位置即可
                else:
                    right += 1
            left = right
        return ans